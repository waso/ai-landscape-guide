# Orders of magnitude

Rough numbers to calibrate against when a video says “a 70B model”, “128k context” or “trained on 15 trillion tokens”. Treat every figure as ±50%; the point is the exponent, not the digit. Snapshot as of 2026 — **this page goes stale fastest; corrections welcome.**

## Model sizes (parameters)

| | |
|---|---|
| GPT-2 small (2019; Raschka's model) | **124M** |
| BERT-base | **110M** |
| Typical embedding model | **100M–1B** |
| "Small" open LLMs (Llama 3 8B, Mistral 7B, Qwen 7B) | **7–9B** |
| Mid-size open LLMs | **27–70B** |
| Large open MoE (DeepSeek-V3: 671B total / 37B active) | **100B–700B total** |
| Frontier closed models | **undisclosed; estimated hundreds of billions to trillions, mostly MoE** |

## Training data (tokens)

| | |
|---|---|
| GPT-2 (WebText) | **≈ 10B** |
| GPT-3 (2020) | **300B** |
| Chinchilla rule of thumb | **20 × parameters** |
| Llama 2 (2023) | **2T** |
| Llama 3 (2024) | **15T** |
| Qwen3 (2025) | **36T** |
| All of English Wikipedia | **≈ 5–6B** |

## Context windows (tokens)

| | |
|---|---|
| GPT-2 | **1k** |
| GPT-3 / early ChatGPT | **2k–4k** |
| GPT-4 (2023) | **8k–32k** |
| Llama 3.1, most 2024+ open models | **128k** |
| Claude | **200k–1M** |
| Gemini | **1M+** |
| A 300-page book | **≈ 150k** |

## Token rules of thumb

| | |
|---|---|
| 1 token | **≈ 4 characters ≈ ¾ of an English word** |
| 1 page of text | **≈ 500 tokens** |
| Polish vs English, same text | **≈ 2× more tokens (1.5–2.5× by tokenizer)** |
| A typical image in a VLM | **≈ 250–1,500 tokens** |
| A full-day meeting transcript | **≈ 80–100k tokens** |

## Memory: bytes per parameter

| | |
|---|---|
| FP32 | **4 B → 8B model = 32 GB** |
| BF16 / FP16 | **2 B → 8B model = 16 GB, 70B = 140 GB** |
| INT8 | **1 B → 8B model = 8 GB** |
| INT4 (Q4 GGUF) | **0.5 B → 8B model ≈ 4–5 GB, 70B ≈ 40 GB** |
| Full fine-tuning with AdamW (weights + grads + optimizer) | **≈ 16 B per parameter → 8B model ≈ 128 GB + activations** |
| KV cache | **grows with context × batch; can exceed the weights for long contexts** |

## GPU memory

| | |
|---|---|
| RTX 4090 / 5090 (consumer) | **24 / 32 GB** |
| A100 | **40 / 80 GB** |
| H100 / H200 | **80 / 141 GB** |
| B200 | **≈ 180–192 GB** |
| Mac with unified memory | **up to 192–512 GB shared** |

## Compute and time

| | |
|---|---|
| Training FLOPs | **≈ 6 × parameters × tokens (Llama 3 8B ≈ 7 × 10²³)** |
| Llama 3.1 training (Meta's figures) | **8B ≈ 1.5M H100-hours · 70B ≈ 7.0M · 405B ≈ 31M** |
| Pre-training wall clock | **weeks to months** |
| Post-training | **days to weeks** |
| LoRA fine-tune of a 7B model | **minutes to a few hours on one GPU** |
| Inference latency | **TTFT 0.2–2 s · decode 20–200 tokens/s per request** |

## Cost (order of magnitude, 2026)

| | |
|---|---|
| Frontier pre-training run | **$10M–$1B+** |
| Post-training | **$100k–$100M (RL phases are growing)** |
| Your LoRA fine-tune | **$1–$100 of GPU time** |
| API, small / fast models | **cents to about a dollar per million tokens** |
| API, frontier models | **dollars to tens of dollars per million tokens; output 3–8× input; cached input much cheaper** |
| Renting one H100 | **≈ $2–4 per hour** |
