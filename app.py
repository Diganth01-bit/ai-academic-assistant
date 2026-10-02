import streamlit as st

from src.graph import build_graph
from src.planner import generate_study_plan


st.set_page_config(
    page_title="NMAMIT Academic Assistant",
    page_icon="🎓",
    layout="wide"
)


st.title(
    "🎓 NMAMIT Academic Assistant"
)

st.caption(
    "AI-powered academic assistant "
    "using Ollama + RAG + LangChain + LangGraph"
)


if "messages" not in st.session_state:

    st.session_state.messages = []


with st.sidebar:

    st.header(
        "📚 Academic Assistant"
    )

    page = st.radio(
        "Select a feature",
        [
            "Academic Assistant",
            "Study Planner"
        ]
    )


if page == "Academic Assistant":

    st.subheader(
        "Ask your academic question"
    )


    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


    question = st.chat_input(
        "Ask about academics, regulations, exams..."
    )


    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message("user"):

            st.markdown(question)


        with st.chat_message("assistant"):

            with st.spinner(
                "Searching college knowledge base..."
            ):

                graph = build_graph()

                result = graph.invoke(
                    {
                        "question": question,
                        "intent": "",
                        "context": "",
                        "answer": "",
                        "sources": []
                    }
                )


            answer = result["answer"]

            st.markdown(answer)


            sources = result.get(
                "sources",
                []
            )


            if sources:

                st.markdown(
                    "### 📚 Sources"
                )

                for source in sources:

                    st.write(
                        f"📄 {source}"
                    )


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


else:

    st.subheader(
        "📅 Personalized Study Planner"
    )


    subjects_text = st.text_area(
        "Subjects",
        "DBMS, DAA, Operating Systems, Computer Networks"
    )


    exam_date = st.date_input(
        "Examination Date"
    )


    hours = st.number_input(
        "Available study hours per day",
        min_value=1,
        max_value=12,
        value=3
    )


    if st.button(
        "Generate Study Plan"
    ):

        subjects = [
            subject.strip()
            for subject in subjects_text.split(",")
            if subject.strip()
        ]


        plan = generate_study_plan(
            subjects,
            exam_date,
            hours
        )


        st.success(
            "Study plan generated!"
        )


        st.text(plan)