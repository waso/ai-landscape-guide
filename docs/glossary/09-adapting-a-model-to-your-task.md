# 9. Adapting a model to your task

*Stage 5: your own fine-tuning on an open-weight or API model*

This is where a company or an individual steps in. Usually hours on one GPU with a few thousand examples. Try prompting and RAG first (Map 7); fine-tune for style, format, latency or truly niche tasks.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Fine-tuning (your version) ★ { #fine-tuning-your-version }

Taking an open-weight model (or an API fine-tuning endpoint) and training it further on your own examples to change its style, format or domain behaviour.

**Why it matters:** Makes a general model behave your way: consistent format, your tone, your domain's conventions, often with a smaller and cheaper model.

### Full fine-tuning { #full-fine-tuning }

Update all the weights.

**Why it matters:** Highest quality ceiling but needs the most GPU memory and risks forgetting general skills.

### Parameter-Efficient Fine-Tuning (PEFT) { #parameter-efficient-fine-tuning }

A family of methods that freeze the model and train only a small set of extra parameters.

**Why it matters:** Fine-tune a big model on a single GPU and store the result as a tiny file.

<small>*Index aliases:* PEFT</small>

### Low-Rank Adaptation (LoRA) ★ { #low-rank-adaptation }

The most popular PEFT method: learn small low-rank matrices that are added to the attention and feed-forward weights.

**Why it matters:** Trains ~1% of the parameters for most of the benefit; the adapter is a small file (tens to a couple of hundred MB) you can swap in and out.

<small>*Index aliases:* LoRA</small>

### QLoRA { #qlora }

LoRA on top of a 4-bit quantized base model.

**Why it matters:** Lets you fine-tune a 65–70B model on a single 48 GB GPU, or a 7–13B model on a consumer card.

<small>*Index aliases:* QLoRA (4-bit LoRA)</small>

### Adapters, prompt tuning, prefix tuning { #adapters-prompt-tuning-prefix-tuning }

Other PEFT flavours: small bottleneck layers inserted in the network, or learned soft-prompt vectors prepended to the input.

**Why it matters:** Same goal as LoRA (cheap adaptation), different mechanics; LoRA won on simplicity.

<small>*Index aliases:* Prefix tuning / prompt tuning</small>

### Rank (r) and alpha { #rank-r-and-alpha }

LoRA hyperparameters controlling adapter size and how strongly it is scaled.

**Why it matters:** Higher rank = more capacity and memory; typical values are 8–64.

<small>*Index aliases:* Rank / alpha (LoRA)</small>

### Merging an adapter { #merging-an-adapter }

Adding the trained LoRA matrices into the base weights to produce a single standalone model.

**Why it matters:** Removes the small inference overhead of a separate adapter and gives you one file to deploy.

<small>*Index aliases:* Adapter (LoRA)</small>

### Task / classification head { #task-classification-head }

A small new output layer placed on top of the model for a specific task (e.g. spam / not spam), replacing the LM head. (Raschka chapter 6.)

**Why it matters:** The simplest fine-tune: reuse everything the model knows, train only the last layer for your labels.

<small>*Index aliases:* Classification head</small>

### Catastrophic forgetting { #catastrophic-forgetting }

Fine-tuning on a narrow dataset erodes the general abilities the model had before.

**Why it matters:** Why you keep the learning rate low, mix in general data, and prefer LoRA: to add a skill without losing the others.

### Domain adaptation { #domain-adaptation }

Specialising a general model to a field: legal, medical, your codebase, your product's tone.

**Why it matters:** Makes the model fluent in your world's vocabulary and conventions.

### Instruction dataset { #instruction-dataset }

The prompt → completion pairs you fine-tune on. Quality matters more than quantity; hundreds to a few thousand good examples often suffice.

**Why it matters:** Your main lever: the model will copy whatever these examples do, including their mistakes.

### Dataset formats { #dataset-formats }

*Also known as:* Alpaca, ShareGPT, messages / JSONL

Standard JSON layouts for instruction data: Alpaca (instruction / input / output), ShareGPT (conversations), or OpenAI-style messages lists.

**Why it matters:** The format most fine-tuning tools expect; converting your data into one of these is step one.

<small>*Index aliases:* Alpaca / ShareGPT format</small>

### Open weights vs open source { #open-weights-vs-open-source }

Open weights means you can download and fine-tune the parameters (Llama, Mistral, Qwen, Gemma). True open source also releases the data and training code (OLMo).

**Why it matters:** Open weights are what let you fine-tune and self-host; "open source" is usually a looser claim.

<small>*Index aliases:* Qwen, Open weights, Open source (models)</small>

### API fine-tuning { #api-fine-tuning }

Fine-tuning a closed model through the provider's API: you upload examples, they train and host the result.

**Why it matters:** Fine-tuning without GPUs or ops; the trade-off is lock-in and less control.

### Hugging Face PEFT / TRL / Unsloth / Axolotl { #hugging-face-peft-trl-unsloth-axolotl }

The standard libraries and tools for running LoRA, SFT and DPO on open models.

**Why it matters:** The tools most fine-tuning tutorials use; Unsloth is the fast, memory-light one for single GPUs.

<small>*Index aliases:* Unsloth / Axolotl, TRL</small>

### Evaluation set { #evaluation-set }

A held-out slice of your own examples used to check the fine-tune actually improved things.

**Why it matters:** The only way to know your fine-tune helped and did not just overfit your examples.
