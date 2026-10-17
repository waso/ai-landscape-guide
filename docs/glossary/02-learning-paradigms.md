# 2. Learning paradigms

*How a model learns: from labels, from structure, from itself, or from rewards*

Every training technique in this guide is one of these four in disguise. Pre-training is self-supervised, SFT is supervised, RLHF is reinforcement learning.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Supervised learning ★ { #supervised-learning }

Learning from examples that come with the correct answer (labels); the model learns input → label. Used in classic ML, in SFT and in reward-model training.

**Why it matters:** Most accurate way to learn when you can afford labelled examples. Its limit is the cost of labelling.

### Unsupervised learning { #unsupervised-learning }

Finding structure in data with no labels: grouping, compressing, spotting anomalies.

**Why it matters:** Works on data nobody has labelled, which is most data. Finds groups and outliers you did not know to look for.

### Self-supervised learning (SSL) ★ { #self-supervised-learning }

Supervised-style training where the label is carved out of the data itself, e.g. hide the next word and predict it. This is how LLMs are pre-trained.

**Why it matters:** Turns the whole internet into free training labels. The single trick that made LLMs possible at scale.

<small>*Index aliases:* SSL, SSL (self-supervised)</small>

### Semi-supervised learning { #semi-supervised-learning }

Mixing a small labelled set with a lot of unlabelled data.

**Why it matters:** Gets most of the accuracy of supervised learning with a fraction of the labelling cost.

### Reinforcement Learning (RL) ★ { #reinforcement-learning }

An agent takes actions in an environment and learns from rewards instead of labelled answers. Used in games, robotics and LLM post-training (RLHF, GRPO).

**Why it matters:** Lets a model get better than its teachers: it can discover strategies no example showed it, as long as you can score the result.

<small>*Index aliases:* RL, RL (reinforcement learning)</small>

### Agent, environment, policy, reward (RL vocabulary) { #agent-environment-policy-reward }

The agent is the learner, the environment is what it acts on, the policy is its decision rule (for LLMs: the model itself), the reward is the feedback signal.

**Why it matters:** Decode any RL video: "policy" = the model being trained, "reward" = the score it is chasing.

<small>*Index aliases:* RL vocabulary, Policy (RL), Reward (RL), Environment (RL)</small>

### Exploration vs exploitation { #exploration-vs-exploitation }

The RL dilemma: try new actions to discover better ones (explore) or repeat what already works (exploit).

**Why it matters:** Explains why RL training samples several answers per prompt instead of only the best one.

### Q-learning / DQN (Deep Q-Network) { #q-learning-dqn }

Classic value-based RL: learn a table (or network) estimating how good each action is in each state. DQN was the 2013 breakthrough that played Atari games from pixels.

**Why it matters:** The RL you see in game-playing demos. LLM post-training uses policy-based methods (PPO, GRPO) instead.

<small>*Index aliases:* Deep Q-Network, DQN</small>

### Monte Carlo Tree Search / AlphaGo (MCTS) { #monte-carlo-tree-search-alphago }

Search that looks ahead by simulating many possible futures and focusing on promising ones. Combined with neural networks (AlphaGo) it beat Go champion Lee Sedol in 2016.

**Why it matters:** An ancestor of "thinking longer" in reasoning models: spend more compute at decision time to get better decisions. (Today's reasoning models do it with long chains of thought, not tree search.)

<small>*Index aliases:* MCTS, AlphaGo</small>

### Imitation learning / behaviour cloning { #imitation-learning-behaviour-cloning }

Learning a policy by copying demonstrations from an expert.

**Why it matters:** SFT is imitation learning: the model copies the ideal answers humans wrote. RL is what lets it go beyond them.

<small>*Index aliases:* Behaviour cloning</small>

### Transfer learning { #transfer-learning }

Reusing what a model learned on one task or dataset as the starting point for another. Fine-tuning a pre-trained model is transfer learning.

**Why it matters:** Why you never start from zero: a model that already knows language learns your task from a few hundred examples.

### Contrastive learning { #contrastive-learning }

*Also known as:* CLIP, SimCLR

Training that pulls representations of matching pairs together and pushes non-matching pairs apart (an image and its caption; two views of the same photo).

**Why it matters:** How embedding models and CLIP learn that "a photo of a cat" and the cat picture belong together.

### Classification { #classification }

Predicting a category (spam / not spam, cat / dog).

**Why it matters:** The most common ML task in business. Next-token prediction is also a classification over the vocabulary.

### Regression { #regression }

Predicting a continuous number (price, temperature, time to failure).

**Why it matters:** The other basic task; when the answer is a number, it is regression.

### Clustering { #clustering }

Grouping similar items together without labels (k-means).

**Why it matters:** Finds natural groups: customer segments, topics in documents, duplicate records.

### Dimensionality reduction { #dimensionality-reduction }

Compressing many features into fewer while keeping the important structure (PCA, t-SNE, UMAP).

**Why it matters:** How people draw 2-D pictures of embeddings: hundreds of dimensions squashed down so you can see clusters.

<small>*Index aliases:* t-SNE / UMAP</small>

### Anomaly detection { #anomaly-detection }

Flagging data points that do not look like the rest.

**Why it matters:** Fraud, intrusion and fault detection: learn what normal looks like, alert on the rest.

### Label / ground truth { #label-ground-truth }

The known correct answer attached to a training example.

**Why it matters:** The expensive ingredient of supervised learning; its quality caps the model's quality.

<small>*Index aliases:* Ground truth</small>
