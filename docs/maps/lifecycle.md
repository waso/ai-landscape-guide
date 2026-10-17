# Map 2 — The LLM lifecycle

*Where every term lives.*

Left to right is the order things happen. Stages 1–4 are done once by an AI lab and cost millions; stage 5 is where you fine-tune; stages 6–7 are what every application does. **Weights change only in stages 3, 4 and 5.** The numbers are the glossary sections.

[![Map 2: the LLM lifecycle](../assets/maps/map2-lifecycle.png)](../assets/maps/map2-lifecycle.png)

*Click the image to open it full size.*

## The seven stages

| Stage | Section | Who does it, cost | Weights change? | Typical scale | Output |
|---|---|---|---|---|---|
| **1. Data & tokenization** — *raw text → tokens* | [5](../glossary/05-data-tokenization.md) | Lab · collected once | no | trillions of tokens | — |
| **2. Architecture** — *the Transformer, no weights yet* | [6](../glossary/06-the-transformer-architecture.md) | Lab · designed once | no | a few hundred lines of code | — |
| **3. Pre-training** — *self-supervised* | [7](../glossary/07-pre-training.md) | Lab · $10M–$1B · weeks | YES | 10¹³ tokens · 10³–10⁵ GPUs | Base model |
| **4. Post-training** — *supervised + reinforcement* | [8](../glossary/08-post-training-alignment.md) | Lab · $100k–$100M · days–weeks | YES | 10⁴–10⁷ examples · 10²–10⁴ GPUs | Instruct / chat model |
| **5. Adaptation** — *supervised (transfer learning)* | [9](../glossary/09-adapting-a-model-to-your-task.md) | You · $10–$10k · hours | YES (a little) | 10²–10⁴ examples · 1 GPU | Your specialised model |
| **6. Inference & serving** — *no learning, weights frozen* | [10](../glossary/10-inference-serving.md) | Anyone · per token | no | ms per token · 1 GPU or an API | Tokens |
| **7. Applications** — *engineering around the model* | [11](../glossary/11-building-applications.md) | You · product | no | your code · your data | Product |

### Terms by stage

**1. Data & tokenization** — Corpus, Token, Tokenizer, BPE, SentencePiece, Vocabulary, Special tokens, Context window, Dedup / filtering, Data mixture, Synthetic data, Chat template

**2. Architecture** — Transformer, Attention, Q / K / V, Multi-head (MHA), GQA / MQA, Causal mask, Embeddings, RoPE, Transformer block, FFN / SwiGLU, RMSNorm, QK-Norm, Residual stream, LM head, MoE, MLA, FlashAttention, Decoder-only · BERT · T5, Mamba / SSM

**3. Pre-training** — Next-token prediction, Cross-entropy loss, Backprop, AdamW, LR schedule, Batch / epoch, BF16 mixed precision, Gradient clipping, Scaling laws, Chinchilla, FLOPs, Data / tensor / pipeline parallel, FSDP / ZeRO, Checkpoint, Perplexity, Continued pre-training

**4. Post-training** — SFT / instruction tuning, Preference data, Reward model, RLHF, PPO, DPO, GRPO, GSPO, RLAIF / Constitutional AI, RLVR, Reasoning models, KL penalty, Reward hacking, Rejection sampling, Distillation, Safety training

**5. Adaptation** — Fine-tuning, Full fine-tune, PEFT, LoRA, QLoRA, Adapters, Rank / alpha, Catastrophic forgetting, Domain adaptation, Open weights, HF PEFT / TRL, Eval set

**6. Inference & serving** — Autoregressive, Prefill / decode, KV cache, Temperature, Top-k / Top-p, Greedy, Beam search, Logprobs, Streaming, TTFT · TPOT, Continuous batching, Quantization INT8 / INT4, GGUF, Speculative decoding, vLLM · llama.cpp, Prompt caching

**7. Applications** — Prompt engineering, System prompt, Zero- / few-shot, Chain-of-thought, Structured outputs, Tool use, Agents, MCP, RAG, Embeddings, Vector DB, Chunking, Reranker, Context engineering, Guardrails, Prompt injection, LLM-as-judge, Observability

### Cross-cutting bands

**NN foundations** ([section 4](../glossary/04-neural-network-foundations.md); *the training loop, used wherever weights change: stages 3, 4, 5*) — Forward pass, Loss function, Backprop, Gradient descent, Optimizer, Learning rate, Dropout, Weight decay, Overfitting, Embedding, Softmax, Logits, LayerNorm, Residual

**Evaluation & safety** ([section 12](../glossary/12-evaluation-safety-interpretability.md); *every stage*) — Benchmarks: MMLU · GPQA · SWE-bench, Held-out test set, Contamination, Arena / Elo, Hallucination, Red teaming, Jailbreak, Alignment, Interpretability / SAE, Model card

**Infrastructure** ([section 13](../glossary/13-infrastructure-ecosystem.md); *every stage*) — GPU / TPU, CUDA, VRAM / HBM, NVLink · cluster, PyTorch / JAX, Hugging Face, Safetensors, Kernels / Triton, Model API

**Beyond text** ([section 14](../glossary/14-beyond-text-vision-audio-video.md); *same ideas on pixels and audio: section 14*) — CLIP, VLM, Vision encoder, Latent diffusion, DiT, ControlNet, Whisper / ASR, TTS, Text-to-video

## Three things to remember

- **Reading tip.** A video about “training” is about stages 3–5. A video about “fine-tuning” is usually stage 5 (yours) but sometimes stage 4 (the lab’s). Anything about prompts, RAG, tools or agents is stage 7 and never touches the weights.
- **Three models, one lineage.** Base model (after 3) → instruct / chat model (after 4) → your specialised model (after 5). `Llama-3-8B` is a base model; `Llama-3-8B-Instruct` has been through stage 4.
- **Same loop, different data.** Stages 3, 4 and 5 all run the [training loop of Map 3](training-loop.md). What changes is the data (web text, human preferences, your examples), the scale, and who pays.
