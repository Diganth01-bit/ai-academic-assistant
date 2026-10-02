from config import get_llm


llm = get_llm()

response = llm.invoke(
    "Explain RAG in one sentence."
)

print(response.content)