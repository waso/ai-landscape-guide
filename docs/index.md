# The AI landscape field guide

**About 340 AI and machine-learning terms, explained in plain language and placed on a map of where they sit: pre-training, post-training, fine-tuning, inference, applications.**

Made for people who learn from videos and courses and keep meeting new acronyms. Every entry has a short definition and a *why it matters* line; seven maps show how the pieces fit together.

<div class="grid cards" markdown>

-   :material-magnify: **Heard a term?**

    ---

    Use the search box or the [A–Z index](index-a-z.md). Every acronym from the videos is there, including the ones that are only nicknames.

-   :material-map: **Want the big picture?**

    ---

    Start with the [seven maps](maps/big-picture.md): the nested circles of AI, the LLM lifecycle, the training loop, the life of one request, inside a Transformer block, RAG and agents, and a decision guide.

-   :material-book-open-variant: **Want it explained?**

    ---

    The [glossary](glossary/01-the-big-picture.md) has 14 sections ordered like the lifecycle, so neighbours on the map are neighbours on the page.

-   :material-source-pull: **Found a mistake, or a missing term?**

    ---

    This is a community document. [Open an issue or a pull request](https://github.com/waso/ai-landscape-guide) — see [how to contribute](contributing.md).

</div>

## The 14 sections

| # | Section | What it covers |
|---|---|---|
| 1 | [The big picture](glossary/01-the-big-picture.md) | How AI, ML, deep learning and LLMs relate |
| 2 | [Learning paradigms](glossary/02-learning-paradigms.md) | How a model learns: from labels, from structure, from itself, or from rewards |
| 3 | [Classic ML toolbox](glossary/03-classic-ml-toolbox.md) | Pre-deep-learning algorithms and the vocabulary of any ML project |
| 4 | [Neural-network foundations](glossary/04-neural-network-foundations.md) | The training loop and building blocks used by every stage that changes weights |
| 5 | [Data & tokenization](glossary/05-data-tokenization.md) | Stage 1 of the LLM lifecycle: what the model reads, and in what units |
| 6 | [The Transformer architecture](glossary/06-the-transformer-architecture.md) | Stage 2: the shape of the network before any weights are learned |
| 7 | [Pre-training](glossary/07-pre-training.md) | Stage 3: the expensive phase that produces a base model |
| 8 | [Post-training & alignment](glossary/08-post-training-alignment.md) | Stage 4: turning a base model into an assistant |
| 9 | [Adapting a model to your task](glossary/09-adapting-a-model-to-your-task.md) | Stage 5: your own fine-tuning on an open-weight or API model |
| 10 | [Inference & serving](glossary/10-inference-serving.md) | Stage 6: running the model to produce tokens, fast and cheaply |
| 11 | [Building applications](glossary/11-building-applications.md) | Stage 7: prompting, retrieval, tools and agents around a frozen model |
| 12 | [Evaluation, safety & interpretability](glossary/12-evaluation-safety-interpretability.md) | Cross-cutting: measuring, attacking and understanding models at every stage |
| 13 | [Infrastructure & ecosystem](glossary/13-infrastructure-ecosystem.md) | Cross-cutting: the hardware and software everything runs on |
| 14 | [Beyond text: vision, audio, video](glossary/14-beyond-text-vision-audio-video.md) | Cross-cutting: terms from image, speech and video AI that appear in general AI videos |

Sections 1–4 are the foundations, 5–11 follow the seven stages of the LLM lifecycle (see [Map 2](maps/lifecycle.md)), and 12–14 cut across all stages.

## Learn these 30 first

If you know only these, you can follow most videos. They are marked ★ in the glossary and listed here in the order of the map: the field → how models learn → inside the network → the lifecycle → using it.

| | | |
|---|---|---|
| [Model](glossary/01-the-big-picture.md#model) | [Neural Network](glossary/01-the-big-picture.md#neural-network) | [Training vs inference](glossary/01-the-big-picture.md#training-vs-inference) |
| [Large Language Model](glossary/01-the-big-picture.md#large-language-model) | [Supervised learning](glossary/02-learning-paradigms.md#supervised-learning) | [Self-supervised learning](glossary/02-learning-paradigms.md#self-supervised-learning) |
| [Reinforcement Learning](glossary/02-learning-paradigms.md#reinforcement-learning) | [Overfitting / underfitting](glossary/03-classic-ml-toolbox.md#overfitting-underfitting) | [Weights, biases, parameters](glossary/04-neural-network-foundations.md#weights-biases-parameters) |
| [Loss function](glossary/04-neural-network-foundations.md#loss-function) | [Backpropagation](glossary/04-neural-network-foundations.md#backpropagation) | [Gradient descent](glossary/04-neural-network-foundations.md#gradient-descent) |
| [Embedding](glossary/04-neural-network-foundations.md#embedding) | [Token](glossary/05-data-tokenization.md#token) | [Context window / context length](glossary/05-data-tokenization.md#context-window-context-length) |
| [Transformer](glossary/06-the-transformer-architecture.md#transformer) | [Attention](glossary/06-the-transformer-architecture.md#attention) | [Pre-training](glossary/07-pre-training.md#pre-training) |
| [Next-token prediction](glossary/07-pre-training.md#next-token-prediction) | [Base model](glossary/07-pre-training.md#base-model) | [Supervised Fine-Tuning](glossary/08-post-training-alignment.md#supervised-fine-tuning) |
| [Reinforcement Learning from Human Feedback](glossary/08-post-training-alignment.md#reinforcement-learning-from-human-feedback) | [Fine-tuning (your version)](glossary/09-adapting-a-model-to-your-task.md#fine-tuning-your-version) | [Low-Rank Adaptation](glossary/09-adapting-a-model-to-your-task.md#low-rank-adaptation) |
| [Inference](glossary/10-inference-serving.md#inference) | [Temperature](glossary/10-inference-serving.md#temperature) | [System prompt](glossary/11-building-applications.md#system-prompt) |
| [Agent](glossary/11-building-applications.md#agent) | [Retrieval-Augmented Generation](glossary/11-building-applications.md#retrieval-augmented-generation) | [Hallucination](glossary/11-building-applications.md#hallucination) |

## Maps and reference pages

| Map | What it shows |
|---|---|
| [Map 1 — The big picture](maps/big-picture.md) | The nested circles AI ⊃ ML ⊃ deep learning ⊃ Transformers, and the four ways a model can learn |
| [Map 2 — The LLM lifecycle](maps/lifecycle.md) | Seven stages, every term placed, and the one distinction that matters: do the weights change? |
| [Map 3 — The training loop](maps/training-loop.md) | Forward pass → loss → backprop → optimizer step; architecture families; a timeline |
| [Map 4 — Life of a request](maps/life-of-a-request.md) | What happens when your code calls a model, step by step |
| [Map 5 — Inside a Transformer block](maps/transformer-block.md) | The block with real tensor shapes; GPT-2 small vs Llama-3-8B |
| [Map 6 — RAG and agents](maps/rag-and-agents.md) | The retrieval pipeline and the agent loop, with MCP |
| [Map 7 — Decision guide](maps/decision-guide.md) | Prompt, RAG, fine-tune or train? Who does what |

| Reference | |
|---|---|
| [Software engineer's translation table](reference/translation-table.md) | Every AI concept mapped to something you already run in production, plus eight naming traps |
| [Orders of magnitude](reference/orders-of-magnitude.md) | Sizes, tokens, context windows, memory, GPUs, compute, cost |
| [Math-notation decoder](reference/math-notation.md) | The symbols that flash past on slides |
| [Model families](reference/model-families.md) | Who makes what, and how to read a model name |
| [Raschka's book → this guide](reference/raschka-book.md) | Chapter map for *Build a Large Language Model (From Scratch)* and a reading order |
| [The Stanford CME295 slide, decoded](guides/stanford-cme295-slide.md) | 35 acronyms from the course's lecture-1 slide, in its own grouping |
