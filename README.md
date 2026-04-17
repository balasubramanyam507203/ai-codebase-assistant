# 🚀 AI Codebase Assistant

An intelligent AI-powered tool that helps developers understand, analyze, and debug codebases using **LangChain, RAG, and Agents**.

---

## 📌 Features

- 🔍 Explain any pasted code snippet
- 📁 Ask questions about an entire codebase (RAG)
- 🐞 Detect bugs, risks, and bad practices
- 🤖 Agent-based tool selection (dynamic decision making)
- 📚 Source-aware answers using vector search

---

## 🧠 Concepts Covered

This project is built in layers to demonstrate core GenAI concepts:

### 1. LLM Integration
- Direct interaction with OpenAI model

### 2. LangChain
- Prompt templates
- Chains for structured execution

### 3. RAG (Retrieval-Augmented Generation)
- Codebase indexing
- Chunking and embeddings
- Vector search using FAISS
- Context-based answering

### 4. Agents
- Tool-based execution
- Dynamic decision-making
- Automatic routing between:
  - code explanation
  - codebase search
  - bug detection

### 5. MCP (Model Context Protocol)
- Demonstrates how tools can be exposed externally
- Future integration for:
  - GitHub repositories
  - Documentation systems
  - External APIs

---

## 🏗️ Tech Stack

- Python
- Streamlit (Frontend)
- LangChain
- OpenAI API
- FAISS (Vector Database)
- python-dotenv

---

## 📂 Project Structure


ai-codebase-assistant/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│ └── sample_codebase/
│
├── src/
│ ├── llm.py
│ ├── ingest.py
│ ├── retriever.py
│ ├── rag_chain.py
│ ├── tools.py
│ ├── agent.py
│ └── mcp_notes.md
│
└── vectorstore/


---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-codebase-assistant.git
cd ai-codebase-assistant
2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Add API key

Create a .env file:

OPENAI_API_KEY=your_api_key_here
▶️ Run the App
streamlit run app.py

🧪 Sample Questions
Explain Code
Explain this code clearly
Codebase Questions (RAG)
Where is login logic defined?
How does authentication work?
Which file contains addition logic?
Bug Detection
Find possible bugs in this code

🚀 Future Improvements

GitHub integration via MCP
Multi-file dependency analysis
Better UI (React frontend)
Code visualization
Security vulnerability scanning

🎯 Key Takeaway

This project demonstrates how modern AI systems are built using:

Retrieval (RAG)
Reasoning (LLMs)
Decision-making (Agents)
Extensibility (MCP)

👨‍💻 Author

Bala Subramanyam Pallapothu