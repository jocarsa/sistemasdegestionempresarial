entrenar:

GPU
python 004-entrenamiento.py \
  --model Qwen/Qwen2.5-3B-Instruct \
  --data "001-preguntas y respuestas.jsonl" \
  --output salida-qwen25-qa \
  --epochs 3 \
  --batch-size 2 \
  --grad-accum 8 \
  --lr 2e-4 \
  --max-length 512 \
  --use-4bit
CPU
python 004-entrenamiento.py \
  --model Qwen/Qwen2.5-3B-Instruct \
  --data "001-preguntas y respuestas.jsonl" \
  --output salida-qwen25-qa-cpu \
  --epochs 1 \
  --batch-size 1 \
  --grad-accum 1 \
  --lr 1e-4 \
  --max-length 256
  
inferir:

python 005-inferencia.py \
  --base-model Qwen/Qwen2.5-3B-Instruct \
  --adapter salida-qwen25-qa-v2 \
  --question "¿Quién es Jose Vicente Carratala en el contexto de este dataset?" \
  --use-4bit