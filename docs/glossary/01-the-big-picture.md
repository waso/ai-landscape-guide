# 1. The big picture

*How AI, ML, deep learning and LLMs relate*

These are the nested circles of Map 1. Every other term in this guide lives somewhere inside them.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Model ★ { #model }

A function with learned parameters: input goes in, a prediction comes out. On disk it is a file of numbers (the weights) plus the code that runs them.

**Why it matters:** When a video says "the model", it means this: a big file of numbers and the program that applies them.

### Artificial Intelligence (AI) { #artificial-intelligence }

Umbrella term for any technique that lets computers do things that normally need human intelligence, from hand-written rules to learned neural networks.

**Why it matters:** The whole field. Everything else in this guide is a sub-topic of it.

<small>*Index aliases:* AI</small>

### Machine Learning (ML) { #machine-learning }

Sub-field of AI where the program learns patterns from examples instead of being explicitly programmed with rules.

**Why it matters:** Solves problems where nobody can write the rules by hand: recognising a face, judging spam, predicting churn.

<small>*Index aliases:* ML</small>

### Deep Learning (DL) { #deep-learning }

ML using neural networks with many layers. The approach behind modern vision, speech and language models.

**Why it matters:** More layers let the network learn more abstract patterns (edges → shapes → objects; letters → words → meaning). This is what made today's AI possible.

<small>*Index aliases:* DL</small>

### Neural Network (NN) ★ { #neural-network }

A model built from layers of simple units (neurons) that pass weighted signals forward. Training adjusts the weights.

**Why it matters:** The basic machine every deep-learning model, including every LLM, is built from.

<small>*Index aliases:* NN</small>

### Training vs inference ★ { #training-vs-inference }

Training adjusts the weights using data: expensive, done rarely, by whoever builds the model. Inference runs the frozen weights to get an answer: cheap, done billions of times, by everyone.

**Why it matters:** The most important split on the map: stages 3–5 train, stages 6–7 only infer. Prompting and RAG never change the weights.

### Generative AI (GenAI) { #generative-ai }

Models that produce new content (text, images, audio, code) rather than only predicting a label or a number.

**Why it matters:** The shift from AI that classifies things to AI that makes things.

<small>*Index aliases:* GenAI</small>

### Large Language Model (LLM) ★ { #large-language-model }

A very large neural network (almost always a Transformer) trained on huge amounts of text to predict the next token. The engine behind chatbots and coding assistants.

**Why it matters:** The thing you talk to in ChatGPT or Claude. The central object of this guide; stages 1–7 of Map 2 describe its life.

<small>*Index aliases:* LLM</small>

### Foundation model { #foundation-model }

A big general-purpose model trained once on broad data and then adapted to many tasks. LLMs are the best-known example.

**Why it matters:** Train once, expensively; reuse everywhere, cheaply. This economics is why a few labs train and everyone else adapts.

### Frontier model / frontier lab { #frontier-model-frontier-lab }

The most capable models available at a given moment, and the handful of companies that train them (OpenAI, Anthropic, Google DeepMind, Meta, xAI, and a few Chinese labs).

**Why it matters:** "Frontier" in a video simply means "the best there is right now".

<small>*Index aliases:* Frontier lab</small>

### Multimodal model { #multimodal-model }

A model that handles more than one data type (text + images + audio + video) as input and/or output.

**Why it matters:** Lets one model read a screenshot, listen to a voice note, and answer in text. See section 14.

<small>*Index aliases:* Multimodal (section 14)</small>

### Natural Language Processing (NLP) { #natural-language-processing }

The field of making computers understand and generate human language. LLMs are its current state of the art.

**Why it matters:** The older name for the discipline; many pre-2020 techniques (word2vec, BERT, parsing) come from here.

<small>*Index aliases:* NLP</small>

### Computer Vision (CV) { #computer-vision }

The field of understanding images and video. Historically CNNs, increasingly Transformers (ViT).

**Why it matters:** Where deep learning first proved itself (ImageNet, 2012), and where many terms like "convolution" come from.

<small>*Index aliases:* CV, Computer vision (CV)</small>

### Discriminative vs generative model { #discriminative-vs-generative-model }

A discriminative model learns to separate or label inputs (spam / not spam). A generative model learns the distribution of the data, so it can produce new samples.

**Why it matters:** Tells you whether a model judges inputs or produces outputs. A spam filter is discriminative; an LLM is generative.

### Narrow AI vs AGI { #narrow-ai-vs-agi }

*Also known as:* Artificial General Intelligence

Narrow AI does one task well. AGI would match humans across most intellectual tasks; it is a goal and a debate, not a product.

**Why it matters:** When people argue about AGI timelines, this is the term; nothing you can download today is AGI.

<small>*Index aliases:* AGI</small>

### Symbolic AI { #symbolic-ai }

*Also known as:* GOFAI, expert systems

The older, rule- and logic-based approach to AI. Contrasts with learning from data. Still used inside planners and some hybrid systems.

**Why it matters:** Explains why "AI" in a 1990s product meant if/else rules, and why "neuro-symbolic" means mixing the two.

<small>*Index aliases:* Expert systems / GOFAI</small>
