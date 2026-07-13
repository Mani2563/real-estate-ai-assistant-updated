from pathlib import Path

from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
    DirectoryLoader,
    Docx2txtLoader,
    TextLoader,
    BSHTMLLoader,
)

from config import DATA_DIR


class DocumentLoader:
    """
    Loads all supported document types
    from the knowledge base.
    """

    def __init__(self):
        self.data_dir = DATA_DIR

    def load_pdf_documents(self) -> list[Document]:
        loader = PyPDFDirectoryLoader(
            str(self.data_dir / "pdf")
        )
        return loader.load()


    def load_docx_documents(self) -> list[Document]:
        loader = DirectoryLoader(
            str(self.data_dir / "docx"),
            glob="**/*.docx",
            loader_cls=Docx2txtLoader,
        )
        return loader.load()

    def load_html_documents(self) -> list[Document]:
        loader = DirectoryLoader(
            str(self.data_dir / "html"),
            glob="**/*.html",
            loader_cls=BSHTMLLoader,
        )
        return loader.load()

    def load_markdown_documents(self) -> list[Document]:
        loader = DirectoryLoader(
            str(self.data_dir / "markdown"),
            glob="**/*.md",
            loader_cls=TextLoader,
        )
        return loader.load()

    def load_all_documents(self) -> list[Document]:
        documents = []

        documents.extend(self.load_pdf_documents())
        documents.extend(self.load_docx_documents())
        documents.extend(self.load_html_documents())
        documents.extend(self.load_markdown_documents())

        return documents