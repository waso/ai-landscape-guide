# Math-notation decoder

The symbols that flash past on slides. Most formulas in this field are one of three things: a loss to minimise, an update rule, or a probability.

| Symbol | Read as | Meaning | Where you see it |
|---|---|---|---|
| `θ (theta)` | "theta" | All the model's parameters (weights) as one big vector. θ* is the best one. | Everywhere: p_θ, ∇_θ, θ ← θ − η∇ |
| `W, b` | weights, bias | A layer's weight matrix and bias vector. y = Wx + b is one linear layer. | Section 4; Map 5 |
| `x, y, ŷ` | x, y, y-hat | Input, true target, model's prediction. The hat means "estimated". | Loss functions |
| `𝓛 or J` | loss | The loss function; the number training minimises. | Loss curves, every training paper |
| `∇_θ 𝓛` | "gradient of the loss w.r.t. theta" | The vector of partial derivatives: how the loss changes when each weight changes. | Backprop, gradient descent |
| `η (eta) or α` | learning rate | Step size of each update. | θ ← θ − η ∇_θ 𝓛 |
| `←` | "is updated to" | Assignment in an update rule. | Gradient descent |
| `Σ, Π` | sum, product | Add up (or multiply) over an index: Σᵢ xᵢ. | Losses, probabilities |
| `𝔼[·]` | expected value | The average over a distribution; "on average over the data". | RL objectives, scaling laws |
| `P(y \| x)` | "probability of y given x" | Conditional probability; what a discriminative model outputs. | Classification |
| `p_θ(x_t \| x_<t)` | next-token probability | Probability the model with parameters θ assigns to token t given all earlier tokens. | Pre-training objective |
| `−log p` | negative log-likelihood | The cross-entropy loss for one token; small when the right token had high probability. | Loss function, perplexity = exp(mean loss) |
| `argmax` | "the argument that maximises" | The index of the largest value; the chosen class or token under greedy decoding. | Decoding |
| `softmax(z)ᵢ = eᶻⁱ / Σⱼ eᶻʲ` | softmax | Turns scores z into probabilities that sum to 1. | Output layer, attention |
| `σ(x) = 1 / (1 + e⁻ˣ)` | sigmoid | Squashes any number into (0, 1). | Logistic regression, gates |
| `ReLU(x) = max(0, x)` | "rectified linear unit" | Zero for negatives, identity for positives. GELU / SiLU are smooth versions. | Activation functions |
| `‖w‖², ‖w‖₁` | L2 norm squared, L1 norm | Size of a vector; used as a penalty in regularization. | Weight decay, L1 / L2 |
| `Wᵀ` | W transpose | Flip rows and columns of a matrix. | QKᵀ in attention |
| `QKᵀ / √d_k` | attention scores | Dot products of queries with keys, scaled by the square root of the key dimension. | Map 5; section 6 |
| `d_model, d_k, h` | model width, key dim, heads | Hidden size (e.g. 768), size per head (64), number of heads (12). | Transformer shape |
| `B, T, V` | batch, sequence length, vocab size | Typical tensor shape [B, T, d_model]; logits are [B, T, V]. | Shapes in code |
| `N, D, C` | parameters, data tokens, compute | The three scaling-law variables; C ≈ 6ND. | Scaling laws, Chinchilla |
| `KL(p ‖ q)` | KL divergence | How different distribution p is from q; zero when identical. | RLHF penalty, DPO's β term |
| `π_θ, r, A, γ` | policy, reward, advantage, discount | The policy (the model), the reward, how much better than average an action was, and how much future rewards count. | PPO, GRPO |
| `ε (epsilon)` | clip range or small constant | PPO's clipping range (≈ 0.2), or a tiny number to avoid division by zero. | PPO; AdamW |
| `β (beta)` | beta | Strength of the KL penalty in DPO / RLHF, or Adam's momentum coefficients β₁, β₂. | DPO, AdamW |
| `x ~ p` | "x is sampled from p" | Draw a random value from distribution p. | Sampling, RL |
| `𝒪(n²)` | big-O notation | Cost grows with the square of n. Attention is 𝒪(T²) in sequence length. | Quadratic cost of attention |
| `⊙` | element-wise product | Multiply matching elements. Appears in gates (SwiGLU / GLU) and masks. | SwiGLU, gating |

## The three formulas worth memorising

- `θ ← θ − η ∇_θ 𝓛` — gradient descent: move the weights a little downhill.
- `𝓛 = −Σ log p_θ(x_t | x_<t)` — next-token cross-entropy: be surprised as little as possible by the real text.
- `Attention(Q,K,V) = softmax(QKᵀ / √d_k) V` — each token takes a weighted average of the others, weights from query–key similarity.
