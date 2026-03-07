import numpy as np


class Retriever:

    def __init__(self, knowledge_store, embedding_service):

        self.documents = knowledge_store.get_all_documents()

        self.embedding_service = embedding_service

        embeddings = embedding_service.embed(self.documents)

        from rag.vector_store import VectorStore

        self.vector_store = VectorStore(embeddings)

    def retrieve(self, query):

        query_vector = self.embedding_service.embed([query])

        indices = self.vector_store.search(query_vector)

        results = [self.documents[i] for i in indices]

        return results
