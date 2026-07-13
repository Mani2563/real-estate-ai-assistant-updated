from pathlib import Path
from langchain_core.documents import Document


class MetadataNormalizer:
    """
    Standardizes document metadata across all supported file types.
    """

    @staticmethod
    def normalize(documents: list[Document]) -> list[Document]:

        normalized_docs = []

        for document in documents:

            source_path = Path(document.metadata.get("source", ""))

            metadata = {
                "source": source_path.name,
                "file_name": source_path.stem,
                "file_type": source_path.suffix.replace(".", ""),
                "page": document.metadata.get("page", 0),
            }

            normalized_docs.append(
                Document(
                    page_content=document.page_content,
                    metadata=metadata,
                )
            )

        return normalized_docs