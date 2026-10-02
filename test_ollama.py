from config import get_llm

print("Loading Ollama model...")

llm = get_llm()

response = llm.invoke("Explain DBMS in simple words.")

print("\nANSWER:")
print(response.content)