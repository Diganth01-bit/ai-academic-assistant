import os

from langchain_community.vectorstores import FAISS

from src.ingest import (
    load_documents,
    split_documents
)

from src.embeddings import (
    get_embeddings
)


VECTOR_DB_PATH = "vector_db"


def create_vectorstore():

    print("Loading college documents...")

    documents = load_documents()

    print("Splitting documents...")

    chunks = split_documents(
        documents
    )

    print("Creating embeddings...")

    embeddings = get_embeddings()

    print("Creating FAISS vector database...")

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(
        VECTOR_DB_PATH
    )

    print(
        "FAISS vector database created."
    )


def load_vectorstore():

    if not os.path.exists(
        VECTOR_DB_PATH
    ):

        raise FileNotFoundError(
            "Vector database not found. "
            "Run vectorstore.py first."
        )

    embeddings = get_embeddings()

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


if __name__ == "__main__":

    create_vectorstore()