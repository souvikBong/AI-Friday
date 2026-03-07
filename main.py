from knowledge.knowledge_store import KnowledgeStore
from rag.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from rag.rag_pipeline import RAGPipeline
from llm.llm_client import LLMClient


def main():

    knowledge_store = KnowledgeStore()

    retriever = Retriever(knowledge_store)
    prompt_builder = PromptBuilder()
    llm_client = LLMClient()

    rag = RAGPipeline(retriever, prompt_builder, llm_client)

    while True:
        query = input("User: ")

        response = rag.run(query)

        print("Bot:", response)


if __name__ == "__main__":
    main()
