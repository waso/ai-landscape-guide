# 6. The Transformer architecture

*Stage 2: the shape of the network before any weights are learned*

Nearly every LLM is a stack of identical Transformer blocks (Map 5). The terms here describe the parts of a block and the design choices between model families.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Transformer ★ <a id="transformer"></a>
The neural architecture from the 2017 paper "Attention Is All You Need": stacked blocks of attention plus feed-forward layers.

**Why it matters:** Processes all tokens in parallel (fast on GPUs) and lets any token look at any other (long-range context). Both are why it won.

### Attention ★ <a id="attention"></a>
A mechanism that lets each token look at other tokens and weigh how relevant they are, so context flows across the whole sequence in one step.

**Why it matters:** How the model knows that "it" refers to "the cat" ten words earlier. The core idea of modern AI.

### Self-attention <a id="self-attention"></a>
Attention where tokens attend to other tokens of the same sequence.

**Why it matters:** Lets every word be interpreted in the light of every other word in the text.

### Query, Key, Value <a id="query-key-value"></a>
*Also known as:* Q, K, V

Three projections of each token. A token's query is compared with every key to get weights, which are then applied to the values.

**Why it matters:** Think of a lookup: the query asks a question, keys say what each token offers, values are what gets returned.

### Scaled dot-product attention <a id="scaled-dot-product-attention"></a>
The actual attention formula: softmax(QKᵀ / √d) · V.

**Why it matters:** The one formula every video shows. Dividing by √d keeps the softmax from saturating so gradients stay healthy.

### Multi-Head Attention (MHA) <a id="multi-head-attention"></a>
Several attention operations run in parallel (heads), each free to focus on a different kind of relationship.

**Why it matters:** One head can track grammar while another tracks topic. More heads, richer understanding.

<small>*Index aliases:* MHA</small>

### Multi-Query / Grouped-Query Attention <a id="multi-query-grouped-query-attention"></a>
*Also known as:* MQA, GQA

Variants that share key/value projections across heads. Llama 2 (70B), Llama 3, Mistral and most 2024+ models use GQA.

**Why it matters:** Shrinks the KV cache several-fold, so inference is faster and cheaper with almost no quality loss.

### Multi-head Latent Attention (MLA) <a id="multi-head-latent-attention"></a>
DeepSeek's alternative to GQA: keys and values are compressed into a small latent vector per token, which is what the KV cache stores; they are expanded again when attention runs (DeepSeek-V2, V3, R1).

**Why it matters:** Cuts the KV cache far more than GQA with no quality loss, which is how DeepSeek serves long contexts cheaply.

<small>*Index aliases:* MLA</small>

### Causal (masked) attention <a id="causal-masked-attention"></a>
Masking so a token can only attend to earlier tokens.

**Why it matters:** Stops the model from cheating by looking at the answer during training, and is what makes it generate left to right.

<small>*Index aliases:* Causal mask, Masked attention</small>

### Attention mask <a id="attention-mask"></a>
The tensor that marks which positions may attend to which (causal mask, padding mask).

**Why it matters:** The practical implementation of "no peeking ahead" and "ignore padding".

### Quadratic cost of attention (O(n²)) <a id="quadratic-cost-of-attention"></a>
Every token compares itself with every other, so compute and memory grow with the square of the sequence length.

**Why it matters:** Why long context is expensive and why FlashAttention, sliding windows and state-space models exist.

<small>*Index aliases:* O(n²), O(n²) attention</small>

### Sliding-window attention / attention sinks <a id="sliding-window-attention-attention-sinks"></a>
Limiting each token to attend only to the last N tokens (sliding window), optionally keeping a few initial tokens always visible (attention sinks).

**Why it matters:** Makes very long inputs affordable at some cost in long-range recall; used in the original Mistral 7B and, mixed with global layers, in Gemma 2/3 and gpt-oss.

<small>*Index aliases:* SWA, Attention sinks</small>

### Cross-attention <a id="cross-attention"></a>
The decoder attending to the encoder's outputs, in encoder-decoder models.

**Why it matters:** How a translator model reads the source sentence while writing the target one.

### Decoder-only model <a id="decoder-only-model"></a>
*Also known as:* GPT, Llama, Claude, Gemini, Mistral

A Transformer with causal self-attention only, trained to predict the next token. The dominant LLM design.

**Why it matters:** Simplest design that scales; one model does understanding and generation. Almost every chat model is this.

### Encoder-only model <a id="encoder-only-model"></a>
*Also known as:* BERT, RoBERTa

A bidirectional Transformer good at understanding, classification and embeddings, but not at generating text.

**Why it matters:** Still the usual choice for cheap classification and small, fast embedding models, because it reads both directions at once; many top-scoring embedding models are now built on decoder-only LLMs.

### Encoder-decoder model <a id="encoder-decoder-model"></a>
*Also known as:* T5, BART, original Transformer

An encoder reads the input, a decoder writes the output.

**Why it matters:** Natural for translation and summarisation; largely displaced by decoder-only models that do everything.

<small>*Index aliases:* T5 / BART</small>

### Positional encoding / embedding <a id="positional-encoding-embedding"></a>
How the model knows token order, since attention by itself is order-blind. Sinusoidal in 2017, learned in GPT-2.

**Why it matters:** Without it, "dog bites man" and "man bites dog" look identical to the model.

<small>*Index aliases:* Positional embedding</small>

### Rotary Positional Embedding (RoPE) <a id="rotary-positional-embedding"></a>
Today's standard positional scheme: encodes position by rotating the Q and K vectors so attention depends on relative distance.

**Why it matters:** Does not extrapolate well on its own, but can be cheaply stretched to longer contexts (position interpolation, NTK-aware scaling, YaRN), which is what makes 128k-token contexts practical.

<small>*Index aliases:* RoPE</small>

### ALiBi <a id="alibi"></a>
*Also known as:* Attention with Linear Biases

A positional scheme with no position embeddings at all: a penalty proportional to the query–key distance is subtracted from each attention score, with a different slope per head (used by MPT and BLOOM).

**Why it matters:** Trains on short sequences and extrapolates to longer ones; the main rival to RoPE before RoPE won.

<small>*Index aliases:* ALiBi (positional biases)</small>

### Hidden state <a id="hidden-state"></a>
The vector representing a token at a given layer; the residual stream's value at that point.

**Why it matters:** What gets passed from block to block, and what the LM head reads at the end. "Hidden size" = its length.

### Transformer block / layer <a id="transformer-block-layer"></a>
One unit of [attention → add & norm → feed-forward → add & norm]. Models stack 32 to 100+ of them.

**Why it matters:** The repeating unit; a model is this block copied N times with different weights. See Map 5.

### Feed-forward in a block <a id="feed-forward-in-a-block"></a>
*Also known as:* MLP, SwiGLU

The per-token two-layer network after attention; it holds most of the parameters. SwiGLU is the gated variant most modern models use.

**Why it matters:** Attention moves information between tokens; the FFN processes it. Facts the model "knows" are mostly stored here.

### Residual stream <a id="residual-stream"></a>
The running vector per token that every block adds its contribution to.

**Why it matters:** Each block reads from and writes to it, so information from early layers survives to the end.

### Attention Residuals (AttnRes) <a id="attention-residuals"></a>
A 2026 variant of the residual stream (Moonshot AI): instead of adding every earlier layer's output with a fixed weight of 1, each layer attends over earlier outputs with learned, softmax-normalised weights.

**Why it matters:** Small but consistent gains for ~4% extra training cost; a sign that even the residual stream is still being redesigned.

<small>*Index aliases:* AttnRes</small>

### Pre-norm vs post-norm <a id="pre-norm-vs-post-norm"></a>
Whether normalization happens before or after each sub-layer. Pre-norm with RMSNorm is the modern choice.

**Why it matters:** Pre-norm trains more stably at scale, which is why GPT-2 onward switched to it.

<small>*Index aliases:* Pre-norm</small>

### QK-Norm <a id="qk-norm"></a>
*Also known as:* query-key normalization

Normalize the query and key vectors (RMSNorm or LayerNorm) before computing attention scores (Gemma 3, OLMo 2, Qwen3).

**Why it matters:** Stops attention logits from blowing up, which removes a common cause of loss spikes and allows higher learning rates.

<small>*Index aliases:* QKNorm</small>

### d_model, n_heads, n_layers (hidden size) <a id="d-model-n-heads-n-layers"></a>
The main shape hyperparameters of a Transformer: vector width per token, number of attention heads, number of stacked blocks.

**Why it matters:** Three numbers that describe a model's shape; parameter count follows from them (Map 5).

<small>*Index aliases:* Hidden size</small>

### Language-model head <a id="language-model-head"></a>
*Also known as:* LM head, unembedding

The final linear layer mapping each token's hidden state to logits over the vocabulary.

**Why it matters:** Turns the model's internal vector into "a score for every possible next token".

### Weight tying <a id="weight-tying"></a>
Reusing the token-embedding matrix as the LM head.

**Why it matters:** Saves a large chunk of parameters in small models (a third of GPT-2's).

### Mixture of Experts (MoE) <a id="mixture-of-experts"></a>
Replaces each feed-forward layer with several experts and a router that activates only a few per token (Mixtral, DeepSeek-V3, Qwen3-MoE).

**Why it matters:** Huge knowledge capacity with the compute cost of a much smaller model: a 235B model that runs like a 22B one.

<small>*Index aliases:* MoE</small>

### Dense vs sparse model <a id="dense-vs-sparse-model"></a>
A dense model uses all parameters for every token; a sparse (MoE) model uses a subset.

**Why it matters:** Explains names like "235B-A22B": 235B parameters total, 22B active per token.

<small>*Index aliases:* Sparse model, Dense model</small>

### FlashAttention <a id="flashattention"></a>
An exact but much faster, memory-efficient GPU implementation of attention.

**Why it matters:** Same maths, 2–4× faster and far less memory, by being clever about GPU memory traffic. An engineering trick, not a new architecture.

### State-space models / hybrids <a id="state-space-models-hybrids"></a>
*Also known as:* Mamba, SSM

Alternative sequence layers whose cost grows linearly with sequence length. Often mixed with attention layers.

**Why it matters:** A bet on cheaper long context; hybrids keep a few attention layers for precise recall.

### Vision Transformer (ViT) <a id="vision-transformer"></a>
A Transformer applied to image patches as if they were tokens.

**Why it matters:** Showed the same architecture works for images, which is what makes multimodal models possible.

<small>*Index aliases:* ViT</small>
