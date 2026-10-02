from src.vectorstore import load_vectorstore
from src.prompts import ACADEMIC_PROMPT
from config import get_llm


def get_retriever():
    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )


def retrieve_documents(question):
    retriever = get_retriever()

    return retriever.invoke(question)


def format_documents(documents):
    formatted = []

    for document in documents:

        source = document.metadata.get(
            "source_file",
            "Unknown"
        )

        page = document.metadata.get(
            "page",
            "Unknown"
        )

        formatted.append(
            f"Source: {source}\n"
            f"Page: {page}\n"
            f"{document.page_content}"
        )

    return "\n\n".join(formatted)


def extract_text(content):

    if isinstance(content, str):
        return content

    if isinstance(content, list):

        text_parts = []

        for item in content:

            if isinstance(item, dict):

                if item.get("type") == "text":

                    text_parts.append(
                        item.get("text", "")
                    )

            else:

                text_parts.append(
                    str(item)
                )

        return "\n".join(text_parts)

    return str(content)


def answer_question(question):

    documents = retrieve_documents(question)

    context = format_documents(documents)

    prompt = ACADEMIC_PROMPT.invoke(
        {
            "context": context,
            "question": question
        }
    )

    llm = get_llm()

    response = llm.invoke(prompt)

    answer = extract_text(
        response.content
    )

    sources = []

    for document in documents:

        source = document.metadata.get(
            "source_file",
            "Unknown"
        )

        if source not in sources:
            sources.append(source)

    return {
        "answer": answer,
        "sources": sources,
        "documents": documents
    }