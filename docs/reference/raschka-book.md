# Raschka's *Build a Large Language Model (From Scratch)* → this guide

The book builds GPT-2 small by hand and walks stages 1–3 and 5 of [Map 2](../maps/lifecycle.md) on a laptop (plus instruction SFT, a taste of stage 4). Here is where each chapter lands in the glossary and the maps.

| Chapter | What it builds | In this guide |
|---|---|---|
| **Ch. 1 — Understanding large language models** | What an LLM is, the GPT lineage, pre-train then fine-tune | Sections 1, 2, 6 · Map 1, Map 2 |
| **Ch. 2 — Working with text data** | Tokenization, BPE, sliding-window input–target pairs, token and positional embeddings | Section 5 (tokenizer, BPE, input–target pairs) · section 4 (embedding) · section 6 (positional) |
| **Ch. 3 — Coding attention mechanisms** | Simplified → trainable self-attention, causal mask, dropout, multi-head attention | Section 6 (attention, Q/K/V, causal mask, MHA) · Map 5 |
| **Ch. 4 — Implementing a GPT model from scratch** | LayerNorm, GELU, feed-forward, shortcut connections, the Transformer block, GPT-2 124M | Section 4 (normalization, activation, residual) · section 6 (block, LM head) · Map 5 |
| **Ch. 5 — Pretraining on unlabeled data** | Cross-entropy loss, perplexity, the training loop, temperature and top-k decoding, loading OpenAI's GPT-2 weights | Section 7 (pre-training, loss, perplexity) · section 10 (temperature, top-k) · Map 3, Map 4 |
| **Ch. 6 — Fine-tuning for classification** | Spam classifier: replace the LM head with a classification head, fine-tune the last layers | Section 9 (task head, fine-tuning) · section 2 (supervised) · section 3 (metrics) |
| **Ch. 7 — Fine-tuning to follow instructions** | Instruction dataset (Alpaca format), SFT, evaluating responses with another LLM | Section 8 (SFT, instruct model) · section 9 (instruction dataset, formats) · section 12 (LLM-as-judge) |
| **Appendix A — Introduction to PyTorch** | Tensors, autograd, modules, data loaders, GPU | Section 4 (tensor, autograd) · section 13 (PyTorch, GPU) |
| **Appendix D — Adding bells and whistles to the training loop** | Learning-rate warmup, cosine decay, gradient clipping | Section 7 (LR schedule, gradient clipping) |
| **Appendix E — Parameter-efficient fine-tuning with LoRA** | LoRA layers, rank and alpha, replacing linear layers | Section 9 (LoRA, rank / alpha, PEFT) |

## Suggested reading order through this guide

- **Start** — Section 1 and Map 1: the vocabulary of the field and where LLMs sit.
- **Then** — Section 2 and the paradigm table: supervised / self-supervised / RL are the three words that unlock everything else.
- **Core** — Sections 4 → 5 → 6 with Maps 3 and 5: the training loop, tokens, the Transformer. This is Raschka chapters 2–4.
- **Lifecycle** — Sections 7 → 8 → 9 with Map 2: pre-training, post-training, your fine-tuning. Raschka chapters 5–7.
- **Using it** — Sections 10 → 11 with Maps 4, 6 and 7: inference, prompting, RAG, agents, MCP. Your day job.
- **Later** — Sections 3, 12, 13, 14 as reference; the math decoder and model families when a video throws a symbol or a name at you.

What the book does not cover, and where to find it here: post-training with RL (section 8), inference engineering (section 10, Map 4), RAG and agents (section 11, Map 6), evaluation (section 12), multimodal (section 14).
