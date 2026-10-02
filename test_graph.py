from src.graph import build_graph


graph = build_graph()


question = input(
    "Ask your college question: "
)


result = graph.invoke(
    {
        "question": question,
        "intent": "",
        "context": "",
        "answer": "",
        "sources": []
    }
)


print("\n")
print("=" * 60)
print("FINAL ANSWER")
print("=" * 60)

print(result["answer"])


print("\n")
print("=" * 60)
print("SOURCES")
print("=" * 60)

for source in result.get(
    "sources",
    []
):

    print("-", source)