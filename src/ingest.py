import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


DATA_FOLDER = "data"


def load_documents():

    documents = []

    if not os.path.exists(DATA_FOLDER):

        raise FileNotFoundError(
            "data folder does not exist."
        )

    files = os.listdir(DATA_FOLDER)

    pdf_files = [
        file
        for file in files
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:

        raise FileNotFoundError(
            "No PDF files found inside data folder."
        )

    for filename in pdf_files:

        path = os.path.join(
            DATA_FOLDER,
            filename
        )

        print(f"Loading: {filename}")

        loader = PyPDFLoader(path)

        docs = loader.load()

        for doc in docs:

            doc.metadata["source_file"] = filename
            doc.metadata["college"] = "NMAMIT"

        documents.extend(docs)

    print(
        f"Total pages loaded: {len(documents)}"
    )

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    print(
        f"Total chunks created: {len(chunks)}"
    )

    return chunks


if __name__ == "__main__":

    documents = load_documents()

    chunks = split_documents(
        documents
    )