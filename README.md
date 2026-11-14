# 🚀 GenAI Journey: My Learning & Development Lab

[![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-amber?style=for-the-badge&logo=git)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)]()
[![LangChain](https://img.shields.io/badge/Framework-LangChain-1C3C3C?style=for-the-badge&logo=chainlink)]()
[![Purpose](https://img.shields.io/badge/Purpose-Self%20Learning%20%26%20Practice-success?style=for-the-badge)]()

> ⚠️ **Under Active Development (Work in Progress)**  
> This repository is my personal hands-on laboratory for exploring, practicing, and mastering **Generative AI** engineering. I have not finished yet — new concepts, code experiments, and architectural patterns are continuously being added as I learn!

---

## 📌 Main Purpose of this Repository

The goal of this repository is to document my journey from foundational concepts to advanced practical architectures in GenAI application development. 

Instead of just following tutorials, this space is dedicated to:
- 🧪 **Hands-on Experimentation**: Writing and breaking down code from scratch to understand internal mechanics.
- 🧱 **Building Reusable Patterns**: Mastering core primitives like models, prompts, LCEL chains, structured outputs, and parsers.
- 📚 **Personal Reference**: Serving as a personal knowledge base and code catalog for real-world projects down the road.

---

## 📂 Repository Structure & What's Covered

Here is an overview of the core concepts practiced across the repository:

| Module / Directory | Focus Area | Key Concepts Covered |
| :--- | :--- | :--- |
| **[`langchain-models`](./langchain-models)** | Model Foundations | LLMs, Chat Models (Google Gemini, OpenAI, Anthropic, HuggingFace API/Local), and Text Embedding Models. |
| **[`langchain_promt`](./langchain_promt)** | Prompt Engineering | `PromptTemplate`, `ChatPromptTemplate`, message roles (`System`, `Human`, `AIMessage`), dynamic template generation, and interactive chat UIs. |
| **[`langchain_chain`](./langchain_chain)** | Chains & Workflows | Simple Chains, Sequential Chains, Parallel Execution, and Conditional Routing using LCEL. |
| **[`output_parsers.py`](./output_parsers.py)** | Output Parsing | Extracting structured responses via `StrOutputParser`, `JsonOutputParser`, `PydanticOutputParser`, and `StructuredOutputParser`. |
| **[`langchain-structured-output`](./langchain-structured-output)** | Structured Outputs | Enforcing strict JSON schema, Pydantic models, and TypedDict schemas with modern LLM capabilities. |

---

## 🗺️ Learning Roadmap

This journey is actively in progress. Below is the roadmap of topics currently being tackled and what's coming up next:

- [x] **Foundations**: LLMs vs. Chat Models & Embedding generation
- [x] **Prompt Engineering**: Templates, placeholders, and memory management
- [x] **Output Parsers**: Extracting reliable JSON, Pydantic, and text formats
- [x] **Chains (LCEL)**: Sequential, parallel, and branch logic
- [ ] **RAG (Retrieval-Augmented Generation)**: Vector stores (Chroma, Pinecone, FAISS), document chunking, and semantic search
- [ ] **Agentic AI & Tools**: ReAct agents, tool calling, and autonomous workflows
- [ ] **LangGraph & State Management**: Multi-actor graphs, human-in-the-loop, cyclical workflows
- [ ] **Evaluation & Monitoring**: Tracing and testing LLM outputs (LangSmith, Ragas)

---

## 🛠️ Getting Started Locally

If you'd like to run any of the experiments locally:

### 1. Clone the repository
```bash
git clone https://github.com/sujitkr268/GENAI_JOURNEY.git
cd GENAI_JOURNEY
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r langchain-models/requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the relevant subfolder (or root) and provide your API keys:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

*(All `.env` files are ignored by git to protect credentials).*

---

## 📝 Disclaimer

This is a **personal learning repository**. Code here reflects active experiments, architectural drafts, and iterations. Feel free to explore, take inspiration, or share feedback!
