<div align="center">

# 📚 Documentation Helper
### AI-Powered Documentation Assistant using Retrieval-Augmented Generation (RAG)

Search technical documentation using natural language instead of keywords.

Built with **Python • LangChain • Pinecone • Ollama • Tavily • Streamlit**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=for-the-badge)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20Database-orange?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLMs-black?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge)

</div>

---

# 🌟 Overview

Documentation Helper is an end-to-end **Retrieval-Augmented Generation (RAG)** application that transforms documentation websites into an AI-powered conversational knowledge base.

Instead of manually searching through hundreds of documentation pages, users can simply ask questions in natural language and receive context-aware answers backed by the original documentation.

The application automatically:

- 🌐 Crawls documentation websites
- 📄 Extracts and cleans web content
- ✂️ Chunks documents intelligently
- 🧠 Generates semantic embeddings locally
- 📦 Stores vectors in Pinecone
- 🔍 Retrieves the most relevant context
- 🤖 Generates grounded answers using an LLM
- 📚 Includes source references for transparency

---

# ✨ Features

✅ Automated documentation crawling

✅ Semantic document chunking

✅ Local embedding generation using Ollama

✅ Pinecone vector database integration

✅ Similarity-based retrieval

✅ AI Agent powered question answering

✅ Source-aware responses

✅ Interactive Streamlit interface

✅ Modular and extensible architecture

---

# 🎯 Why This Project?

Traditional documentation search relies on keyword matching.

This project demonstrates how **Retrieval-Augmented Generation (RAG)** enables AI systems to understand the *meaning* of a query rather than matching exact words.

Example:

**Instead of searching**

> "agent framework memory"

You can simply ask

> "How does LangChain manage memory inside an agent?"

and receive a contextual answer with documentation references.

---

# 🏗️ System Architecture

```text
                        Documentation Website
                                  │
                                  ▼
                        Tavily Documentation Crawl
                                  │
                                  ▼
                     Extract & Clean Documentation
                                  │
                                  ▼
                 Recursive Character Text Splitter
                                  │
                                  ▼
                   Ollama Embedding Model
             (snowflake-arctic-embed2)
                                  │
                                  ▼
                     Pinecone Vector Database
                                  │
                                  ▼
                  Similarity Search (Top-K Chunks)
                                  │
                                  ▼
                  LangChain Agent + Ollama LLM
                                  │
                                  ▼
                    Streamlit Conversational UI
```

---

# ⚙️ Technology Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| Framework | LangChain |
| Vector Database | Pinecone |
| Embeddings | Ollama |
| Chat Model | Ollama |
| Web Crawling | Tavily |
| Frontend | Streamlit |
| Environment | UV |
| Prompt Orchestration | LangChain Agents |

---

# 📂 Project Structure

```text
documentation-helper/

├── backend/
│   ├── core.py
│   ├── prompts.py
│   └── ...
│
├── frontend/
│   ├── app.py
│   └── ...
│
├── ingestion.py
├── .env.example
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🚀 How It Works

## Step 1 — Crawl Documentation

The application crawls an entire documentation website.

```
Documentation Website
            │
            ▼
      Tavily Crawl
```

---

## Step 2 — Split Documents

Large pages are divided into smaller semantic chunks.

```
Large Page

↓

Chunk 1

↓

Chunk 2

↓

Chunk 3
```

---

## Step 3 — Generate Embeddings

Each chunk is converted into a dense vector representation.

```
Text

↓

Embedding Vector
```

---

## Step 4 — Store in Pinecone

Embeddings are indexed for efficient semantic retrieval.

```
Embedding

↓

Pinecone Index
```

---

## Step 5 — User Query

```
What are Deep Agents?
```

↓

Generate Query Embedding

↓

Retrieve Similar Chunks

↓

LLM generates grounded response

↓

Display answer + documentation source

---

# 💬 Example

### User

```
What are Deep Agents?
```

---

### Assistant

```
Deep Agents are autonomous AI systems capable of
reasoning, planning and using tools to accomplish
multi-step objectives.

Source:
https://python.langchain.com/...
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Shubham2900/documentation-helper.git
cd documentation-helper
```

---

## Create Virtual Environment

```bash
uv venv
```

---

## Activate Environment

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv sync
```

---

## Configure Environment Variables

Create a `.env`

```text
PINECONE_API_KEY=YOUR_API_KEY
INDEX_NAME=documentation-helper
TAVILY_API_KEY=YOUR_API_KEY
```

---

## Download Ollama Models

```bash
ollama pull snowflake-arctic-embed2
ollama pull gpt-oss:20b
```

---

## Build the Knowledge Base

```bash
uv run python ingestion.py
```

---

## Launch the Application

```bash
uv run streamlit run frontend/app.py
```

---

# 📊 Core Workflow

```text
User Question
      │
      ▼
Generate Embedding
      │
      ▼
Pinecone Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
LangChain Agent
      │
      ▼
Ollama Chat Model
      │
      ▼
Grounded Response
```

---

# 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Prompt Engineering
- AI Agents
- LangChain
- Pinecone
- Ollama
- Documentation Intelligence
- Information Retrieval
- Streamlit Development
- Python Backend Development

---

# 📈 Future Enhancements

- [ ] Hybrid Search (Keyword + Vector)
- [ ] Multi-document support
- [ ] Conversation memory
- [ ] Metadata filtering
- [ ] Streaming responses
- [ ] Source highlighting
- [ ] Docker deployment
- [ ] Authentication
- [ ] Cloud deployment
- [ ] Support multiple LLM providers

---

# 📸 Demo

### Home Screen

> Add a screenshot here

---

### Question Answering

> Add a screenshot here

---

### Knowledge Base Creation

> Add a GIF here

---

# 🤝 Acknowledgements

This project was inspired by educational content from **Eden Marco**. The implementation has been adapted and updated to work with the latest LangChain ecosystem, including current APIs for LangChain, Pinecone, Ollama, and UV.

---

# 👨‍💻 Author

**Shubham Bishnoi**

**LinkedIn**
linkedin.com/in/shubham-bishnoi-32b240163

**GitHub**
https://github.com/Shubham2900

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>