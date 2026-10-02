from src.rag import answer_question


question = input(
    "Ask your college question: "
)


result = answer_question(question)


print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)

print(result["answer"])


print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)


for source in result["sources"]:

    print(f"- {source}")