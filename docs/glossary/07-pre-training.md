# 7. Pre-training

*Stage 3: the expensive phase that produces a base model*

Weeks on thousands of GPUs, predicting the next token over trillions of tokens. Done by labs; the output is a base model that completes text but does not yet follow instructions.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Pre-training ★ <a id="pre-training"></a>
The first and most expensive phase: train the randomly-initialised model on a massive corpus by predicting the next token.

**Why it matters:** Where the model learns language, facts and reasoning. Everything after only shapes how that knowledge is used.

### Next-token prediction ★ <a id="next-token-prediction"></a>
*Also known as:* causal language modelling, CLM

The pre-training objective: given the tokens so far, output a probability distribution over the next one.

**Why it matters:** A deceptively simple task: predicting the next word well enough requires understanding grammar, facts and logic.

<small>*Index aliases:* Causal language modelling (CLM)</small>

### Teacher forcing <a id="teacher-forcing"></a>
During training the model sees the true previous tokens as input, not its own guesses, so all positions train in one parallel pass.

**Why it matters:** Why training is fast (whole sequence at once) while generation is slow (one token at a time).

### Masked language modelling (MLM) <a id="masked-language-modelling"></a>
The BERT-style objective: hide random tokens and predict them from both sides.

**Why it matters:** Produces excellent understanding models (and embeddings) but not text generators.

<small>*Index aliases:* MLM, MLM (masked language modelling)</small>

### Base model ★ <a id="base-model"></a>
The raw pre-trained model: continues text well, does not yet follow instructions or chat.

**Why it matters:** Ask it a question and it may continue with more questions. Post-training turns it into an assistant.

### Checkpoint <a id="checkpoint"></a>
A saved snapshot of the weights (and optimizer state) during or after training.

**Why it matters:** Lets a run resume after a crash and lets researchers compare the model at different points.

### Perplexity <a id="perplexity"></a>
The standard measure of how well a language model predicts text: exp(loss). Lower is better.

**Why it matters:** A perplexity of 10 means the model is, on average, as uncertain as choosing among 10 equally likely tokens.

<small>*Index aliases:* PPL</small>

### Loss curve / validation loss <a id="loss-curve-validation-loss"></a>
Training loss over steps, alongside loss on held-out data. Validation loss rising while training loss falls means overfitting.

**Why it matters:** The main thing engineers watch during a run; a smooth downward curve means learning is working.

<small>*Index aliases:* Validation loss</small>

### Loss spikes / divergence <a id="loss-spikes-divergence"></a>
Sudden jumps in the loss during a long run: a bad batch, too high a learning rate or numerical trouble.

**Why it matters:** The nightmare of large training runs; gradient clipping, lower learning rates and restarting from a checkpoint are the usual fixes.

<small>*Index aliases:* Loss spike</small>

### Learning-rate schedule <a id="learning-rate-schedule"></a>
*Also known as:* warmup, cosine decay, WSD

Ramp the learning rate up at the start, hold, then decay it toward the end.

**Why it matters:** Warmup prevents early blow-ups; decay lets the model settle into a good minimum. Standard practice for every LLM run.

<small>*Index aliases:* Warmup / cosine decay</small>

### Gradient clipping <a id="gradient-clipping"></a>
Cap the gradient norm so one bad batch cannot blow up training.

**Why it matters:** A safety valve against exploding gradients and loss spikes.

### Gradient accumulation <a id="gradient-accumulation"></a>
Sum gradients over several mini-batches before updating.

**Why it matters:** Simulates a big batch on a small GPU, so you can train with less memory.

### Curriculum learning <a id="curriculum-learning"></a>
Ordering training data from easy to hard, or changing the data mix over the course of training.

**Why it matters:** Can make training faster and the final model better than feeding everything in random order.

### Mixed precision <a id="mixed-precision"></a>
*Also known as:* FP32, FP16, BF16, FP8

Using lower-precision numbers for speed and memory while keeping a master copy of the weights in FP32. BF16 is the norm; FP8 is arriving.

**Why it matters:** Roughly doubles throughput and halves activation memory versus FP32, with no loss in quality when done right; weight and optimizer memory stay similar because the FP32 master copy remains.

<small>*Index aliases:* BF16 / FP16 / FP8</small>

### FLOPs / compute budget <a id="flops-compute-budget"></a>
The total floating-point operations a training run uses, roughly 6 × parameters × tokens.

**Why it matters:** Compute is the currency labs plan in; "10²⁵ FLOPs" is how regulators and papers describe a model's size of effort.

### Model FLOPs Utilization (MFU) <a id="model-flops-utilization"></a>
What fraction of the GPUs' theoretical peak compute the training run actually achieves (typically 30–50%).

**Why it matters:** The efficiency score of a training run; low MFU means expensive GPUs sitting idle waiting for data or communication.

<small>*Index aliases:* MFU</small>

### Scaling laws <a id="scaling-laws"></a>
The empirical finding that loss improves smoothly and predictably as you scale parameters, data and compute together.

**Why it matters:** Why labs bet billions: you can predict how much better a 10× bigger model will be before training it.

### Chinchilla-optimal <a id="chinchilla-optimal"></a>
The 2022 rule of thumb of about 20 training tokens per parameter for a given training budget. Modern models are deliberately over-trained far beyond it.

**Why it matters:** Why an 8B model trained on 15T tokens beats older 70B models: small models are cheaper to serve, so extra training pays off.

<small>*Index aliases:* Chinchilla, Compute-optimal, Over-training</small>

### Emergent abilities <a id="emergent-abilities"></a>
Capabilities that appear only once models pass a certain scale (a contested idea).

**Why it matters:** The argument for scaling: arithmetic or multi-step reasoning seemed to switch on at size.

### Data / tensor / pipeline parallelism <a id="data-tensor-pipeline-parallelism"></a>
Three ways to split training across GPUs: by data batches, by slicing layers across devices, or by giving different layers to different devices.

**Why it matters:** How a model too big for one GPU is trained on thousands at once.

<small>*Index aliases:* Tensor parallelism, Pipeline parallelism, Data parallelism</small>

### FSDP / ZeRO <a id="fsdp-zero"></a>
*Also known as:* Fully Sharded Data Parallel

Techniques that shard the weights, gradients and optimizer state across GPUs.

**Why it matters:** Lets models far bigger than one GPU's memory train without complex manual splitting.

<small>*Index aliases:* FSDP, ZeRO (DeepSpeed)</small>

### Continued pre-training <a id="continued-pre-training"></a>
Keep pre-training a base model on new domain data (medical, legal, a new language, your company's docs) before any instruction tuning.

**Why it matters:** The way to add deep domain knowledge or a new language; much cheaper than training from scratch, much heavier than fine-tuning.

### Mid-training / annealing <a id="mid-training-annealing"></a>
The final pre-training phase on a higher-quality data mix with a decaying learning rate.

**Why it matters:** Increasingly where labs tune knowledge quality and inject maths, code and long-context ability.

<small>*Index aliases:* Annealing, Mid-training</small>
