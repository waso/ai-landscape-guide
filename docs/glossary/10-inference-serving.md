# 10. Inference & serving

*Stage 6: running the model to produce tokens, fast and cheaply*

No weights change here. Everything is about choosing the next token well, and about memory, latency and cost. Map 4 shows the whole request path.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Inference ★ <a id="inference"></a>
Using a trained model to produce output. No weights change.

**Why it matters:** What every API call and chat message is. The cost and speed of AI products are decided here.

### Autoregressive generation <a id="autoregressive-generation"></a>
Produce one token, append it to the input, run again, until a stop token or the max length is reached.

**Why it matters:** Why text appears word by word, and why long answers take proportionally longer.

### Prefill vs decode <a id="prefill-vs-decode"></a>
Prefill processes the whole prompt in one parallel pass (compute-bound). Decode produces tokens one at a time (memory-bound).

**Why it matters:** Explains the two numbers you feel: a pause before the first token (prefill), then a steady stream (decode).

<small>*Index aliases:* Prefill, Decode</small>

### KV cache <a id="kv-cache"></a>
Storing the keys and values of all previous tokens so each new token does not recompute them.

**Why it matters:** Makes generation many times faster; its memory size is the main limit on long contexts and many parallel users.

### Decoding strategy <a id="decoding-strategy"></a>
How the next token is chosen from the probability distribution the model outputs.

**Why it matters:** The same model can sound careful or creative depending only on this choice.

### Greedy decoding <a id="greedy-decoding"></a>
Always pick the most probable token.

**Why it matters:** Deterministic and fast, but tends to repeat itself and miss better overall sentences.

### Sampling <a id="sampling"></a>
Pick the next token randomly according to the model's probabilities.

**Why it matters:** Gives variety and more natural text; the reason the same prompt gives different answers.

### Temperature ★ <a id="temperature"></a>
Scales the logits before softmax. Low values make output focused and near-deterministic, high values make it diverse and random. 0 is effectively greedy.

**Why it matters:** Your main creativity knob: low for code and facts, higher for brainstorming.

### Top-k / Top-p (nucleus) sampling <a id="top-k-top-p-nucleus-sampling"></a>
Only sample from the k most likely tokens, or from the smallest set of tokens whose probabilities add up to p.

**Why it matters:** Cuts off the long tail of nonsense tokens so sampling stays creative but coherent.

<small>*Index aliases:* Nucleus sampling, Top-p, Top-k</small>

### Beam search <a id="beam-search"></a>
Keep several candidate sequences and expand the best ones.

**Why it matters:** Finds higher-probability whole sentences; common in translation, rarely used in chat because it sounds bland.

### Repetition / frequency penalty <a id="repetition-frequency-penalty"></a>
Lower the probability of tokens that have already appeared.

**Why it matters:** Stops the model from looping on the same phrase.

<small>*Index aliases:* Frequency penalty</small>

### Constrained / grammar-based decoding <a id="constrained-grammar-based-decoding"></a>
Restricting sampling so the output must follow a grammar or JSON schema.

**Why it matters:** Guarantees valid JSON or a fixed set of choices, rather than hoping the model complies.

<small>*Index aliases:* Grammar-constrained decoding</small>

### Logprobs <a id="logprobs"></a>
The log-probabilities of generated tokens, which APIs can expose.

**Why it matters:** A cheap confidence signal: low probability on a key token is a hint the model is guessing.

### Max tokens / stop sequences <a id="max-tokens-stop-sequences"></a>
The limit on output length, and strings that end generation early.

**Why it matters:** Controls cost and prevents run-on answers.

<small>*Index aliases:* Stop sequence, Max tokens</small>

### Streaming <a id="streaming"></a>
Sending tokens to the client as they are generated.

**Why it matters:** Makes a 10-second answer feel instant because the user starts reading immediately.

### Latency: TTFT, TPOT, tokens/sec <a id="latency-ttft-tpot-tokens-sec"></a>
*Also known as:* time to first token, time per output token

Time to first token measures prefill. Time per output token (the gap between tokens, also called inter-token latency) measures decode; tokens per second is its inverse.

**Why it matters:** The numbers users feel: optimise TTFT for chat, TPOT for long outputs.

<small>*Index aliases:* TPOT, Inter-token latency, TTFT, Tokens per second</small>

### Throughput / batching / continuous batching <a id="throughput-batching-continuous-batching"></a>
Serving many requests at once by batching their decode steps. Continuous batching slots new requests in mid-stream.

**Why it matters:** Serves many more users per GPU, which is what makes API prices possible.

<small>*Index aliases:* Continuous batching</small>

### PagedAttention / vLLM <a id="pagedattention-vllm"></a>
Managing the KV cache like virtual-memory pages so GPU memory is not wasted. vLLM is the open-source engine that popularised it.

**Why it matters:** Fits more simultaneous requests in the same GPU memory, roughly 2–4× the throughput.

<small>*Index aliases:* vLLM, PagedAttention</small>

### Quantization <a id="quantization"></a>
*Also known as:* INT8, INT4, FP8

Storing weights (and sometimes activations) in fewer bits.

**Why it matters:** Cuts memory 2–4× and speeds up inference, at a small quality cost; how a 70B model fits on one GPU or a laptop.

<small>*Index aliases:* INT8 / INT4</small>

### GGUF, GPTQ, AWQ <a id="gguf-gptq-awq"></a>
Common quantized formats and methods. GGUF is the format llama.cpp, Ollama and LM Studio use.

**Why it matters:** When a download page lists "Q4_K_M", it is a 4-bit GGUF file ready for local use.

<small>*Index aliases:* GGUF, GPTQ / AWQ</small>

### Speculative decoding <a id="speculative-decoding"></a>
A small draft model proposes several tokens, the big model verifies them in one pass.

**Why it matters:** Same output as the big model, noticeably faster, because verifying is cheaper than generating.

### Serving engines <a id="serving-engines"></a>
*Also known as:* vLLM, SGLang, TensorRT-LLM, TGI, llama.cpp, Ollama

Software that loads weights and serves requests efficiently: the first four for servers, the last two for laptops.

**Why it matters:** The difference between a demo and a production service; they handle batching, caching and memory for you.

### Prompt caching <a id="prompt-caching"></a>
Reusing the KV cache for a repeated prefix (a long system prompt, a set of documents) across requests.

**Why it matters:** Cuts cost and latency sharply when many requests share the same long beginning.

### Semantic caching <a id="semantic-caching"></a>
Caching whole answers keyed by the meaning of the question, so a similar question returns the stored answer without calling the model.

**Why it matters:** Avoids paying for the same answer twice when users ask the same thing in different words.

### Model routing / cascades <a id="model-routing-cascades"></a>
Sending each request to the cheapest model likely to handle it, escalating to a bigger one only when needed.

**Why it matters:** Big cost savings with little quality loss, because most requests are easy.

<small>*Index aliases:* Cascades</small>

### Batch API, rate limits <a id="batch-api-rate-limits"></a>
Providers offer discounted non-urgent batch processing, and cap how many requests and tokens you can send per minute.

**Why it matters:** Shapes system design: batch what can wait, queue and retry for the rest.

<small>*Index aliases:* Rate limits</small>

### Long context / context extension <a id="long-context-context-extension"></a>
Running models beyond their trained length with positional scaling tricks (RoPE scaling, YaRN) and better attention kernels.

**Why it matters:** How 4k-context models became 128k; recall at the far end of the window is still weaker.

<small>*Index aliases:* YaRN / RoPE scaling</small>

### On-device / edge inference <a id="on-device-edge-inference"></a>
Running small quantized models on phones and laptops with no server.

**Why it matters:** Private, offline and free per use; the trade-off is a much smaller model.

<small>*Index aliases:* Edge inference</small>

### Model size vs memory <a id="model-size-vs-memory"></a>
Rule of thumb: parameters × bytes per weight. A 7B model is about 14 GB in 16-bit and about 4 GB at 4-bit, plus the KV cache.

**Why it matters:** Quick way to know whether a model fits your GPU or laptop before downloading it.
