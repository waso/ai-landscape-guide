# The AI landscape field guide

**About 340 AI and machine-learning terms — from classic ML to LLM agents — explained in plain language and placed on a map of where they sit: pre-training, post-training, fine-tuning, inference, applications.**

📖 **Read it online:** https://waso.github.io/ai-landscape-guide/

Made for people who learn from videos and courses and keep meeting new acronyms. Every entry has a short definition and a **why it matters** line; seven maps show how the pieces fit together.

![Map 2 — the LLM lifecycle](docs/assets/maps/map2-lifecycle.png)

## Start here

- 🔍 **Heard a term?** Look it up in the [A–Z index](docs/index-a-z.md). It has about 660 entries, including acronyms and nicknames.
- 🗺️ **Want the big picture?** Start with the [seven maps](#maps) below.
- 📖 **Want it explained?** Read the [glossary](#the-14-chapters) in order. Neighbours on the map are neighbours on the page.
- ⭐ **Short on time?** Learn the [30 terms marked ★](docs/index.md#learn-these-30-first) first.

## The 14 chapters

| # | Chapter | What it covers |
|---|---|---|
| 1 | [The big picture](docs/glossary/01-the-big-picture.md) | How AI, ML, deep learning and LLMs relate |
| 2 | [Learning paradigms](docs/glossary/02-learning-paradigms.md) | How a model learns: from labels, from structure, from itself, or from rewards |
| 3 | [Classic ML toolbox](docs/glossary/03-classic-ml-toolbox.md) | Pre-deep-learning algorithms and the vocabulary of any ML project |
| 4 | [Neural-network foundations](docs/glossary/04-neural-network-foundations.md) | The training loop and building blocks used by every stage that changes weights |
| 5 | [Data & tokenization](docs/glossary/05-data-tokenization.md) | Stage 1 of the LLM lifecycle: what the model reads, and in what units |
| 6 | [The Transformer architecture](docs/glossary/06-the-transformer-architecture.md) | Stage 2: the shape of the network before any weights are learned |
| 7 | [Pre-training](docs/glossary/07-pre-training.md) | Stage 3: the expensive phase that produces a base model |
| 8 | [Post-training & alignment](docs/glossary/08-post-training-alignment.md) | Stage 4: turning a base model into an assistant |
| 9 | [Adapting a model to your task](docs/glossary/09-adapting-a-model-to-your-task.md) | Stage 5: your own fine-tuning on an open-weight or API model |
| 10 | [Inference & serving](docs/glossary/10-inference-serving.md) | Stage 6: running the model to produce tokens, fast and cheaply |
| 11 | [Building applications](docs/glossary/11-building-applications.md) | Stage 7: prompting, retrieval, tools and agents around a frozen model |
| 12 | [Evaluation, safety & interpretability](docs/glossary/12-evaluation-safety-interpretability.md) | Cross-cutting: measuring, attacking and understanding models at every stage |
| 13 | [Infrastructure & ecosystem](docs/glossary/13-infrastructure-ecosystem.md) | Cross-cutting: the hardware and software everything runs on |
| 14 | [Beyond text: vision, audio, video](docs/glossary/14-beyond-text-vision-audio-video.md) | Cross-cutting: terms from image, speech and video AI that appear in general AI videos |

Chapters 1–4 are the foundations, 5–11 follow the seven stages of the LLM lifecycle (see [Map 2](docs/maps/lifecycle.md)), and 12–14 cut across all stages.

## Maps

| Map | What it shows |
|---|---|
| [Map 1 — The big picture](docs/maps/big-picture.md) | The nested circles AI ⊃ ML ⊃ deep learning ⊃ Transformers, and the four ways a model can learn |
| [Map 2 — The LLM lifecycle](docs/maps/lifecycle.md) | Seven stages, every term placed, and the one distinction that matters: do the weights change? |
| [Map 3 — The training loop](docs/maps/training-loop.md) | Forward pass → loss → backprop → optimizer step; architecture families; a timeline |
| [Map 4 — Life of a request](docs/maps/life-of-a-request.md) | What happens when your code calls a model, step by step |
| [Map 5 — Inside a Transformer block](docs/maps/transformer-block.md) | The block with real tensor shapes; GPT-2 small vs Llama-3-8B |
| [Map 6 — RAG and agents](docs/maps/rag-and-agents.md) | The retrieval pipeline and the agent loop, with MCP |
| [Map 7 — Decision guide](docs/maps/decision-guide.md) | Prompt, RAG, fine-tune or train? Who does what |

## Reference pages

| Reference | |
|---|---|
| [Software engineer's translation table](docs/reference/translation-table.md) | Every AI concept mapped to something you already run in production, plus eight naming traps |
| [Orders of magnitude](docs/reference/orders-of-magnitude.md) | Sizes, tokens, context windows, memory, GPUs, compute, cost |
| [Math-notation decoder](docs/reference/math-notation.md) | The symbols that flash past on slides |
| [Model families](docs/reference/model-families.md) | Who makes what, and how to read a model name |
| [Raschka's book → this guide](docs/reference/raschka-book.md) | Chapter map for *Build a Large Language Model (From Scratch)* and a reading order |
| [The Stanford CME295 slide, decoded](docs/guides/stanford-cme295-slide.md) | 35 acronyms from the course's lecture-1 slide, in its own grouping |

## Contributing

Corrections, clearer wording and missing terms are all welcome — this is meant to be a community document. The glossary is plain Markdown, one file per section, one entry per term, so a contribution is usually a small pull request. See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the entry format, the style rules and the fact-checking expectations, and use the issue templates for a *new term* or a *correction*.

Quick local preview:

```bash
pip install -r requirements.txt
python scripts/build_index.py      # regenerates docs/index-a-z.md from the glossary files
python scripts/check.py            # validates every entry
mkdocs serve                       # http://127.0.0.1:8000
```

The site is built and published to GitHub Pages automatically by [`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml) on every push to `main`.

## Accuracy

Every factual claim (dates, numbers, who uses what) was checked against primary sources before publication, and the pages that go stale fastest (orders of magnitude, model families) say so at the top. If you find something wrong, please open a correction issue with a source.

## Credits and licence

Created and maintained by Waldemar Sojka. The initial content was drafted with the help of Claude (Anthropic) and then fact-checked against primary sources; all remaining errors are the maintainer’s.

- Text, maps and diagrams: [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) — reuse freely with attribution.
- Scripts and site configuration: [MIT](LICENSE).
