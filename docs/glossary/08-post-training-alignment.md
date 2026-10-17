# 8. Post-training & alignment

*Stage 4: turning a base model into an assistant*

Done by the lab after pre-training, historically at a small fraction of the cost (though for the newest reasoning models the RL phase is growing toward pre-training scale). Supervised examples teach the format, then reinforcement learning shapes behaviour. Confusingly, people also call this "fine-tuning" or "alignment".

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Post-training { #post-training }

Everything the lab does after pre-training to make the model useful and safe: SFT, preference optimization, reinforcement learning.

**Why it matters:** Turns a text-completer into an assistant. Most of what you feel as the model's "personality" was shaped here.

### Fine-tuning (general meaning) { #fine-tuning-general-meaning }

Continuing to train a pre-trained model on a smaller, targeted dataset. Labs do it (post-training) and you can do it (section 9).

**Why it matters:** Same mechanics as pre-training, far less data. The word means two different stages depending on who is speaking.

### Supervised Fine-Tuning ★ { #supervised-fine-tuning }

*Also known as:* SFT, instruction tuning

Train on curated prompt → ideal-answer pairs so the model learns to follow instructions and hold a conversation.

**Why it matters:** Teaches the model the format of being helpful: answer the question, use the chat template, stop when done.

### Instruct / chat model { #instruct-chat-model }

The model after post-training. What you actually talk to.

**Why it matters:** The "-Instruct" or "-Chat" suffix on a model name means it has been through this stage.

<small>*Index aliases:* Chat model, Instruct model</small>

### Alignment { #alignment }

Making the model's behaviour match human intentions and values; often summarised as helpful, harmless and honest (HHH).

**Why it matters:** Both a goal (the model behaves as intended) and the name of the RLHF / safety part of post-training.

<small>*Index aliases:* HHH (helpful, harmless, honest)</small>

### Reinforcement Learning from Human Feedback (RLHF) ★ { #reinforcement-learning-from-human-feedback }

Humans rank model outputs → train a reward model on those rankings → use RL (PPO) to push the model toward higher-reward answers.

**Why it matters:** Makes answers more helpful and polite than SFT alone, because it optimises for what people actually prefer. The technique behind ChatGPT.

<small>*Index aliases:* RLHF</small>

### Reward model (RM) { #reward-model }

A model trained to score how good an answer is, standing in for human judgement during reinforcement learning.

**Why it matters:** Lets RL run millions of times without a human in the loop: the reward model is the automated judge.

<small>*Index aliases:* RM, Reward model (RM)</small>

### Preference data { #preference-data }

*Also known as:* pairwise comparisons

"Answer A is better than answer B" data used to train reward models or directly in DPO.

**Why it matters:** Cheaper to collect than ideal answers: comparing two outputs is easier than writing a perfect one.

### Proximal Policy Optimization (PPO) { #proximal-policy-optimization }

The RL algorithm classically used in RLHF. Updates the policy in small clipped steps.

**Why it matters:** Keeps RL training stable: small steps mean the model cannot suddenly wander into nonsense.

<small>*Index aliases:* PPO</small>

### Direct Preference Optimization (DPO) { #direct-preference-optimization }

Trains directly on preference pairs with a simple classification-style loss, skipping the reward model and the RL loop.

**Why it matters:** Gets most of RLHF's benefit with a fraction of the complexity, which is why open-model teams love it.

<small>*Index aliases:* DPO</small>

### Group Relative Policy Optimization (GRPO) { #group-relative-policy-optimization }

A PPO variant that samples a group of answers to the same prompt and scores each relative to the group, with no separate value model. Used by DeepSeek-R1.

**Why it matters:** Cheaper and simpler than PPO, and it turned out to be the recipe for training reasoning models.

<small>*Index aliases:* GRPO, DeepSeek-R1</small>

### Group Sequence Policy Optimization (GSPO) { #group-sequence-policy-optimization }

The Qwen team's 2025 successor to GRPO: the importance ratio and clipping are computed per whole sequence instead of per token. Used to train the Qwen3 Instruct, Coder and Thinking models.

**Why it matters:** More stable RL training, especially for Mixture-of-Experts models, where token-level GRPO tends to collapse.

<small>*Index aliases:* GSPO</small>

### On-policy vs off-policy { #on-policy-vs-off-policy }

On-policy methods (PPO, GRPO) learn from answers the current model just generated; off-policy methods (DPO on a fixed dataset) learn from stored data.

**Why it matters:** On-policy is more expensive but keeps improving the model on its own mistakes; off-policy is cheap but can go stale.

### RLAIF / Constitutional AI { #rlaif-constitutional-ai }

Use an AI, guided by a written set of principles (a constitution), to produce the feedback instead of, or alongside, humans. Anthropic's approach.

**Why it matters:** Scales feedback far beyond what human raters can produce, and makes the rules explicit and inspectable.

<small>*Index aliases:* Constitutional AI, RLAIF</small>

### RL with Verifiable Rewards (RLVR) { #rl-with-verifiable-rewards }

Reinforcement learning where the reward is an automatic check: did the maths answer match, did the unit tests pass.

**Why it matters:** No reward model to fool: when the answer is checkable, RL can push the model far beyond human demonstrations. The key ingredient of reasoning models.

<small>*Index aliases:* RLVR</small>

### Outcome vs process reward model { #outcome-vs-process-reward-model }

*Also known as:* ORM, PRM

An ORM scores only the final answer; a PRM scores each step of the reasoning.

**Why it matters:** Step-level rewards give the model more precise feedback on where it went wrong, at a higher labelling cost.

<small>*Index aliases:* PRM / ORM</small>

### Reasoning / thinking model { #reasoning-thinking-model }

A model post-trained to produce a long chain of thought before answering (OpenAI o-series, DeepSeek-R1, Claude extended thinking, Gemini thinking).

**Why it matters:** Much more accurate on maths, code and multi-step problems, in exchange for more tokens and latency.

<small>*Index aliases:* o1 / o3, Extended thinking</small>

### Thinking budget / reasoning tokens { #thinking-budget-reasoning-tokens }

The number of tokens a reasoning model may spend thinking before it answers; often a setting you control. Reasoning tokens are usually billed as output.

**Why it matters:** Lets you trade cost and speed for accuracy per request.

<small>*Index aliases:* Reasoning tokens</small>

### Test-time compute / inference-time scaling { #test-time-compute-inference-time-scaling }

Spending more compute at answer time (longer thinking, multiple samples, search) to get better answers, instead of only training a bigger model.

**Why it matters:** The second scaling axis: the same model gets smarter if you let it think longer.

<small>*Index aliases:* Inference-time scaling</small>

### Agentic / multi-turn RL { #agentic-multi-turn-rl }

Reinforcement learning on whole tasks that involve many steps and tool calls, not single answers.

**Why it matters:** How models are trained to be good at long coding sessions and browsing, not only at one-shot replies.

### KL penalty / reference model { #kl-penalty-reference-model }

A term in the RL objective keeping the trained model close to the SFT model.

**Why it matters:** Stops the model from drifting into gibberish that happens to score well with the reward model.

<small>*Index aliases:* Reference model, KL divergence</small>

### Reward hacking { #reward-hacking }

The model finding ways to get high reward without actually being good: verbosity, confident tone, telling the grader what it wants.

**Why it matters:** Why RL needs careful rewards: optimise a flawed score and you get a flawed model.

### Sycophancy { #sycophancy }

The tendency to agree with the user over telling the truth.

**Why it matters:** A known side effect of optimising for human approval; worth remembering when a model agrees with you too easily.

### Rejection sampling / Best-of-N { #rejection-sampling-best-of-n }

Generate N answers, keep the best according to a judge or reward model, then train on those.

**Why it matters:** A simple, strong post-training method: let the model teach itself from its own best attempts.

<small>*Index aliases:* Best-of-N</small>

### Distillation { #distillation }

Train a smaller student model to imitate a bigger teacher's outputs.

**Why it matters:** How small, cheap models get surprisingly capable: they copy the behaviour of a frontier model.

### Model merging { #model-merging }

Averaging or combining the weights of several fine-tuned models into one.

**Why it matters:** Combines skills from different fine-tunes without retraining; cheap and oddly effective.

### Safety training / refusals { #safety-training-refusals }

Post-training the model to decline harmful requests and handle sensitive topics carefully.

**Why it matters:** Why a model says no to some requests; the behaviour is learned here, not hard-coded.
