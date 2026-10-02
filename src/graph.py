from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END

from src.rag import (
    retrieve_documents,
    format_documents,
    extract_text
)

from src.prompts import (
    ACADEMIC_PROMPT,
    REVIEW_PROMPT
)

from config import get_llm


class AssistantState(TypedDict):

    question: str

    intent: str

    context: str

    answer: str

    sources: List[str]


def analyze_question(state):

    question = state["question"].lower()

    study_keywords = [
        "study plan",
        "study schedule",
        "timetable",
        "prepare for exam",
        "study planner"
    ]

    if any(
        keyword in question
        for keyword in study_keywords
    ):

        intent = "study_plan"

    else:

        intent = "academic"

    return {
        "intent": intent
    }


def retrieve_information(state):

    documents = retrieve_documents(
        state["question"]
    )

    context = format_documents(
        documents
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
        "context": context,
        "sources": sources
    }


def generate_response(state):

    prompt = ACADEMIC_PROMPT.invoke(
        {
            "context": state["context"],
            "question": state["question"]
        }
    )

    llm = get_llm()

    response = llm.invoke(prompt)

    answer = extract_text(
        response.content
    )

    return {
        "answer": answer
    }


def review_response(state):

    prompt = REVIEW_PROMPT.invoke(
        {
            "question": state["question"],
            "context": state["context"],
            "answer": state["answer"]
        }
    )

    llm = get_llm()

    review = llm.invoke(prompt)

    review_content = review.content

    if isinstance(
        review_content,
        list
    ):

        review_text = " ".join(
            str(item)
            for item in review_content
        )

    else:

        review_text = str(
            review_content
        )

    if "UNSUPPORTED" in review_text.upper():

        return {
            "answer":
            "I could not find enough reliable information "
            "in the college knowledge base to answer this question."
        }

    return {}


def build_graph():

    graph = StateGraph(
        AssistantState
    )

    graph.add_node(
        "question_analysis",
        analyze_question
    )

    graph.add_node(
        "information_retrieval",
        retrieve_information
    )

    graph.add_node(
        "response_generation",
        generate_response
    )

    graph.add_node(
        "response_review",
        review_response
    )

    graph.add_edge(
        START,
        "question_analysis"
    )

    graph.add_edge(
        "question_analysis",
        "information_retrieval"
    )

    graph.add_edge(
        "information_retrieval",
        "response_generation"
    )

    graph.add_edge(
        "response_generation",
        "response_review"
    )

    graph.add_edge(
        "response_review",
        END
    )

    return graph.compile()