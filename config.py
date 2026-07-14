from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------
# Project Paths
# -----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
VECTOR_STORE_DIR = BASE_DIR / "store" / "faiss"

# -----------------------------------------------------
# Chunking
# -----------------------------------------------------

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# -----------------------------------------------------
# Retrieval
# -----------------------------------------------------

TOP_K = 4

# -----------------------------------------------------
# Models
# -----------------------------------------------------

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_MODEL = "llama-3.3-70b-versatile"

# -----------------------------------------------------
# API Keys
# -----------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or os.getenv("groq_api_key")


def _get_streamlit_secret():
    try:
        import streamlit as st

        for key in ("GROQ_API_KEY", "groq_api_key", "api_key"):
            if key in st.secrets:
                return st.secrets[key]
    except Exception:
        return None

    return None


if not GROQ_API_KEY:
    GROQ_API_KEY = _get_streamlit_secret()
