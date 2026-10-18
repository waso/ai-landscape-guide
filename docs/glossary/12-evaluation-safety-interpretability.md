# 12. Evaluation, safety & interpretability

*Cross-cutting: measuring, attacking and understanding models at every stage*

These terms show up at every stage: a loss curve during pre-training, red-teaming before release, an eval set for your own fine-tune.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Evals / evaluation <a id="evals-evaluation"></a>
Any systematic measurement of model quality: benchmarks, human ratings, your own test sets.

**Why it matters:** The only way to know whether a change helped; "it feels better" is not evidence.

### Benchmark <a id="benchmark"></a>
A fixed dataset plus a scoring rule for comparing models.

**Why it matters:** How leaderboards are made; useful, and easy to game.

### MMLU / MMLU-Pro <a id="mmlu-mmlu-pro"></a>
Multiple-choice knowledge questions across 57 subjects; MMLU-Pro is the harder successor with 10 answer options across 14 disciplines.

**Why it matters:** The classic general-knowledge score; now saturated for top models.

<small>*Index aliases:* MMLU</small>

### GSM8K, MATH, AIME <a id="gsm8k-math-aime"></a>
Maths benchmarks from grade-school word problems up to competition level.

**Why it matters:** Where reasoning models show the biggest jumps.

<small>*Index aliases:* GSM8K, AIME</small>

### HumanEval, SWE-bench <a id="humaneval-swe-bench"></a>
Code benchmarks: generating functions from docstrings, and fixing real GitHub issues end to end.

**Why it matters:** SWE-bench (Verified) is the number to watch for coding agents.

<small>*Index aliases:* SWE-bench, HumanEval</small>

### GPQA <a id="gpqa"></a>
Graduate-level science questions designed to be Google-proof.

**Why it matters:** Tests deep expertise rather than memorised trivia.

### ARC-AGI, Humanity's Last Exam <a id="arc-agi-humanity-s-last-exam"></a>
Benchmarks designed to stay hard: abstract visual puzzles (ARC-AGI) and expert questions across every field (HLE).

**Why it matters:** The current frontier benchmarks; when older ones saturate, these are what headlines quote.

<small>*Index aliases:* HLE (Humanity's Last Exam), ARC-AGI</small>

### Agentic benchmarks <a id="agentic-benchmarks"></a>
*Also known as:* SWE-bench Verified, τ-bench, Terminal-Bench

Benchmarks scoring a model on multi-step tasks with tools, not single answers.

**Why it matters:** Measure what matters for agents: finishing the job, not answering a question.

<small>*Index aliases:* τ-bench / Terminal-Bench</small>

### Needle in a haystack <a id="needle-in-a-haystack"></a>
Hide one fact in a very long document and check whether the model can retrieve it.

**Why it matters:** The standard test of whether a long context window really works.

<small>*Index aliases:* NIAH</small>

### pass@k <a id="pass-k"></a>
The chance that at least one of k generated attempts is correct.

**Why it matters:** Used for code and maths; pass@1 is what a user experiences, pass@10 shows the model's potential with search.

### Chatbot Arena / LMArena / Elo <a id="chatbot-arena-lmarena-elo"></a>
Crowd-sourced blind comparisons of models, producing an Elo-style leaderboard.

**Why it matters:** The closest thing to "which model do people prefer".

<small>*Index aliases:* LMArena / Chatbot Arena, Elo rating</small>

### Data contamination <a id="data-contamination"></a>
Benchmark questions leaking into training data, inflating scores.

**Why it matters:** Why benchmark numbers are treated with suspicion and why private test sets exist.

<small>*Index aliases:* Contamination</small>

### Factuality / hallucination rate <a id="factuality-hallucination-rate"></a>
The fraction of generated claims that are unsupported or false.

**Why it matters:** The metric that matters most for RAG and research assistants.

<small>*Index aliases:* Factuality</small>

### Bias and fairness <a id="bias-and-fairness"></a>
Systematic differences in model behaviour across groups of people.

**Why it matters:** A legal and ethical requirement in hiring, lending and medicine.

### Robustness <a id="robustness"></a>
Stability of answers under rephrasing, typos, noise and adversarial inputs.

**Why it matters:** A model that changes its answer over a comma is not production-ready.

### Explainability <a id="explainability"></a>
*Also known as:* SHAP, LIME

Methods that attribute a classic-ML prediction to the features that drove it.

**Why it matters:** Required in regulated decisions; the classic-ML cousin of LLM interpretability.

<small>*Index aliases:* SHAP / LIME, Explainability (SHAP, LIME)</small>

### Red teaming <a id="red-teaming"></a>
Deliberately attacking a model to find harmful or broken behaviour before release.

**Why it matters:** Finds failures before users (or attackers) do.

<small>*Index aliases:* Red team</small>

### Jailbreak <a id="jailbreak"></a>
A prompt that tricks the model into ignoring its safety training.

**Why it matters:** Safety behaviour is learned, not enforced, so defences are layered.

<small>*Index aliases:* Jailbreaking</small>

### Over-refusal <a id="over-refusal"></a>
A model declining harmless requests because they superficially resemble harmful ones.

**Why it matters:** The other side of safety training; labs tune to minimise both harm and over-refusal.

### AI safety / responsible scaling <a id="ai-safety-responsible-scaling"></a>
*Also known as:* RSP, safety levels

The field concerned with preventing harm from AI systems, from today's misuse to risks at larger scale. Responsible-scaling policies tie capability thresholds to the safeguards required before release.

**Why it matters:** Where alignment, red teaming and safety levels come from; how labs commit to not shipping a model until matching safeguards exist.

<small>*Index aliases:* Responsible Scaling Policy, ASL (AI Safety Level), AI safety</small>

### Sandbagging / evaluation awareness <a id="sandbagging-evaluation-awareness"></a>
A model behaving differently when it suspects it is being tested, even hiding capabilities.

**Why it matters:** A newer safety concern: evals are only trustworthy if the model cannot tell it is being evaluated.

<small>*Index aliases:* Evaluation awareness, Sandbagging</small>

### Scalable oversight <a id="scalable-oversight"></a>
Techniques for humans to supervise models on tasks they cannot fully judge themselves (debate, AI-assisted review).

**Why it matters:** The long-term question of alignment: how to check work better than yours.

### Interpretability / mechanistic interpretability <a id="interpretability-mechanistic-interpretability"></a>
Studying what happens inside the network: which neurons, features and circuits do what.

**Why it matters:** Lets researchers see why a model answered as it did, instead of a black box.

<small>*Index aliases:* Mechanistic interpretability</small>

### Features, superposition, Sparse Autoencoders (SAE) <a id="features-superposition-sparse-autoencoders"></a>
Features are the interpretable concepts a model represents; superposition is the finding that it packs more features than it has neurons; Sparse Autoencoders are the tool that unmixes activations into those features.

**Why it matters:** Found concrete concepts inside models (a "Golden Gate Bridge" feature); a path to steering and auditing.

<small>*Index aliases:* SAE, Sparse Autoencoder (SAE), Superposition</small>

### Model card / system card <a id="model-card-system-card"></a>
Documentation of a model's training, capabilities, limits and safety testing.

**Why it matters:** Where to look before trusting a model.

<small>*Index aliases:* System card</small>
