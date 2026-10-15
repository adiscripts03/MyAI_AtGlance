#  AI Engineering Learning Roadmap

A structured journey to learn AI engineering, from LLM fundamentals to RAG, AI agents, LangGraph, and production deployment.

My goal is to understand the concepts behind modern AI systems and implement them using Python, Hugging Face, LangChain, LangGraph, and model APIs such as Groq.

## 🗺️ Learning Roadmap

- [x] **Phase 1: AI & LLM Fundamentals**

  - [x] AI vs Machine Learning vs Deep Learning vs Generative AI
  - [x] Large Language Models (LLMs)
  - [x] Tokens, Tokenization & Context Windows
  - [x] Inference and Model Generation
  - [x] Prompt Engineering
  - [x] System Prompts & Chat Templates
  - [x] Temperature, Top-p & Sampling

- [ ] **Phase 2: Models & Fine-Tuning**

  - [ ] Open Source vs Open-Weight Models
  - [ ] Transformers & Attention Mechanisms
  - [ ] Pretraining vs Fine-Tuning
  - [ ] SFT, LoRA, QLoRA & PEFT
  - [ ] Model Quantization

- [ ] **Phase 3: Embeddings & Vector Search**

  - [ ] Text Embeddings
  - [ ] Vector Databases & Similarity Search
  - [ ] Semantic Search, Keyword Search & Hybrid Search
  - [ ] Chunking, Retrieval & Reranking

- [ ] **Phase 4: Retrieval-Augmented Generation (RAG)**

  - [ ] Understanding RAG Architecture
  - [ ] Document Loaders & Text Splitters
  - [ ] Embedding Models & Vector Stores
  - [ ] Retriever Configuration
  - [ ] RAG Chains with LangChain
  - [ ] Source Attribution & Retrieval Evaluation

- [ ] **Phase 5: Structured Outputs & AI Agents**

  - [ ] JSON Mode & Structured Outputs
  - [ ] Function Calling & Tool Calling
  - [ ] AI Agents & Agentic Workflows
  - [ ] LangGraph: State, Nodes & Edges
  - [ ] Conditional Routing, Loops & Checkpointing
  - [ ] Short-Term Memory & Long-Term Memory

- [ ] **Phase 6: Advanced AI Concepts**

  - [ ] Multimodal AI: Vision, Audio & Text
  - [ ] Model Context Protocol (MCP)
  - [ ] Guardrails & Human-in-the-Loop
  - [ ] Hallucination Detection & Mitigation
  - [ ] Evaluation & Observability

- [ ] **Phase 7: Deployment & Production AI**

  - [ ] Model Inference Servers
  - [ ] Hosted APIs vs Local Inference
  - [ ] FastAPI for AI Applications
  - [ ] Streaming, Latency & Throughput
  - [ ] Authentication, Security & Rate Limiting
  - [ ] Monitoring, Testing & Deployment

## 🛠️ Tech Stack

| Category             | Technologies                        |
| -------------------- | ----------------------------------- |
| Language             | Python                              |
| Model Hub            | Hugging Face                        |
| Model Inference      | Groq API, Hugging Face Transformers |
| LLM Framework        | LangChain                           |
| Agent Workflows      | LangGraph                           |
| Embeddings           | Sentence Transformers               |
| Vector Search        | FAISS, Chroma                       |
| Fine-Tuning          | Transformers, PEFT, LoRA, QLoRA     |
| API Development      | FastAPI                             |
| Evaluation & Tracing | LangSmith                           |
| Protocol             | Model Context Protocol (MCP)        |

## 💻 Projects

### 1. AI Chatbot

- [ ] Connect an LLM using Groq API.
- [ ] Implement prompt templates.
- [ ] Experiment with model parameters.
- [ ] Generate structured outputs.

### 2. Chat with PDFs — RAG Application

- [ ] Load PDF documents.
- [ ] Split documents into chunks.
- [ ] Generate embeddings.
- [ ] Store embeddings in FAISS or Chroma.
- [ ] Retrieve relevant passages.
- [ ] Generate context-grounded answers.
- [ ] Add source attribution.

### 3. AI Agent with Tools

- [ ] Create custom Python tools.
- [ ] Implement tool calling.
- [ ] Build an agent using LangChain.
- [ ] Create a workflow using LangGraph.
- [ ] Add state management and checkpointing.
- [ ] Implement conditional routing.
- [ ] Add human approval for sensitive actions.

### 4. Fine-Tuning a Language Model

- [ ] Prepare a training dataset.
- [ ] Fine-tune a pretrained model using SFT.
- [ ] Experiment with LoRA or QLoRA.
- [ ] Evaluate the fine-tuned model.
- [ ] Compare it against the original model.

### 5. Deploy an AI Application

- [ ] Build a backend using FastAPI.
- [ ] Connect the model or agent.
- [ ] Add error handling and input validation.
- [ ] Implement logging and evaluation.
- [ ] Deploy the application.

## 📚 Learning Resources

- [Hugging Face Documentation](https://huggingface.co/docs)
- [Hugging Face Course](https://huggingface.co/learn)
- [LangChain Documentation](https://python.langchain.com/docs/)
- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [Groq Documentation](https://console.groq.com/docs)
- [FAISS Documentation](https://faiss.ai/)
- [Sentence Transformers Documentation](https://sbert.net/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)

## 📈 Progress Tracker

- **Current focus:** AI & LLM Fundamentals
- **Completed phases:** 0 / 7
- **Projects completed:** 0 / 5

I will update this README as I complete topics, build projects, and document what I learn.

---

⭐ *Learning by building, experimenting, and documenting — one AI concept at a time.*
