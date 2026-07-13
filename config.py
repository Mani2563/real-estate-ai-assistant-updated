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

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

LLM_MODEL = "llama-3.3-70b-versatile"

# -----------------------------------------------------
# API Keys
# -----------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please configure it in the .env file."
    )