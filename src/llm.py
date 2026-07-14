from langchain_groq import ChatGroq

from config import GROQ_API_KEY, LLM_MODEL
from dotenv import load_dotenv

load_dotenv()


class LLMModel:
    """
    Creates the Groq LLM instance.
    """

    @staticmethod
    def get_llm() -> ChatGroq:

        if not GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY not found. Add it in your environment or in Streamlit secrets."
            )

        return ChatGroq(
            model=LLM_MODEL,
            temperature=0,
            max_tokens=1024,
            api_key=GROQ_API_KEY
        )
