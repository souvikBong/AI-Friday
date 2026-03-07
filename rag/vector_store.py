import faiss
import numpy as np


class VectorStore:

    def __init__(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

    def search(self, query_vector, k=2):

        distances, indices = self.index.search(query_vector, k)

        return indices[0]
