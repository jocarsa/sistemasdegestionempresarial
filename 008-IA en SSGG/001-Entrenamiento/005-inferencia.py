#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel


SYSTEM_PROMPT = (
    "Eres un asistente educativo claro, preciso y útil. "
    "Responde en español de forma correcta y breve, salvo que se te pida más detalle. "
    "No inventes datos y limítate al conocimiento aprendido en el ajuste."
)


def detect_precision() -> tuple[bool, bool]:
    has_cuda = torch.cuda.is_available()
    supports_bf16 = False

    if has_cuda:
        major, _minor = torch.cuda.get_device_capability(0)
        supports_bf16 = major >= 8

    return has_cuda, supports_bf16


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inferencia con modelo base + adaptador LoRA"
    )
    parser.add_argument(
        "--base-model",
        required=True,
        help="Modelo base, por ejemplo: Qwen/Qwen2.5-3B-Instruct",
    )
    parser.add_argument(
        "--adapter",
        required=True,
        help="Carpeta del adaptador entrenado",
    )
    parser.add_argument(
        "--question",
        required=True,
        help="Pregunta a realizar",
    )
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=96,
        help="Máximo de tokens nuevos a generar",
    )
    parser.add_argument(
        "--use-4bit",
        action="store_true",
        help="Carga el modelo base en 4 bits",
    )
    parser.add_argument(
        "--merge-adapter",
        action="store_true",
        help="Fusiona el adaptador con el modelo base tras cargarlo",
    )
    args = parser.parse_args()

    has_cuda, supports_bf16 = detect_precision()

    print("[1/5] Cargando tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        args.base_model,
        trust_remote_code=True,
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("[2/5] Preparando configuración del modelo...")
    model_kwargs = {"trust_remote_code": True}

    if args.use_4bit:
        compute_dtype = torch.bfloat16 if supports_bf16 else torch.float16

        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )

        model_kwargs["quantization_config"] = quant_config
        model_kwargs["device_map"] = "auto"
        model_kwargs["dtype"] = compute_dtype
        print(f"Modo 4-bit activado con dtype={compute_dtype}.")
    else:
        normal_dtype = (
            torch.bfloat16 if supports_bf16
            else torch.float16 if has_cuda
            else torch.float32
        )
        model_kwargs["device_map"] = "auto" if has_cuda else None
        model_kwargs["dtype"] = normal_dtype
        print(f"Modo normal activado con dtype={normal_dtype}.")

    print("[3/5] Cargando modelo base...")
    base_model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        **model_kwargs,
    )

    print("[4/5] Cargando adaptador LoRA...")
    model = PeftModel.from_pretrained(base_model, args.adapter)

    if args.merge_adapter:
        print("Fusionando adaptador con el modelo base...")
        model = model.merge_and_unload()

    model.eval()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": args.question},
    ]

    prompt_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer(
        prompt_text,
        return_tensors="pt",
        truncation=True,
    )

    if has_cuda:
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

    print("[5/5] Generando respuesta...")
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=args.max_new_tokens,
            do_sample=False,
            repetition_penalty=1.05,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            use_cache=True,
        )

    input_len = inputs["input_ids"].shape[1]
    generated_tokens = output[0][input_len:]
    answer = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    ).strip()

    print("\n=== PREGUNTA ===")
    print(args.question)
    print("\n=== RESPUESTA ===")
    print(answer if answer else "[Sin respuesta generada]")


if __name__ == "__main__":
    main()