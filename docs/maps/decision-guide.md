# Map 7 — Decision guide

*Prompt, RAG, fine-tune, or train?*

Start at the left column and move right only if the cheaper fix fails. Most real problems never leave the first column.

| Symptom | First try (hours) | Then (days) | Last resort (weeks+) | Don't |
|---|---|---|---|---|
| **Wrong, outdated or missing facts**<br><small>Doesn't know your product, your docs, last week's data</small> | Put the facts in the prompt; add RAG or a search / DB tool | Improve retrieval: chunking, hybrid search, reranker, citations | Continued pre-training on your domain corpus (rare, expensive) | Fine-tuning is a poor way to teach facts: it is unreliable and goes stale. |
| **Right content, wrong form**<br><small>Wrong tone, format, length, language; ignores conventions</small> | Prompt engineering: explicit rules, few-shot examples, structured outputs | LoRA fine-tune on a few hundred ideal examples | Full fine-tune with thousands of examples | Pre-training. Style is cheap to teach; knowledge is not. |
| **Can't do the task at all**<br><small>Fails at multi-step reasoning, complex code, long planning</small> | Bigger or reasoning model; chain-of-thought; decompose into steps | Agent with tools: let it run code, search, check its work | RL fine-tuning with verifiable rewards on your task (research-grade) | Expecting a 7B model to match a frontier model by prompting harder. |
| **Too slow or too expensive**<br><small>Latency, token bill, GPU cost</small> | Shorter prompts, prompt caching, smaller model for easy requests (routing) | Quantization, speculative decoding, better serving engine, batching | Distill or fine-tune a small model to replace the big one on your task | Adding more context "to be safe": cost grows with every token. |
| **Unreliable or unsafe outputs**<br><small>Hallucinates, breaks JSON, follows injected instructions</small> | Structured outputs, validation, guardrails, grounding with citations | Evals + LLM-as-judge in CI; human-in-the-loop for risky actions | Fine-tune for refusal / format behaviour on your own red-team data | Trusting a single model call for anything irreversible. |
| **Needs a new language or deep specialist knowledge**<br><small>Low-resource language, dense legal / medical / scientific domain</small> | Pick a model already strong in it; RAG for the long tail | Continued pre-training on a large domain corpus, then SFT | Train from scratch | Training from scratch unless you are a lab; it costs millions and the base models are better than you can make. |

**The rule of thumb.** Prompting changes nothing and costs nothing: try it first. RAG adds *knowledge*. Fine-tuning changes *behaviour* (style, format, reliability on a narrow task) and is bad at adding knowledge. Continued pre-training adds deep knowledge but needs a corpus and real GPU time. Pre-training from scratch is for labs.

## Who does what

| Role | What they do | Stages |
|---|---|---|
| AI lab (OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek…) | Stages 1–4: collects data, designs the architecture, pre-trains, post-trains, publishes the model (closed API or open weights). | 5, 6, 7, 8 |
| ML / research engineer | Stage 5 and parts of 4: fine-tunes, distils, evaluates, runs training jobs on GPUs; writes PyTorch. | 9, 8, 12 |
| Software / platform engineer | Stages 6–7: serves or calls models, builds RAG, tools, agents and MCP servers, owns latency, cost, evals and observability. | 10, 11, 13 |
| Data scientist / analyst | Classic ML on tabular data (section 3), evaluation design, labelling guidelines, analysis of model outputs. | 3, 12 |

*Stage numbers refer to glossary sections.*
