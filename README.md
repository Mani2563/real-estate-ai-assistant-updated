# Real Estate AI Assistant - RAG System

## Overview
Intelligent AI-powered assistant that answers real estate queries using Retrieval-Augmented Generation (RAG) with a Streamlit web interface.

---

## Requirements
- Python 3.9+
- Groq API Key (free at https://console.groq.com)

---

## Installation

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create `.env` file in root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

---

## Build Knowledge Base (First Time Only)

```bash
python -m src.ingest
```

This creates FAISS vector index from documents in `/data` folder.

---

## Run Application

```bash
streamlit run app.py
```

Access at: `http://localhost:8501`

---

## Features

✅ **User Authentication** - Simple login/signup with password validation  
✅ **RAG-Powered Chat** - Answers from real estate knowledge base  
✅ **Multi-Turn Memory** - Maintains conversation context  
✅ **Source Citations** - Shows document references for every answer  
✅ **Irrelevance Handling** - Gracefully rejects off-topic questions  
✅ **Dynamic Password Validation** - Real-time feedback on signup  

---

## Project Structure

```
├── app.py                    # Streamlit UI
├── config.py                 # Configuration
├── src/
│   ├── rag_chain.py         # RAG pipeline
│   ├── retriever.py         # Document retrieval
│   ├── vector_store.py      # FAISS vector DB
│   ├── llm.py               # Groq LLM
│   ├── embeddings.py        # BGE embeddings
│   ├── auth.py              # Authentication
│   ├── memory.py            # Conversation memory
│   ├── loaders.py           # Document loading
│   ├── splitter.py          # Text chunking
│   ├── metadata.py          # Metadata handling
│   └── ingest.py            # Knowledge base ingestion
├── data/                     # Knowledge base (PDF, DOCX, HTML, Markdown)
└── store/
    └── faiss/               # Vector index
```

---

## Knowledge Base Details

**Documents:** 92 documents across multiple categories
- Project Brochures (PDF)
- Builder Profiles (PDF)
- Property Listings (HTML)
- Amenities & Location Guides (Markdown)
- Legal Documents (DOCX)
- Policies & Terms (HTML/DOCX)

**Embedding Model:** BAAI/bge-small-en-v1.5 (HuggingFace)  
**Vector Database:** FAISS  
**LLM:** Llama 3.3 70B (via Groq)  
**Similarity Threshold:** 0.5 (Cosine similarity)

---

## Test the System

### Sample Questions
- "Tell me about Horizon Business Park"
- "What is the payment plan?"
- "Show project amenities"
- "What is the cancellation policy?"
- "Compare available projects"

---

## Deployment

Deploy to any platform (Streamlit Cloud, Heroku, Railway, Render, etc.)

**Requirements for deployment:**
- Set `GROQ_API_KEY` environment variable
- Ensure `/data` and `/store` folders are included
- Use Python 3.9+

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** LangChain, Groq
- **Embeddings:** HuggingFace (BAAI/bge-small-en-v1.5)
- **Vector DB:** FAISS
- **Document Processing:** PyPDF, Docx2txt, BeautifulSoup4

---

## Support

For issues or questions, refer to:
- [Streamlit Docs](https://docs.streamlit.io)
- [LangChain Docs](https://python.langchain.com)
- [Groq API](https://console.groq.com/docs)


