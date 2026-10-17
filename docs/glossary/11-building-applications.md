# 11. Building applications

*Stage 7: prompting, retrieval, tools and agents around a frozen model*

Where most engineers spend their time. The model is a component; the system around it (Map 6) decides whether the product works.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Prompt { #prompt }

The text you send to the model: instructions, context, question.

**Why it matters:** The model's entire view of your task; everything it does not say, the model does not know.

### System prompt ★ { #system-prompt }

Instructions set by the developer that frame the whole conversation: persona, rules, available tools, output format.

**Why it matters:** Your main control surface as an engineer; most product behaviour is written here, not trained.

### Prompt engineering { #prompt-engineering }

Crafting prompts to get reliable results: clear instructions, examples, explicit output format, role, constraints. Prompts are versioned and tested like code.

**Why it matters:** The cheapest and fastest way to improve a model's output; always the first thing to try.

<small>*Index aliases:* Prompt template</small>

### Zero-shot / few-shot { #zero-shot-few-shot }

Asking with no examples versus including a few worked examples in the prompt.

**Why it matters:** A couple of examples in the prompt often beat pages of instructions.

<small>*Index aliases:* Few-shot, Zero-shot</small>

### In-context learning (ICL) { #in-context-learning }

The model's ability to pick up a task from examples in the prompt without any weight updates.

**Why it matters:** Why few-shot works: the model adapts on the fly, no training needed.

<small>*Index aliases:* ICL</small>

### Chain-of-Thought (CoT) { #chain-of-thought }

Asking the model to reason step by step before answering.

**Why it matters:** Noticeably more accurate on reasoning tasks because the model gets to "use scratch paper"; reasoning models bake this in.

<small>*Index aliases:* CoT</small>

### Self-consistency / majority voting { #self-consistency-majority-voting }

Sample several answers and take the most common one.

**Why it matters:** A simple way to buy accuracy with more compute; a form of test-time scaling you can do from the outside.

<small>*Index aliases:* Majority voting</small>

### Tree of Thoughts / search { #tree-of-thoughts-search }

Explore several reasoning paths, evaluate them, and expand the promising ones, instead of one linear chain.

**Why it matters:** Better on hard planning problems; the application-level cousin of MCTS.

<small>*Index aliases:* Tree of Thoughts</small>

### Structured outputs / JSON mode { #structured-outputs-json-mode }

Forcing the model to answer in a machine-readable format, often validated against a schema.

**Why it matters:** Makes model output safe to parse in code, which any real integration needs.

<small>*Index aliases:* JSON mode</small>

### Function calling / tool use { #function-calling-tool-use }

The model emits a structured request (call get_weather with city = Kraków), your code runs it and returns the result for the model to continue.

**Why it matters:** Lets the model act on the world and fetch live data instead of guessing from memory.

<small>*Index aliases:* Tool use, Function calling</small>

### Agent ★ { #agent }

An LLM in a loop: observe → decide → act with tools → observe the result, until the task is done.

**Why it matters:** Turns a chatbot into something that completes multi-step tasks: fixing a bug, booking a trip, researching a question.

### Workflows vs agents { #workflows-vs-agents }

A workflow is a fixed sequence of LLM calls you program; an agent decides its own next step at runtime.

**Why it matters:** Workflows are predictable and cheap; agents are flexible and harder to control. Use the simplest one that works.

### Agentic workflow, ReAct, planning { #agentic-workflow-react-planning }

Patterns for structuring agents: interleaving reasoning and actions (ReAct), explicit plans, decomposition into sub-tasks, reflection.

**Why it matters:** Known recipes that make agents more reliable than a bare loop.

<small>*Index aliases:* ReAct</small>

### Multi-agent system { #multi-agent-system }

Several specialised agents (planner, coder, reviewer, researcher) coordinating on one task.

**Why it matters:** Splits a big job into roles with separate contexts; helps on long tasks, adds coordination overhead.

<small>*Index aliases:* Multi-agent</small>

### Model Context Protocol (MCP) { #model-context-protocol }

An open standard for connecting models to tools and data sources through a common server interface, so any MCP client can use any MCP server.

**Why it matters:** Write a tool once, use it from every assistant: the "USB-C of AI tools". Your Spring AI servers speak this.

<small>*Index aliases:* MCP</small>

### Agent-to-Agent protocol (A2A) { #agent-to-agent-protocol }

A standard for agents from different vendors to discover each other and exchange tasks.

**Why it matters:** MCP connects an agent to tools; A2A connects agents to agents.

<small>*Index aliases:* A2A</small>

### Computer-use / browser agents { #computer-use-browser-agents }

Agents that operate a screen, browser or terminal through screenshots, clicks and keystrokes.

**Why it matters:** Lets a model use software that has no API, which is most software.

<small>*Index aliases:* Computer use, Browser agent</small>

### Agentic coding { #agentic-coding }

*Also known as:* Claude Code, Cursor, Copilot agent mode

Coding assistants that read a repository, edit files, run tests and iterate on their own. "Vibe coding" is building by describing what you want and accepting the result.

**Why it matters:** The most widely adopted agent use case; changes how software gets written.

<small>*Index aliases:* Vibe coding, Cursor / Copilot</small>

### Sandboxing { #sandboxing }

Running an agent's code and tool calls in an isolated environment with limited permissions.

**Why it matters:** Contains the damage when an agent makes a mistake or is tricked by prompt injection.

<small>*Index aliases:* Sandbox</small>

### Human-in-the-loop (HITL) { #human-in-the-loop }

Requiring a person to approve certain steps (sending the email, deleting the file, paying).

**Why it matters:** The standard safety net for agents taking real actions.

<small>*Index aliases:* HITL</small>

### Retrieval-Augmented Generation (RAG) ★ { #retrieval-augmented-generation }

Fetch relevant documents (search or vector database) and put them in the prompt so the model answers from your data.

**Why it matters:** Gives the model knowledge it was never trained on, kept up to date, with sources, without any training.

<small>*Index aliases:* RAG, Agentic RAG</small>

### Text embeddings { #text-embeddings }

Vectors representing the meaning of a text chunk; similar texts land near each other. Produced by a separate embedding model.

**Why it matters:** The basis of semantic search: find documents by meaning, not by matching keywords.

<small>*Index aliases:* Embedding model</small>

### Vector database { #vector-database }

*Also known as:* pgvector, Pinecone, Weaviate, Qdrant; FAISS is the underlying index library

A store that indexes embeddings for fast nearest-neighbour search.

**Why it matters:** Finds the 10 most relevant chunks out of millions in milliseconds.

<small>*Index aliases:* Pinecone / Weaviate / Qdrant, FAISS</small>

### Chunking { #chunking }

Splitting documents into pieces small enough to embed and retrieve.

**Why it matters:** Chunk size and overlap decide whether retrieval finds the right passage; one of the most-tuned RAG knobs.

### Semantic / hybrid search { #semantic-hybrid-search }

Searching by embedding similarity; hybrid search combines it with classic keyword search (BM25).

**Why it matters:** Hybrid catches both "same meaning, different words" and exact identifiers like error codes.

<small>*Index aliases:* BM25 / keyword search, Hybrid search</small>

### Reranker { #reranker }

A second model that re-orders retrieved chunks by relevance before they go into the prompt.

**Why it matters:** Cheap accuracy boost for RAG: retrieve 50 loosely, keep the best 5 precisely.

### Grounding / citations { #grounding-citations }

Tying answers to retrieved sources so claims can be checked.

**Why it matters:** Reduces hallucination and lets users verify; does not eliminate it.

<small>*Index aliases:* Citations</small>

### Context engineering { #context-engineering }

Managing everything in the context window (system prompt, retrieved docs, tool results, memory) so the model has what it needs and nothing more.

**Why it matters:** Too little context and the model guesses; too much and it gets lost and costs more. Good agents are mostly good context management.

### Memory (short- and long-term) { #memory-short-and-long-term }

Conversation history inside the context window versus facts stored outside and retrieved later.

**Why it matters:** How an assistant remembers you across sessions: it is retrieval, not training.

### Guardrails { #guardrails }

Input and output checks (classifiers, rules, schemas) placed around the model.

**Why it matters:** Catches bad inputs and bad outputs the model itself might let through.

<small>*Index aliases:* Guardrail</small>

### Prompt injection { #prompt-injection }

An attack where untrusted content (a web page, an email, a document) contains instructions the model wrongly follows.

**Why it matters:** The top security risk for agents: anything the model reads can try to give it orders.

### LLM-as-a-judge { #llm-as-a-judge }

Using a strong model to grade another model's outputs at scale.

**Why it matters:** Makes evaluation cheap enough to run on every change, like unit tests for prompts.

<small>*Index aliases:* LaaJ, Judge model</small>

### Orchestration frameworks { #orchestration-frameworks }

*Also known as:* LangChain, LlamaIndex, Spring AI, Semantic Kernel, Agent SDKs

Libraries wiring prompts, tools, retrieval and agents together.

**Why it matters:** Save boilerplate; the concepts underneath are the ones in this section.

<small>*Index aliases:* LangChain / LlamaIndex</small>

### Observability / tracing { #observability-tracing }

*Also known as:* LangSmith, Langfuse, OpenTelemetry

Logging prompts, tool calls, tokens, cost and latency per request.

**Why it matters:** You cannot improve an LLM app you cannot see; tracing shows why a given answer went wrong.

<small>*Index aliases:* LangSmith / Langfuse</small>

### Hallucination ★ { #hallucination }

Confident, fluent, wrong output.

**Why it matters:** The model is predicting plausible text, not checking facts. RAG, tools and grounding reduce it; nothing eliminates it.

### Token pricing { #token-pricing }

APIs bill per input token and per output token. Output tokens cost more; cached input tokens cost less.

**Why it matters:** Why prompt length, answer length and caching are the three cost levers.
