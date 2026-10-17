# Software engineer's translation table

Every AI concept mapped to something you already run in production. The analogies are imperfect on purpose; the third column says where they break.

| AI term | Closest thing you know | How it maps, and where it breaks |
|---|---|---|
| **Model (weights)** | A compiled binary / artifact | You cannot read it; it was produced by a build (training) you probably did not run. |
| **Training** | The build pipeline | Hours to weeks, expensive, produces one artifact. You rarely rebuild; you configure around the artifact. |
| **Inference** | Runtime / executing the binary | Pure function of input + weights. No state change. |
| **Pre-training vs post-training** | Compiling the kernel vs. configuring the distro | One is the giant general build; the other makes it usable for people. |
| **Fine-tuning (LoRA)** | A patch / plugin on the artifact | Small diff on top of the original; swap it in and out. |
| **Prompt / system prompt** | Request payload + config file | The system prompt is config that ships with your app; the user message is the request. |
| **Context window** | Max request size (plus response) | Hard limit; everything you want the model to consider must fit. |
| **Tokens** | The billing and sizing unit | Like bytes for storage: context limits, speed and price are all per token. |
| **Temperature** | A randomness / seed setting | 0 = deterministic-ish; higher = more variety. |
| **Embeddings + vector DB** | An index for fuzzy, by-meaning lookup | Like a search index, but similarity is semantic rather than keyword. |
| **RAG** | A DB lookup before the call | Fetch relevant rows, put them in the request, then call the model. |
| **Tool use / function calling** | The model emitting a method call you execute | The model returns {name, args}; your code runs it and returns the result. |
| **Agent** | A while-loop with function calls and a stop condition | while not done: call model → maybe call tool → append result. |
| **MCP** | An interface spec (like OpenAPI / JDBC) for tools | Implement the server once; any compliant client can call it. |
| **Hallucination** | A confident bug with no stack trace | The output is well-formed and wrong. Validate, ground, test. |
| **Evals** | Your test suite | Run on every prompt or model change; LLM-as-judge is a flaky-but-useful assertion. |
| **Observability / tracing** | Logs, metrics, traces | Same tools (OpenTelemetry), same reasons. |
| **Prompt injection** | SQL injection for LLMs | Untrusted input interpreted as instructions. Treat all retrieved content as data. |
| **Guardrails** | Input validation + output validation | Schema checks, classifiers, allow-lists, around the model call. |
| **Model API vs self-hosting** | SaaS vs running it on your own GKE | Same trade-offs: ops burden, cost at scale, data residency, control. |

## Eight naming traps that confuse everyone

**“Fine-tuning” means two things** — Labs say it for post-training (SFT, RLHF) that turns a base model into a chat model. Engineers say it for adapting a finished model to their own task (LoRA). Same mechanics, different stage and budget.

**“Training” vs “inference”** — Training changes weights (stages 3–5). Inference only runs the frozen weights (stage 6). Prompting, RAG and agents never change weights; they are inference-time engineering (stage 7).

**“Alignment” is both a goal and a stage** — As a goal: the model behaves as intended. As a stage: the RLHF / DPO / safety part of post-training.

**Model, weights, checkpoint, parameters** — All the same thing from different angles: the learned numbers. A checkpoint is a saved copy; parameters count them; weights is the file you download.

**Supervised vs self-supervised** — Same loss, same loop. The difference is where the label comes from: a human (SFT) or the data itself (next token).

**Agent vs model** — A model answers once. An agent is a model in a loop with tools, memory and a stopping rule. The agent is code you write; the model is the thing it calls.

**Embedding (the layer) vs embeddings (the API)** — Inside an LLM, the embedding layer turns token IDs into vectors. An “embedding model” or embeddings API is a separate model that turns whole texts into vectors for search. Same idea, different object.

**Context window vs memory** — The context window is the model’s working memory for one request. “Memory” features are retrieval: facts stored outside and pasted back in. The model itself remembers nothing between calls.
