# Agentic RAG Chatbot

Chat with your documents (PDF, DOCX, TXT) using Retrieval-Augmented Generation, FAISS, and Hugging Face models.

## 🚀 Features

- 📄 Supports multiple document formats
- 🔍 Semantic search using FAISS + Sentence Transformers
- 🤖 Lightweight Hugging Face LLM (Flan-T5-small)
- 🌐 Optional web search fallback (DuckDuckGo)
- 💬 Multi-turn conversation with memory
- 📦 Streamlit UI with chat + document preview

## 🧰 Tech Stack

| Layer      | Tool |
|------------|------|
| UI         | Streamlit |
| RAG        | FAISS + Sentence Transformers |
| LLM        | google/flan-t5-small |
| MCP        | JSON-style agent messages |
| Lang       | Python |
| Others     | PyMuPDF, docx, torch |

## 🧱 How to Run

```bash
pip install -r requirements.txt
python -m streamlit run app.py
