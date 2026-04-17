#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
import argparse
from typing import Dict, Any, Tuple

import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
)
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig


SYSTEM_PROMPT = (
    "Eres un asistente educativo claro, preciso y útil. "
    "Responde en español de forma correcta y breve, salvo que se te pida más detalle. "
    "No inventes datos y limítate al conocimiento aprendido en el ajuste."
)


def build_messages(example: Dict[str, Any]) -> Dict[str, Any]:
    question = str(example.get("question", "")).strip()
    answer = str(example.get("answer", "")).strip()

    if not question or not answer:
        return {"messages": []}

    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }


def detect_hardware() -> Tuple[bool, bool, bool]:
    has_cuda = torch.cuda.is_available()
    supports_bf16 = False

    if has_cuda:
        major, _minor = torch.cuda.get_device_capability(0)
        supports_bf16 = major >= 8

    use_fp16 = has_cuda and not supports_bf16
    return has_cuda, supports_bf16, use_fp16


def estimate_warmup_steps(
    dataset_len: int,
    batch_size: int,
    grad_accum: int,
    epochs: int,
    warmup_ratio: float = 0.05,
) -> int:
    if dataset_len <= 0:
        return 10

    steps_per_epoch = math.ceil(dataset_len / max(1, batch_size * grad_accum))
    total_steps = max(1, steps_per_epoch * epochs)
    return max(1, int(total_steps * warmup_ratio))


def choose_target_modules(model_name: str) -> list[str]:
    """
    Selecciona módulos LoRA razonables para distintos modelos.
    Evita depender de 'all-linear', que no siempre funciona igual en todas las versiones.
    """
    name = model_name.lower()

    if "qwen" in name:
        return ["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"]

    if "llama" in name or "mistral" in name or "nous-hermes" in name:
        return ["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"]

    if "phi" in name:
        return ["q_proj", "k_proj", "v_proj", "dense", "fc1", "fc2"]

    if "gpt2" in name:
        return ["c_attn", "c_proj", "c_fc"]

    return ["q_proj", "k_proj", "v_proj", "o_proj"]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fine-tuning LoRA/QLoRA para JSONL con {question, answer}, con fallback automático a CPU"
    )
    parser.add_argument("--model", required=True, help="Modelo base de Hugging Face")
    parser.add_argument("--data", required=True, help="Archivo JSONL con question/answer")
    parser.add_argument("--output", required=True, help="Carpeta de salida")
    parser.add_argument("--epochs", type=int, default=6)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--grad-accum", type=int, default=8)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--use-4bit", action="store_true", help="Activar QLoRA si hay GPU CUDA")
    parser.add_argument("--logging-steps", type=int, default=5)
    parser.add_argument("--save-strategy", default="epoch", choices=["no", "steps", "epoch"])
    parser.add_argument("--save-steps", type=int, default=50)
    parser.add_argument("--lora-r", type=int, default=32)
    parser.add_argument("--lora-alpha", type=int, default=64)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    print("[1/8] Detectando hardware y precisión...")
    has_cuda, supports_bf16, use_fp16 = detect_hardware()
    use_bf16 = has_cuda and supports_bf16

    print(f"CUDA disponible: {has_cuda}")
    print(f"Soporta BF16:    {supports_bf16}")
    print(f"Usará BF16:      {use_bf16}")
    print(f"Usará FP16:      {use_fp16}")

    requested_4bit = args.use_4bit
    effective_4bit = requested_4bit and has_cuda

    if requested_4bit and not has_cuda:
        print("Aviso: se solicitó --use-4bit, pero no hay CUDA disponible.")
        print("       Se desactiva QLoRA automáticamente y se usará CPU en float32.")

    print("[2/8] Cargando tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        args.model,
        trust_remote_code=True,
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tokenizer.padding_side = "right"

    print("[3/8] Cargando dataset JSONL...")
    dataset = load_dataset("json", data_files=args.data, split="train")
    dataset = dataset.map(build_messages)
    dataset = dataset.filter(lambda x: len(x["messages"]) > 0)

    if len(dataset) == 0:
        raise ValueError("No hay ejemplos válidos en el JSONL.")

    print(f"Ejemplos válidos: {len(dataset)}")

    print("[4/8] Preparando configuración del modelo...")
    model_kwargs = {"trust_remote_code": True}

    if effective_4bit:
        compute_dtype = torch.bfloat16 if supports_bf16 else torch.float16
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
        model_kwargs["quantization_config"] = quant_config
        model_kwargs["device_map"] = "auto"
        print("Modo QLoRA 4-bit activado.")
        print(f"compute_dtype={compute_dtype}")
    else:
        if has_cuda:
            normal_dtype = torch.bfloat16 if supports_bf16 else torch.float16
            model_kwargs["torch_dtype"] = normal_dtype
            model_kwargs["device_map"] = "auto"
            print(f"Modo normal en GPU activado con torch_dtype={normal_dtype}.")
        else:
            model_kwargs["torch_dtype"] = torch.float32
            print("Modo CPU activado con torch.float32.")

    print("[5/8] Cargando modelo base...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        **model_kwargs,
    )
    model.config.use_cache = False

    if not has_cuda:
        model.to("cpu")

    print("[6/8] Preparando LoRA...")
    target_modules = choose_target_modules(args.model)
    print(f"Módulos objetivo LoRA: {target_modules}")

    peft_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=target_modules,
    )

    warmup_steps = estimate_warmup_steps(
        dataset_len=len(dataset),
        batch_size=args.batch_size,
        grad_accum=args.grad_accum,
        epochs=args.epochs,
        warmup_ratio=0.05,
    )

    if effective_4bit:
        optim_name = "paged_adamw_8bit"
    else:
        optim_name = "adamw_torch"

    print(f"Warmup steps: {warmup_steps}")
    print(f"Optimizador:  {optim_name}")

    print("[7/8] Preparando argumentos de entrenamiento...")
    training_args = SFTConfig(
        output_dir=args.output,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        logging_steps=args.logging_steps,
        save_strategy=args.save_strategy,
        save_steps=args.save_steps if args.save_strategy == "steps" else 500,
        bf16=use_bf16,
        fp16=use_fp16,
        report_to="none",
        warmup_steps=warmup_steps,
        lr_scheduler_type="cosine",
        optim=optim_name,
        dataloader_pin_memory=has_cuda,
        remove_unused_columns=False,
        max_length=args.max_length,
    )

    print("[8/8] Entrenando...")
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        peft_config=peft_config,
        processing_class=tokenizer,
    )

    trainer.train()

    print("Guardando adaptador LoRA...")
    trainer.model.save_pretrained(args.output)
    tokenizer.save_pretrained(args.output)

    print("Entrenamiento completado.")
    print(f"Salida guardada en: {args.output}")


if __name__ == "__main__":
    main()