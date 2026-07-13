from src.loaders import DocumentLoader
from src.metadata import MetadataNormalizer
from src.splitter import DocumentSplitter
from src.vector_store import VectorStore


def main():

    print("=" * 60)
    print("Starting Knowledge Base Ingestion")
    print("=" * 60)

    # Load
    loader = DocumentLoader()
    documents = loader.load_all_documents()
    print(f"Loaded Documents : {len(documents)}")

    # Normalize Metadata
    documents = MetadataNormalizer.normalize(documents)

    # Split
    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)
    print(f"Created Chunks : {len(chunks)}")

    # Build FAISS
    vector_store = VectorStore()

    db = vector_store.create(chunks)

    vector_store.save(db)

    print("\nFAISS Index Created Successfully")
    print("Knowledge Base Ready")


if __name__ == "__main__":
    main()