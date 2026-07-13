from langchain_groq import ChatGroq

from config import LLM_MODEL
from dotenv import load_dotenv

load_dotenv()


class LLMModel:
    """
    Creates the Groq LLM instance.
    """

    @staticmethod
    def get_llm() -> ChatGroq:

        return ChatGroq(
            model=LLM_MODEL,
            temperature=0,
            max_tokens=1024
        )