# Model families and how to read a model name

Version numbers change every few months; family names and suffixes are what to recognise. Snapshot as of mid-2026 — **corrections welcome.**

| Lab | Families | Weights | Known for |
|---|---|---|---|
| **OpenAI** | GPT-4o / GPT-4.1 / GPT-5 (chat), o-series (reasoning), gpt-oss (open-weight, 2025) | Closed, except gpt-oss | ChatGPT; the API most tutorials use |
| **Anthropic** | Claude: Haiku (small), Sonnet (mid), Opus (large); extended thinking | Closed | Coding, agents, long context |
| **Google DeepMind** | Gemini (Flash, Pro; thinking); Gemma (open) | Gemini closed, Gemma open | Multimodal, 1M+ context; Gemma for local use |
| **Meta** | Llama 2 / 3 / 4 | Open weights | The family that started the open-weight ecosystem |
| **Mistral AI** | Mistral 7B, Mixtral (MoE), Codestral, Mistral Large | Mostly open | European lab; strong small models |
| **Alibaba** | Qwen 2.5 / 3 (dense + MoE), Qwen-VL, Qwen-Coder | Open weights | Widest range of open sizes; strong coding and multilingual |
| **DeepSeek** | DeepSeek-V3 (MoE), R1 (reasoning) | Open weights | Cheap frontier-class training; GRPO; open reasoning |
| **xAI** | Grok | Closed (older versions opened) | Large compute; integrated with X |
| **Microsoft** | Phi (small models) | Open weights | Small, synthetic-data-heavy models for edge |
| **AI2 (Allen Institute)** | OLMo, Tülu | Fully open (data + code) | The reference for truly open-source LLMs |
| **Others to recognise** | Cohere Command, NVIDIA Nemotron, Moonshot Kimi, Zhipu GLM, MiniMax, Stability AI (Stable Diffusion), Black Forest Labs (Flux) | Mixed | Appear in leaderboards and image / video news |

## Decoding a model name

| Pattern | Meaning |
|---|---|
| `Llama-3.1-8B-Instruct` | family · generation · parameter count · post-trained for chat |
| `Qwen3-235B-A22B` | 235B total parameters, 22B active per token: a Mixture of Experts |
| `Mixtral-8x7B` | 8 experts of ~7B each; ≈ 47B total, ≈ 13B active |
| `-Base / -Instruct / -Chat` | raw pre-trained model vs. post-trained assistant |
| `-R1, -Thinking, o1 / o3` | reasoning model: thinks before answering |
| `-mini, -nano, -flash, -haiku, -lite` | the small, fast, cheap tier of a family |
| `-VL, -vision, -omni` | accepts images (and audio / video) |
| `-Coder, -Code` | trained or tuned for programming |
| `-Distill-, DeepSeek-R1-Distill-Qwen-7B` | a small model trained to imitate a big one: teacher first (DeepSeek-R1), the small base model last (Qwen 7B) |
| `-Q4_K_M.gguf, -GPTQ, -AWQ, -FP8` | quantized files: 4-bit GGUF for llama.cpp / Ollama, GPTQ / AWQ for GPUs, FP8 for H100s |
| `-128k, -1M` | context window |
| `-v0.3, -2507` | revision or release date (July 2025) |
| `Dense vs MoE` | if no "A" number and no "x", it is probably dense: all parameters used for every token |

Three lineages to keep apart: **base → instruct → reasoning** (same family, more post-training each step); **dense vs MoE** (all parameters vs a routed subset per token); **full precision vs quantized file** (same model, fewer bits).
