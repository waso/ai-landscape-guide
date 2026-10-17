# 13. Infrastructure & ecosystem

*Cross-cutting: the hardware and software everything runs on*

Why NVIDIA, Hugging Face and PyTorch come up in every video.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### GPU { #gpu }

*Also known as:* NVIDIA H100 / B200, AMD MI300

The massively parallel processor that does nearly all training and inference.

**Why it matters:** Neural networks are mostly matrix multiplication, and GPUs do thousands of those in parallel; the reason AI progress tracks GPU supply.

<small>*Index aliases:* H100 / B200, NVIDIA</small>

### TPU { #tpu }

Google's custom accelerator, used for Gemini and available on Google Cloud.

**Why it matters:** The main non-NVIDIA option at frontier scale.

<small>*Index aliases:* TPU (Google)</small>

### Custom inference chips { #custom-inference-chips }

*Also known as:* Groq LPU, Cerebras, Trainium, Inferentia

Accelerators designed specifically for running (or training) models, often with very high token speed.

**Why it matters:** Why some providers serve 500+ tokens per second. (NVIDIA licensed Groq's technology in late 2025.)

<small>*Index aliases:* Groq / Cerebras</small>

### CUDA { #cuda }

NVIDIA's GPU programming platform.

**Why it matters:** The software moat: most frameworks and kernels target CUDA first, which keeps the ecosystem NVIDIA-first.

### VRAM / HBM (GPU memory) { #vram-hbm }

The GPU's memory. 80 GB on an H100, 24 GB on a consumer RTX 4090.

**Why it matters:** The hard limit on which models fit; most "can I run this?" questions are about VRAM.

<small>*Index aliases:* VRAM, HBM</small>

### Out of memory { #out-of-memory }

*Also known as:* OOM, CUDA OOM

The error when a model, batch or KV cache does not fit in GPU memory.

**Why it matters:** The most common error in any training or serving tutorial; fixes are smaller batch, quantization, gradient accumulation or a bigger GPU.

<small>*Index aliases:* OOM (out of memory)</small>

### NVLink, InfiniBand, cluster { #nvlink-infiniband-cluster }

High-speed interconnects joining thousands of GPUs into one training machine.

**Why it matters:** Training a frontier model is as much a networking problem as a maths problem.

<small>*Index aliases:* InfiniBand / NVLink</small>

### PyTorch { #pytorch }

The dominant deep-learning framework, and what Raschka's book uses. JAX (Google) and TensorFlow are the alternatives.

**Why it matters:** Nearly every tutorial, paper and model release is in PyTorch; learn it first.

<small>*Index aliases:* JAX / TensorFlow</small>

### Hugging Face { #hugging-face }

*Also known as:* Transformers library, Hub

The de-facto library and repository for open models, datasets and tokenizers.

**Why it matters:** The GitHub of models: where you download weights and the library that loads them in three lines.

<small>*Index aliases:* Hugging Face Hub</small>

### Safetensors / weights file { #safetensors-weights-file }

The standard file format for storing model parameters safely (no arbitrary code on load).

**Why it matters:** The file you actually download; safe to open unlike the older pickle format.

<small>*Index aliases:* Safetensors</small>

### Parameter count { #parameter-count }

*Also known as:* 7B, 70B, 405B

Model size in billions of weights.

**Why it matters:** A quick proxy for capability, memory and cost; the first number anyone quotes about a model.

### Model API { #model-api }

*Also known as:* Anthropic, OpenAI, Google, Bedrock, Vertex

Hosted access to a model: you send tokens, you get tokens, you pay per token.

**Why it matters:** The way most products use frontier models: no GPUs, no ops, pay per use.

### Inference providers { #inference-providers }

*Also known as:* Together, Fireworks, Groq; OpenRouter

Companies that host open-weight models behind an API, often cheaper or faster than running them yourself. OpenRouter is an aggregator: one API that routes to many providers, closed and open.

**Why it matters:** The middle path between a frontier API and self-hosting.

<small>*Index aliases:* Together / Fireworks / OpenRouter</small>

### GPU kernel / Triton { #gpu-kernel-triton }

A low-level program that runs on the GPU. FlashAttention is a kernel; Triton lets you write them in Python.

**Why it matters:** Where the big speed-ups come from; most engineers never write one, but the names come up.

<small>*Index aliases:* Triton</small>

### Serving on Kubernetes { #serving-on-kubernetes }

*Also known as:* GPU node pools, KServe, vLLM on GKE

Running inference engines as containers on GPU nodes, with autoscaling and the usual K8s plumbing.

**Why it matters:** How a self-hosted model becomes a production service; the same platform skills you already have apply.

<small>*Index aliases:* KServe / GKE GPU nodes</small>

### Local inference stack { #local-inference-stack }

*Also known as:* llama.cpp, Ollama, LM Studio

Tools for running open-weight models on your own laptop or server.

**Why it matters:** The fastest way to try an open model: one command, no cloud, full privacy.

### Apple Silicon / MLX { #apple-silicon-mlx }

Macs share memory between CPU and GPU, so a Mac with 64–512 GB of unified memory can run models that need several consumer GPUs; MLX is Apple's framework for it.

**Why it matters:** Why Mac laptops are popular for local LLMs despite having no NVIDIA GPU.

<small>*Index aliases:* MLX</small>

### Experiment tracking { #experiment-tracking }

*Also known as:* Weights & Biases, MLflow

Tools that log every training run's settings, loss curves and results.

**Why it matters:** How teams compare hundreds of runs without losing track of what worked.

### Notebooks { #notebooks }

*Also known as:* Jupyter, Colab, Kaggle

Interactive Python environments; Colab and Kaggle give free GPU time.

**Why it matters:** Where most tutorials (and Raschka's code) run; the cheapest way to get a GPU for an hour.

<small>*Index aliases:* Colab / Kaggle</small>
