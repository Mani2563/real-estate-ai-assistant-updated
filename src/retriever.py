from langchain_core.documents import Document

from src.vector_store import VectorStore


class Retriever:

    def __init__(self):

        vector_store = VectorStore().load()

        self.retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 4,
                "score_threshold": 0.4
            }
        )

    def retrieve(
        self,
        query: str
    ) -> list[Document]:

        return self.retriever.invoke(query)