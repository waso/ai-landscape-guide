# The Stanford CME295 slide, decoded

The 35 acronyms from the “…but don’t worry!” slide of Stanford CME295 *Transformers & LLMs* (Autumn 2026, Lecture 1), each explained in plain words, grouped exactly as on the slide. Two groups describe what is *inside* the model, two describe how its *weights are changed* after pre-training, two describe how it is *measured*.

## Attention techniques

*How a token looks at the other tokens. All six are variations on the same mechanism; the newer ones exist to cut memory and cost, not to change what attention does.*

<small>Inside the model (field guide section 6, Map 5)</small>

### MHA — Multi-Head Attention <a id="mha"></a>
Attention is the part of a Transformer that lets each word look at the other words in the text and decide which ones matter for understanding it. When the model reads the word "it", attention is how it works out that "it" refers to "the cat" ten words earlier. "Multi-head" means the model does this looking-around several times in parallel, and each parallel copy, called a head, is free to look for a different kind of relationship. One head may track grammar, another the topic, another which words are close together. The results of all heads are glued back together before the next layer.

This is the original design from the 2017 "Attention Is All You Need" paper, and it is the baseline that every other technique in this box is compared against. GPT-2 small has 12 heads per layer; Llama-3-8B has 32.

**Good to know:** The catch: while the model generates text, it keeps a memory of every earlier token for every head (the KV cache). With many heads and long texts that memory becomes the thing that limits how many users fit on one GPU, which is exactly what GQA, MQA and MLA were invented to fix. — [in the glossary](../glossary/06-the-transformer-architecture.md#multi-head-attention)

### GQA — Grouped-Query Attention <a id="gqa"></a>
The memory problem of multi-head attention comes from every head keeping its own private copy of the "keys and values" of all earlier tokens. GQA keeps all the heads that ask questions (the queries) but makes several of them share one copy of the keys and values, like a group of readers sharing one copy of a book instead of each buying their own. The heads still look for different things; they just read from a shared memory.

The saving is large and the quality loss is almost nil. In Llama-3-8B, 32 query heads share 8 sets of keys and values, so the memory per token drops four times. That is what allows longer contexts and more simultaneous users on the same hardware.

**Good to know:** Introduced by Google researchers in 2023. It sits exactly between the original design (every head has its own memory) and MQA below (everyone shares a single memory). Nearly every model released since 2024 uses it: Llama 2 70B, Llama 3, Mistral, Qwen, Gemma. — [in the glossary](../glossary/06-the-transformer-architecture.md#multi-query-grouped-query-attention)

### MQA — Multi-Query Attention <a id="mqa"></a>
The extreme version of sharing: all the query heads share one single set of keys and values. The per-token memory shrinks by the number of heads, 32 times for a 32-head model, so generating text becomes very fast and cheap.

The price is quality. Every head now reads from the same, less rich memory, so the model loses some of its ability to track several relationships at once, and training was found to be less stable. That is why GQA, which shares among groups of heads rather than among all of them, became the standard compromise.

**Good to know:** Proposed by Noam Shazeer in 2019 with the memorable title "One Write-Head is All You Need". Used in Google's PaLM, in Falcon-7B and in the StarCoder code models. — [in the glossary](../glossary/06-the-transformer-architecture.md#multi-query-grouped-query-attention)

### MLA — Multi-head Latent Attention <a id="mla"></a>
DeepSeek's answer to the same memory problem, taken from a different angle. Instead of making heads share their memory, MLA compresses the memory itself: for every token it stores a small, squeezed summary of the keys and values, like a zip file, and unpacks it on the fly whenever attention needs it. The squeezing is learned during training, so very little information is lost.

Because the stored summary is much smaller than the original keys and values, the saving is bigger than with GQA, and DeepSeek reports no loss of quality, sometimes a small gain. This is one of the main reasons DeepSeek's models can serve long conversations so cheaply.

**Good to know:** Introduced with DeepSeek-V2 in 2024 and kept in DeepSeek-V3 and R1. Compared with its predecessor model, DeepSeek reported a memory for past tokens about 93% smaller. One subtlety: the position information (RoPE, see next box) does not survive the squeezing, so a small separate piece of each key carries it. — [in the glossary](../glossary/06-the-transformer-architecture.md#multi-head-latent-attention)

### SWA — Sliding-Window Attention <a id="swa"></a>
Normally every token may look at every earlier token, so the cost of attention grows with the square of the text length. Sliding-window attention lets each token look only at the last few thousand tokens, like reading with a window that slides along the page. Cost and memory then stop growing with the length of the text, and the memory of past tokens can be a fixed-size rolling buffer.

Information from further back is not lost entirely: each layer passes on what it saw, so a token in layer ten indirectly knows about things far outside its own window. The trade-off is weaker recall of very distant details, which is why modern models mix windowed layers with a few normal "see everything" layers. Gemma 2 alternates the two one-to-one; Gemma 3 uses five windowed layers for every full one; OpenAI's gpt-oss alternates them too.

**Good to know:** The idea comes from Longformer (2020) and was popularised by the original Mistral 7B, which used a window of about 4,000 tokens. A related trick called attention sinks keeps the first few tokens of the text permanently visible, because the model habitually parks its spare attention on them. — [in the glossary](../glossary/06-the-transformer-architecture.md#sliding-window-attention-attention-sinks)

### AttnRes — Attention Residuals <a id="attnres"></a>
To understand this one you need the "residual stream": in a Transformer, every layer adds its output to a running total that is passed upward, so by the time the last layer runs it sees the sum of everything the earlier layers produced, each counted with equal weight. That fixed "add everything equally" rule has been unchanged since 2015.

AttnRes replaces it with a choice. Each layer learns how much to take from each earlier layer, using the same attention idea but applied across the depth of the network rather than across the words of the text. A later layer can lean heavily on layer three and ignore layer seven if that works better.

**Good to know:** Published by Moonshot AI (the Kimi lab) in March 2026. The gain is small but consistent across benchmarks, for roughly 4% extra training cost and 2% extra inference cost. Its main lesson for a learner: even the basic plumbing of the Transformer is still being redesigned in 2026. — [in the glossary](../glossary/06-the-transformer-architecture.md#attention-residuals)

## Architecture optimizations

*Changes to the other parts of the Transformer block: how experts are routed, how position is encoded, how numbers are kept in a healthy range, and what the feed-forward layer looks like.*

<small>Inside the model (field guide sections 4 and 6, Map 5)</small>

### MoE — Mixture of Experts <a id="moe"></a>
Each Transformer block contains a feed-forward network, the part that holds most of the model's stored knowledge. In a normal ("dense") model every token goes through the same one. In a Mixture of Experts, that single network is replaced by many smaller ones, the experts, plus a tiny router that sends each token to only a few of them. Think of a hospital reception sending each patient to two relevant specialists rather than to every doctor in the building.

The result is a model that holds far more knowledge in total while doing only the work of a much smaller model for each token. The names tell you both numbers: Qwen3-235B-A22B has 235 billion parameters in total but uses only 22 billion per token; DeepSeek-V3 has 671 billion total and 37 billion active; Mixtral 8x7B picks 2 of its 8 experts. Most frontier models since 2025 are built this way.

**Good to know:** The costs: all the experts must sit in memory even though only a few run at a time, the router has to be trained so that work is spread evenly instead of everyone crowding the same two experts, and spreading experts across many GPUs is an engineering job of its own. — [in the glossary](../glossary/06-the-transformer-architecture.md#mixture-of-experts)

### RoPE — Rotary Positional Embedding <a id="rope"></a>
Attention on its own is blind to word order: "dog bites man" and "man bites dog" look identical to it. Position has to be injected somehow. RoPE does it by treating a token's position as an angle and rotating its query and key vectors by that angle, like turning the hands of a clock. When two rotated vectors are compared, only the difference between their angles matters, so attention naturally sees how far apart two words are rather than where exactly each one sits.

This has no learned parameters and works well, which is why nearly every current open model uses it: Llama, Mistral, Qwen, Gemma, DeepSeek. It is applied inside every attention layer, not once at the start.

**Good to know:** Introduced in 2021. One thing to know: a model trained on, say, 8,000-token texts does not automatically cope with 100,000-token texts; RoPE on its own extrapolates badly. Long contexts come from "stretching" tricks with names like position interpolation and YaRN, plus a short extra round of training. Llama 3 also turned up RoPE's internal base frequency, from 10,000 to 500,000, to make long contexts work. — [in the glossary](../glossary/06-the-transformer-architecture.md#rotary-positional-embedding)

### ALiBi — Attention with Linear Biases <a id="alibi"></a>
A different answer to the word-order problem. Instead of encoding positions at all, ALiBi simply makes attention pay less to tokens that are further away by subtracting a penalty that grows with distance: nearby words matter a lot, far-away words a little. Each head uses a different steepness, so some heads stay very local and others look far.

Its selling point was "train short, test long": a model trained on short texts keeps working on much longer ones, because the rule is the same at every distance. It is also trivially cheap, with no extra parameters.

**Good to know:** Proposed in 2021 and used by the BLOOM and MPT models. In the end RoPE won the popularity contest: it scored better at large scale and fitted the fast attention software (FlashAttention) more easily. You will still meet ALiBi in papers and in older open models. — [in the glossary](../glossary/06-the-transformer-architecture.md#alibi)

### LN — Layer Normalization <a id="ln"></a>
Deep networks break when the numbers flowing through them drift to huge or tiny values. LayerNorm fixes this by rescaling each token's vector so that its values have a standard spread, like converting every exam to a 0-to-100 scale before comparing them, and then letting the model stretch and shift the result with two learned knobs.

In a Transformer it sits just before each attention and each feed-forward sub-layer. Placing it before rather than after (the "pre-norm" layout, adopted from GPT-2 onwards) is what made 100-layer models trainable without constant crashes.

**Good to know:** Invented in 2016. Most current models use a lighter variant called RMSNorm (2019), which skips one of the steps and runs a bit faster with the same effect; Llama, Qwen, DeepSeek and Gemma all use it. When a slide says LN, RMSNorm or "norm layers", it is this idea. — [in the glossary](../glossary/04-neural-network-foundations.md#normalization)

### QKNorm — Query-Key Normalization <a id="qknorm"></a>
A targeted version of the same idea, applied at one specific spot: the query and key vectors are normalised right before they are compared inside attention. Why there? As models grow, those comparison scores can grow enormous, the attention softmax turns into a rigid "look at one token only", and training suddenly diverges with a loss spike.

With QK-Norm the scores stay in a bounded range, the spikes disappear, and the model can be trained with a higher learning rate, which means faster and cheaper training.

**Good to know:** First proposed in 2020, it became standard after Google's 22-billion-parameter vision Transformer (2023) used it to cure exactly this instability. Used in Gemma 3, OLMo 2 and Qwen3, and in many models released since. It works alongside RoPE: normalise first, then rotate. — [in the glossary](../glossary/06-the-transformer-architecture.md#qk-norm)

### SwiGLU — Swish-Gated Linear Unit <a id="swiglu"></a>
The feed-forward network inside each block is where most of the parameters and most of the stored knowledge live. The classic version is "transform, then squash": multiply by a matrix, apply a simple activation function, multiply by another matrix. SwiGLU is a better-performing design: it runs two transforms in parallel and uses one of them as a gate that decides how much of the other passes through, like a valve on each signal line.

In practice it trains to a lower loss than the plain version for the same compute, which is why PaLM, Llama, Mistral, Qwen and DeepSeek all use it. The gating needs a third matrix, half again as many weights at the same width, so models make the hidden layer narrower to compensate.

**Good to know:** Proposed by Noam Shazeer in 2020 (the same person behind MQA). Gemma uses a cousin called GeGLU with a different activation; GPT-2 uses the old ungated design with a GELU activation, which is what Raschka's book implements. — [in the glossary](../glossary/06-the-transformer-architecture.md#feed-forward-in-a-block)

## Model tuning

*Changing the weights of an existing model with ordinary supervised training. SFT and DPO are done by labs and by you; PEFT, LoRA and QLoRA are the techniques that make it affordable on one GPU.*

<small>Stages 4 and 5 of Map 2 (field guide sections 8 and 9)</small>

### SFT — Supervised Fine-Tuning <a id="sft"></a>
Show the model many examples of a prompt together with the ideal answer, and train it to reproduce those answers. A freshly pre-trained model only knows how to continue text; SFT is how it learns to follow instructions, answer a question instead of continuing it, use the chat format and stop when it is done. It is also how you teach a model your own format, tone or domain conventions.

Under the hood it is the same training loop as pre-training, just on a much smaller and hand-picked dataset, and usually with the loss computed only on the answer part, not on the prompt. Because the model copies what it sees, the quality of the examples matters far more than their number: a few thousand good ones are often enough, and bad examples are copied just as faithfully.

**Good to know:** It was step one of the InstructGPT recipe (2022) that led to ChatGPT. Famous datasets include Alpaca (52,000 examples generated by a stronger model) and ShareGPT (real conversations). It is also the mechanism of distillation: fine-tune a small model on a big model's answers. Raschka's chapter 7 is an SFT run. — [in the glossary](../glossary/08-post-training-alignment.md#supervised-fine-tuning)

### PEFT — Parameter-Efficient Fine-Tuning <a id="peft"></a>
Fine-tuning all 8 billion weights of a model needs a lot of GPU memory, because for every weight the optimizer also stores extra bookkeeping numbers, and it produces a whole new 16-gigabyte copy of the model. PEFT is the family of methods that freeze the original model and train only a small add-on, often under 1% of the size, like patching a program instead of recompiling it.

What you gain: far less memory, faster training, the original stays intact, and you can keep dozens of small task-specific add-ons next to one base model and swap them in and out. Serving systems can even host hundreds of such add-ons at once.

**Good to know:** Members of the family: adapters (small extra layers inserted in each block, 2019), prompt tuning (learned vectors stuck in front of the input) and prefix tuning (learned vectors stuck in front of every layer), both from 2021, and LoRA (2021), which won. The Hugging Face library that implements them is literally called peft. — [in the glossary](../glossary/09-adapting-a-model-to-your-task.md#parameter-efficient-fine-tuning)

### LoRA — Low-Rank Adaptation <a id="lora"></a>
The most popular PEFT method. Rather than changing a big weight matrix directly, LoRA learns a thin "patch" made of two small matrices whose product is added on top of the original. The patch has a tiny fraction of the numbers in the original matrix, yet it captures most of what a full fine-tune would have learned, because the change needed to adapt a model turns out to be simple.

The patch starts at zero, so training begins exactly from the base model and moves away from it gradually. It is usually applied to the attention matrices and often to the feed-forward ones too. The main knob is the rank, which sets the patch size; values between 8 and 64 are typical. At the end you can either keep the patch as a separate small file, or merge it into the base weights so inference costs nothing extra.

**Good to know:** Published by Microsoft researchers in 2021. For Llama-3-8B with a typical setup, the patch is about 42 million trainable numbers, roughly half a percent of the model, and an adapter file of under 100 megabytes. — [in the glossary](../glossary/09-adapting-a-model-to-your-task.md#low-rank-adaptation)

### QLoRA — Quantized LoRA <a id="qlora"></a>
LoRA on top of a compressed base model. The big frozen model is stored in 4-bit numbers, a quarter of the usual memory, while the small LoRA patch is trained in normal precision. When the model runs, the compressed weights are expanded on the fly, so the maths is the same; only the storage is smaller.

This is what lets a 65-to-70-billion-parameter model be fine-tuned on a single 48-gigabyte GPU, and a 7-to-13-billion model on an ordinary gaming card. The authors showed the results match full-precision fine-tuning almost exactly.

**Good to know:** Published in 2023. Three tricks make it work: a 4-bit number format designed for the typical shape of weight values, compressing the compression tables themselves, and shuffling optimizer memory to the CPU when there is a spike. It is the reason "fine-tune it yourself" became realistic for individuals. — [in the glossary](../glossary/09-adapting-a-model-to-your-task.md#qlora)

### DPO — Direct Preference Optimization <a id="dpo"></a>
A way to teach a model from preferences, pairs of answers where one is marked better than the other, without the full reinforcement-learning machinery of RLHF. DPO turns each pair into a simple training objective: raise the probability of the preferred answer, lower the probability of the rejected one, while staying close to the starting model so it does not drift.

You get most of the benefit of RLHF with a fraction of the complexity: no reward model to train, no sampling loop, only two models in memory instead of four. That is why open-model teams use it so widely; Zephyr, Tülu and Meta's Llama 3 pipeline all use it.

**Good to know:** Published by Stanford researchers in 2023. Its clever bit is mathematical: the authors showed that the RLHF objective has a closed-form answer, so the reward model can be eliminated. Note that the slide puts DPO under "model tuning", not under RL, precisely because no reinforcement-learning loop runs. Variants you may hear of: IPO, KTO, ORPO, SimPO. — [in the glossary](../glossary/08-post-training-alignment.md#direct-preference-optimization)

## Reinforcement Learning

*Training by trial and reward instead of by example: the model produces answers, something scores them, and the weights move toward higher scores. This is how models learn to be preferred by people and, more recently, how they learn to reason.*

<small>Stage 4 of Map 2 (field guide section 8)</small>

### RLHF — Reinforcement Learning from Human Feedback <a id="rlhf"></a>
The recipe behind ChatGPT. It has three stages. First, people compare pairs of model answers and say which is better. Second, a separate "judge" model, the reward model, is trained to predict those human preferences. Third, the language model practises on thousands of prompts: it writes answers, the judge scores them, and the weights are nudged toward answers that score higher, while a leash keeps the model close to its starting point so it does not drift into nonsense that happens to please the judge.

Examples alone (SFT) can teach a model the format of being helpful; RLHF teaches it what people actually prefer, which is how answers became more helpful, more polite and more careful. It is also where a model's "personality" is largely shaped.

**Good to know:** The ideas date from 2017 and were applied to language models from 2019; the InstructGPT paper (2022) is the canonical description. The expensive part is the practice stage, which needs four models in memory at once, and that cost is what DPO and GRPO were designed to cut. — [in the glossary](../glossary/08-post-training-alignment.md#reinforcement-learning-from-human-feedback)

### RLVR — Reinforcement Learning with Verifiable Rewards <a id="rlvr"></a>
The same practice loop as RLHF, but with the human-trained judge replaced by an automatic check: did the maths answer match, do the unit tests pass, is the output in the required format. Because a unit test cannot be flattered or fooled, the model can be pushed much further than human preferences allow.

This is the main ingredient that produced the current reasoning models. When only correct answers are rewarded, the model discovers on its own that writing out long chains of reasoning before answering leads to more correct answers, and that behaviour grows during training. The limit is obvious: it only works where answers can be verified, so maths and code lead the way and the research question is how to extend it to softer tasks.

**Good to know:** The name was coined by the Allen Institute's Tülu 3 project in late 2024; DeepSeek-R1 (January 2025) made it famous, training with simple rule-based rewards for correctness and format, using the GRPO algorithm below. — [in the glossary](../glossary/08-post-training-alignment.md#rl-with-verifiable-rewards)

### RM — Reward Model <a id="rm"></a>
The trained judge used in RLHF. It takes a prompt and a candidate answer and outputs a single number: how good this answer is. It is built by taking a copy of the language model, replacing its text-producing head with a scoring head, and training it on the human comparison data. Once it exists, the practice loop can run millions of times without a human in the room.

Its weaknesses become the main model's weaknesses. If the judge has learned that long, confident answers tend to win votes, the trained model becomes long and confident whether or not it is right; this is called reward hacking, and it is why RLHF keeps a leash on the model and why RLVR replaces the judge with a verifier wherever it can.

**Good to know:** Two flavours you will hear about: an outcome reward model scores only the final answer, a process reward model scores each step of the reasoning. Using a general language model as the judge ("LLM-as-a-judge", in the metrics box) is the same idea without special training. — [in the glossary](../glossary/08-post-training-alignment.md#reward-model)

### PPO — Proximal Policy Optimization <a id="ppo"></a>
The reinforcement-learning algorithm classically used inside RLHF. Its one big idea is caution. After seeing how the judge scored a batch of answers, it moves the model a little in the right direction, but it clips any update that would change the model's behaviour too much in one step. Plain reinforcement learning without that clipping tends to spiral out of control; PPO stays stable.

To decide how good each situation is, PPO trains an extra helper model, the "value" network, alongside the main one. Together with the reference model and the reward model, that makes four large models in memory during training, which is PPO's main drawback in the LLM setting.

**Good to know:** Published by OpenAI in 2017 for games and robotics, and reused for language models from 2019. In RLHF each generated token is treated as one "action", and the score arrives only when the answer is complete. — [in the glossary](../glossary/08-post-training-alignment.md#proximal-policy-optimization)

### GRPO — Group Relative Policy Optimization <a id="grpo"></a>
A cheaper cousin of PPO from DeepSeek. For each question the model writes a group of answers, say sixteen. Each answer is scored, and its training signal is simply how much better or worse it did than its siblings in the group: above the group average means "do more of this", below means "do less". Because answers are judged relative to each other, PPO's extra value network is not needed at all.

That halves the memory and simplifies the whole setup, and it works with any kind of score: a reward model or an automatic check. It is the algorithm that trained DeepSeek-R1's reasoning and it spread through the open-source world within weeks.

**Good to know:** Published in DeepSeekMath in February 2024, a year before R1 made it famous. Known weaknesses: a bias toward longer answers, fixed in later variants, and instability on very long answers and on Mixture-of-Experts models, which led to GSPO. — [in the glossary](../glossary/08-post-training-alignment.md#group-relative-policy-optimization)

### GSPO — Group Sequence Policy Optimization <a id="gspo"></a>
Qwen's 2025 refinement of GRPO. GRPO judges and clips the update token by token. On very long answers those thousands of tiny per-token judgements add up a lot of noise, and on Mixture-of-Experts models, where slightly different experts may fire from one version of the model to the next, training could collapse altogether. GSPO judges and clips the whole answer as one unit instead.

The benefit is stable, efficient training at large scale with less engineering trickery: Qwen's team had needed a workaround called "routing replay" to keep GRPO working on their MoE models, and GSPO removed the need for it.

**Good to know:** Published by the Qwen team in July 2025 and used to train the Qwen3 Instruct, Coder and Thinking models. Implementations exist in the common open-source RL libraries (TRL, verl). — [in the glossary](../glossary/08-post-training-alignment.md#group-sequence-policy-optimization)

## Benchmarks

*Fixed exams used to compare models. Each is a dataset plus a scoring rule; the five on the slide cover maths, broad knowledge, expert science, real software engineering and the current "hardest exam".*

<small>Cross-cutting (field guide section 12)</small>

### AIME — American Invitational Mathematics Examination <a id="aime"></a>
A real competition exam for strong US high-school students: 15 problems per paper, each with a whole-number answer between 0 and 999, no multiple choice to guess from, about three hours for a human. It became the favourite test for reasoning models because the answers are unambiguous and the problems need several steps of real mathematics, not recall.

The numbers tell the story of 2024–25. GPT-4-class models solved roughly one problem in ten on the 2024 paper. OpenAI's o1 and DeepSeek-R1 solved about four in five. Within another year, reasoning models were above 90%. The 2025 paper is popular precisely because it appeared after most models' training data was collected, so they cannot have memorised it.

**Good to know:** Scores are usually reported as single-attempt accuracy, often averaged over many tries; you will also see "cons@64", meaning the model answers 64 times and the most common answer counts. With only 30 problems a year, small score differences are noise. — [in the glossary](../glossary/12-evaluation-safety-interpretability.md#gsm8k-math-aime)

### HLE — Humanity's Last Exam <a id="hle"></a>
A deliberately brutal exam built in early 2025 because the older benchmarks had become too easy. About 2,500 questions were written by subject experts across more than a hundred fields, from maths and physics to law, linguistics and classics, and only questions that the best models at the time got wrong were kept. Roughly one in seven needs an image as well as text.

The name is the point: it is meant to be the last academic-style benchmark worth building. When models pass it, exams of this kind stop telling us anything. At launch the best models scored in the single digits; with reasoning and web tools, scores climbed into the tens of percent during 2025 and 2026.

**Good to know:** Created by the Center for AI Safety together with Scale AI, with nearly a thousand contributors. Besides accuracy it reports how well calibrated a model is, so a model that is confidently wrong is penalised. — [in the glossary](../glossary/12-evaluation-safety-interpretability.md#arc-agi-humanity-s-last-exam)

### MMLU — Massive Multitask Language Understanding <a id="mmlu"></a>
The classic general-knowledge test: around 14,000 four-option multiple-choice questions across 57 subjects, from elementary maths to law, medicine and history. From 2021 to 2024 it was the headline number in nearly every model announcement, usually run "5-shot", with five worked examples shown first.

Top models now score around 90%, so it mostly tells you that a model is not bad rather than how good it is. A few percent of its questions are known to be wrong, and many of them have leaked into training data. For separating strong models, the harder MMLU-Pro (2024) took over: 12,000 questions, ten options instead of four, more reasoning required, which knocks 16 to 33 points off the scores.

**Good to know:** Published in 2020 by Dan Hendrycks and colleagues. When a 2026 lecture mentions MMLU, it is usually as the example of a benchmark that got saturated. — [in the glossary](../glossary/12-evaluation-safety-interpretability.md#mmlu-mmlu-pro)

### SWE-bench — Software Engineering Benchmark <a id="swe-bench"></a>
The benchmark for coding agents, and the one most relevant to your work. Take real bug reports and feature requests from popular open-source Python projects (Django, scikit-learn, sympy and others), give the model the repository, and check whether its patch makes the project's own tests pass while not breaking the ones that passed before. It measures finishing a real engineering job, not writing a function from a description.

Scores went from almost nothing in 2023 to well over half the tasks in 2025, the clearest single sign of the agentic-coding shift. The number labs quote is SWE-bench Verified, a subset of 500 tasks that human reviewers checked are actually solvable; the full set has about 2,300 tasks, and a cheap 300-task "Lite" version exists.

**Good to know:** Published by Princeton researchers in 2023; the Verified subset was curated by OpenAI in 2024. One caveat to keep in mind: the result depends as much on the agent scaffolding around the model as on the model itself. — [in the glossary](../glossary/12-evaluation-safety-interpretability.md#humaneval-swe-bench)

### GPQA — Graduate-Level Google-Proof Q&A <a id="gpqa"></a>
Hard science questions in biology, physics and chemistry, written by people with PhDs in those fields, designed so that a smart person outside the field, given unlimited time and Google, still gets only about a third right. Experts in the same field get about two thirds. It tests deep expertise rather than memorised trivia, hence "Google-proof".

The number usually quoted is GPQA Diamond, the subset of 198 questions that experts answered correctly and non-experts mostly missed. GPT-4 scored around 39% when the test came out in 2023; reasoning models passed 80% in 2025, so it is approaching the point where it stops being useful.

**Good to know:** Four options per question means pure guessing already gives 25%, worth remembering when two models are a couple of points apart. — [in the glossary](../glossary/12-evaluation-safety-interpretability.md#gpqa)

## Metrics

*The numbers you compute. A benchmark is a dataset; a metric is how you score it, or how you measure something that is not a benchmark at all, like speed or how far a model has drifted.*

<small>Spread across the lifecycle: pre-training (PPL), post-training (KL), inference (TTFT, TPOT), applications (LaaJ), evaluation (Pass@k, Elo)</small>

### PPL — Perplexity <a id="ppl"></a>
How surprised a language model is by a piece of text. A perplexity of 20 means that, on average, the model was as uncertain about each next token as if it were choosing among 20 equally likely options. Lower is better. It is computed directly from the training loss, which is why it is the number labs watch fall during pre-training and the standard way to compare models on raw text.

It measures prediction, not helpfulness: a model can have excellent perplexity and still be a poor assistant. It also depends on the tokenizer and on the text used, so you can only compare models that share a tokenizer, on the same data.

**Good to know:** For scale: GPT-2 small scores about 37 on a standard Wikipedia test set, the largest GPT-2 about 17. Raschka's chapter 5 prints it during training, and it is the quick check people run after compressing a model to 4 bits: if perplexity barely moved, the compression did little harm. — [in the glossary](../glossary/07-pre-training.md#perplexity)

### LaaJ — LLM-as-a-Judge <a id="laaj"></a>
Using a strong language model to grade another model's answers, either by giving a score against a rubric or by saying which of two answers is better. It is far cheaper than human raters and agrees with them most of the time, so teams run it like a test suite on every change to a prompt or a model.

The judge has known biases: it prefers longer answers, it prefers whichever answer it sees first, it prefers its own writing style, and it is weak at checking maths. Good setups counter these by swapping the order of the two answers, giving the judge a reference solution, and using strict rubrics.

**Good to know:** The approach was formalised in 2023, when researchers showed that GPT-4 as a judge agreed with human preferences more than 80% of the time, about as often as humans agree with each other. The same idea doubles as a training signal (the reward in RLAIF) and as a filter for generated training data. Raschka's chapter 7 uses a local Llama model as the judge. — [in the glossary](../glossary/11-building-applications.md#llm-as-a-judge)

### KL — Kullback–Leibler divergence <a id="kl"></a>
A number that says how different two probability distributions are: zero when they are identical, growing as they diverge. In LLM training it is mostly used as a leash. During RLHF or GRPO the model is penalised for moving its token probabilities too far from the starting model, which stops it from degenerating into gibberish that happens to score well with the judge. The strength of that leash is a tuning knob, and DPO has the same knob built in.

It also appears in distillation, where a small student model is trained to match the full probability distribution of a big teacher rather than just copying its words, and in the maths behind the training loss itself: minimising cross-entropy is the same as minimising the KL divergence to the real text.

**Good to know:** Named after two statisticians from the 1950s. Note that it is one-directional: the divergence from A to B is not the same as from B to A, which is why papers are careful to say which way round they measure it. — [in the glossary](../glossary/08-post-training-alignment.md#kl-penalty-reference-model)

### Pass@k — Pass at k <a id="pass-k"></a>
The chance that at least one of k attempts is correct. Pass@1 is what a user experiences on a single try. Pass@10 or pass@100 shows what the model can do if you let it try many times and pick the attempt that works, which is realistic for code (run the tests) and for anything with an automatic checker.

The gap between the two is informative. A big gap between pass@1 and pass@100 means the capability is in there but unreliable; reinforcement learning with verifiable rewards often works by closing that gap, pulling single-try success up toward what many tries could already achieve.

**Good to know:** Introduced with OpenAI's Codex in 2021 together with a careful way of estimating it from many samples. It is standard on coding benchmarks (HumanEval, LiveCodeBench) and maths. Do not confuse it with majority voting, where the most common answer is chosen without any checker. — [in the glossary](../glossary/12-evaluation-safety-interpretability.md#pass-k)

### Elo — Elo rating <a id="elo"></a>
A rating system borrowed from chess. On Chatbot Arena (now LMArena), people chat with two anonymous models side by side and vote for the better answer. Each vote moves the winner's rating up and the loser's down, more when the result was a surprise, and the ratings settle into a leaderboard. A 400-point gap means the higher-rated model is expected to win about ten times out of eleven.

It is the closest thing to "which model do people prefer", and it has the weaknesses of a popularity contest: longer and nicer-looking answers win votes, the prompts are skewed toward casual use, and votes can be gamed. The site added "style control", which corrects for length and formatting, and separate leaderboards for coding and hard prompts.

**Good to know:** Named after Arpad Elo, who designed it in the 1960s. LMArena stopped using the chess-style running update at the end of 2023 and now fits all votes together with a statistical model, but it still reports scores on the familiar Elo-like scale, with confidence intervals. — [in the glossary](../glossary/12-evaluation-safety-interpretability.md#chatbot-arena-lmarena-elo)

### TTFT — Time To First Token <a id="ttft"></a>
How long the user waits before the first word of the answer appears, the pause you feel after pressing Enter. It is made of three parts: time in the queue on a busy server, the time to process the whole prompt (the "prefill" phase), and the network. Prompt processing dominates: it grows with the length of the prompt, so pasting a long document or stuffing many retrieved passages into the context makes it longer. A 100,000-token prompt can take several seconds even on a top GPU.

Two things make it feel fast. Prompt caching reuses the already-processed part of a prompt that repeats between requests, such as a long system prompt or the same document, and can cut TTFT many times over. Streaming does not change TTFT but makes the rest of the answer appear as it is generated instead of all at once.

**Good to know:** Product teams typically aim for well under a second for chat. If you benchmark a model API, this is one of the two numbers to record; the other is TPOT. — [in the glossary](../glossary/10-inference-serving.md#latency-ttft-tpot-tokens-sec)

### TPOT — Time Per Output Token <a id="tpot"></a>
Once the answer has started, how long each additional token takes; turn it upside down and you get the familiar tokens-per-second. Total waiting time is TTFT plus TPOT times the number of tokens in the answer, which is why long answers from a reasoning model feel slow even when the first token came fast.

What sets it is surprising: for each new token the model has to read all of its weights from GPU memory, and that reading, not the arithmetic, is the bottleneck. An 8-billion-parameter model in normal precision is 16 gigabytes; an H100 can read about 3,350 gigabytes per second; so one token can never take less than about 5 milliseconds, roughly 200 tokens per second for a single user. Compress the weights to 4 bits and the ceiling rises four times, which is why quantization speeds up generation. Speculative decoding, where a small model drafts several tokens and the big one checks them in one read, is the other main trick.

**Good to know:** Serving many users at once lets the server share one read of the weights across all of them, which is great for throughput but can make each individual user's TPOT a little worse. Typical values for hosted models are 10 to 50 milliseconds per token, that is 20 to 100 tokens per second. — [in the glossary](../glossary/10-inference-serving.md#latency-ttft-tpot-tokens-sec)
