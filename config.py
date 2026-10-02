import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()


def get_llm():
    model_name = os.getenv("OLLAMA_MODEL", "qwen3:8b")

    return ChatOllama(
        model=model_name,
        temperature=0
    )