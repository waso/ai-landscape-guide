# 4. Neural-network foundations

*The training loop and building blocks used by every stage that changes weights*

This is what Raschka's book builds by hand. Pre-training, post-training and your own fine-tuning all run the same loop: forward pass → loss → backprop → optimizer step (Map 3).

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Neuron / perceptron { #neuron-perceptron }

The basic unit: a weighted sum of inputs plus a bias, passed through an activation function.

**Why it matters:** Everything in deep learning is millions of these wired together; each one is just multiply, add, squash.

<small>*Index aliases:* Perceptron</small>

### Weights, biases, parameters ★ { #weights-biases-parameters }

The numbers inside the model that training adjusts. "7B" means 7 billion of them.

**Why it matters:** The parameters are the model. Download the weights and you have it; change them and you have a different model.

<small>*Index aliases:* Weights (the file), Parameters</small>

### Activations { #activations }

The intermediate values flowing through the network for one input (as opposed to the weights, which are fixed during inference).

**Why it matters:** Weights are what the model knows; activations are what it is thinking right now about this input. Interpretability studies activations.

### Layer / hidden layer { #layer-hidden-layer }

A group of neurons computed together. Layers between input and output are hidden layers.

**Why it matters:** "Deep" simply means many hidden layers; each adds a level of abstraction.

<small>*Index aliases:* Hidden layer</small>

### Multi-Layer Perceptron / Feed-forward network { #multi-layer-perceptron-feed-forward-network }

*Also known as:* MLP, FFN

Stacked fully-connected layers. Also the second half of every Transformer block.

**Why it matters:** The plainest neural network; inside an LLM the FFN layers are where most of the parameters, and most of the stored knowledge, live.

### Activation function { #activation-function }

*Also known as:* ReLU, GELU, SiLU/Swish, sigmoid, tanh

Non-linearity applied after a layer. GELU and SiLU are the ones used inside LLMs.

**Why it matters:** Without it, stacking layers would collapse into one straight line. The non-linearity is what lets networks learn curves and complex rules.

### Softmax { #softmax }

Turns a vector of scores into probabilities that sum to 1.

**Why it matters:** How the model expresses "70% sure the next word is 'Paris'". Applied at the output and inside attention.

### Logits { #logits }

Raw, unnormalised scores that come out before softmax.

**Why it matters:** What the model actually computes; softmax just converts them to probabilities. Temperature acts on logits.

### One-hot encoding { #one-hot-encoding }

Representing a category as a vector of zeros with a single 1 at that category's position.

**Why it matters:** The naive way to feed words to a network. Embeddings replace it with dense vectors that carry meaning.

### Forward pass { #forward-pass }

Running an input through the network to get an output.

**Why it matters:** Inference is just a forward pass; training is a forward pass plus a backward pass.

### Loss function ★ { #loss-function }

*Also known as:* cross-entropy, MSE

A number measuring how wrong the output is; training minimises it. Cross-entropy for classification and next-token prediction, mean squared error for regression.

**Why it matters:** Defines what "better" means. The whole of training is "make this number smaller".

<small>*Index aliases:* Cross-entropy</small>

### Backpropagation (backprop) ★ { #backpropagation }

The algorithm that computes how much each weight contributed to the loss, by applying the chain rule backwards through the network.

**Why it matters:** Tells every one of the billions of weights which direction to move. Without it, training deep networks would be hopeless.

### Gradient { #gradient }

The direction and size of change in loss for each weight.

**Why it matters:** The "which way is downhill" signal; backprop computes it, the optimizer follows it.

### Gradient descent (SGD) ★ { #gradient-descent }

Nudge each weight a small step against its gradient. Stochastic gradient descent does this on one mini-batch per step.

**Why it matters:** The learning rule behind all of deep learning: take a small step downhill, repeat millions of times.

<small>*Index aliases:* SGD</small>

### Optimizer { #optimizer }

*Also known as:* Adam, AdamW

Smarter update rules that adapt the step size per weight using running averages of gradients. AdamW is the default for Transformers.

**Why it matters:** Makes training converge faster and more reliably than plain gradient descent, at the cost of extra memory per weight.

### Learning rate (LR) { #learning-rate }

How big each update step is.

**Why it matters:** The single most important hyperparameter. Too high and training blows up; too low and it never gets anywhere.

<small>*Index aliases:* Learning rate (LR)</small>

### Batch / mini-batch { #batch-mini-batch }

The group of examples processed in one step before the weights are updated.

**Why it matters:** Bigger batches use the GPU better and give smoother gradients; smaller ones fit in memory. A knob you will see in every training script.

### Epoch { #epoch }

One full pass over the training set.

**Why it matters:** Classic ML trains for many epochs; LLM pre-training usually sees each token about once.

### Training loop { #training-loop }

Forward pass → loss → backward pass → optimizer step, repeated. Everything from a toy MLP to a frontier LLM runs this loop.

**Why it matters:** If you understand this loop (Map 3) you understand what "training" means at every stage of Map 2.

### Weight initialization { #weight-initialization }

How the weights are set before training starts: small random numbers with a carefully chosen scale.

**Why it matters:** A bad starting scale makes gradients vanish or explode on step one; good initialization makes deep networks trainable.

### Dropout { #dropout }

Randomly switch off neurons during training.

**Why it matters:** Forces the network not to rely on any single neuron, which reduces overfitting.

### Weight decay { #weight-decay }

Shrink the weights slightly every step (L2-style regularization).

**Why it matters:** Keeps weights small, which helps generalisation; the "W" in AdamW.

### Normalization { #normalization }

*Also known as:* BatchNorm, LayerNorm, RMSNorm

Rescaling activations so they stay in a healthy range. LayerNorm and its cheaper cousin RMSNorm are the ones used in Transformers.

**Why it matters:** Keeps training stable in very deep networks; without it, values drift and training diverges.

### Residual / skip connection { #residual-skip-connection }

Add a layer's input to its output. Forms the residual stream of a Transformer.

**Why it matters:** Lets gradients flow straight through dozens of layers, which is what makes 100-layer networks trainable at all.

<small>*Index aliases:* Skip connection</small>

### Vanishing / exploding gradients { #vanishing-exploding-gradients }

Gradients shrinking to nothing or blowing up as they flow back through many layers.

**Why it matters:** The historical reason deep networks did not work before ~2012; residuals, normalization and better initialization fixed it.

<small>*Index aliases:* Exploding gradients, Vanishing gradients</small>

### Embedding ★ { #embedding }

A learned vector of numbers representing a token, word, image or item so that similar things end up close together.

**Why it matters:** How a computer represents meaning: "king" and "queen" become nearby points. The input to every LLM and the basis of semantic search.

### Latent space / representation { #latent-space-representation }

The internal vector space in which the model represents meaning.

**Why it matters:** Where the model "thinks": arithmetic on these vectors (king − man + woman ≈ queen) is what makes them useful.

<small>*Index aliases:* Latent space</small>

### Inductive bias { #inductive-bias }

The assumptions an architecture builds in: CNNs assume nearby pixels matter, RNNs assume order, Transformers assume very little.

**Why it matters:** Explains why CNNs need less data for images and why Transformers need huge data but scale further.

### Tensor { #tensor }

A multi-dimensional array (vector, matrix, and beyond).

**Why it matters:** The data type everything in deep learning is made of; a "shape" like [batch, tokens, 768] tells you what is flowing where.

### Autograd / computational graph { #autograd-computational-graph }

Framework machinery (PyTorch) that records every operation so backprop can be computed automatically.

**Why it matters:** Why you never write backprop by hand: call `loss.backward()` and PyTorch does the calculus.

<small>*Index aliases:* Computational graph</small>

### Convolutional Neural Network (CNN) { #convolutional-neural-network }

A network using small sliding filters. The classic architecture for images (LeNet, AlexNet, ResNet).

**Why it matters:** Detects the same pattern anywhere in an image with few parameters. Still the workhorse for vision on small devices.

<small>*Index aliases:* CNN</small>

### Recurrent networks { #recurrent-networks }

*Also known as:* RNN, LSTM, GRU

Networks that process sequences one step at a time with a memory state. They dominated language tasks before Transformers replaced them.

**Why it matters:** Worked for sequences but could not be parallelised and forgot long-range context. Attention fixed both problems.

<small>*Index aliases:* LSTM / GRU</small>

### Sequence-to-sequence (seq2seq) { #sequence-to-sequence }

An encoder reads an input sequence, a decoder writes an output sequence (early translation models).

**Why it matters:** Attention was invented to fix seq2seq's bottleneck of squeezing a whole sentence into one vector.

<small>*Index aliases:* seq2seq</small>

### Autoencoder / VAE { #autoencoder-vae }

*Also known as:* Variational Autoencoder

Networks trained to compress and then reconstruct their input. The variational version learns a smooth latent space you can sample from.

**Why it matters:** Learns compact representations without labels; the VAE is also the compressor inside Stable Diffusion.

<small>*Index aliases:* VAE</small>

### Generative Adversarial Network (GAN) { #generative-adversarial-network }

A generator and a discriminator trained against each other.

**Why it matters:** Produced the first photorealistic generated faces (2014–2020); mostly replaced by diffusion models, which are easier to train.

<small>*Index aliases:* GAN</small>

### Diffusion model { #diffusion-model }

Generates images (and audio, video) by learning to reverse a gradual noising process.

**Why it matters:** The engine behind Stable Diffusion, DALL·E 2/3 and Midjourney: start from noise, remove it step by step toward the prompt.
