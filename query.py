import faiss
import pickle
import requests
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("vector_store.index")

# Load documents
with open("documents.pkl", "rb") as f:
    documents = pickle.load(f)

query = input("Ask a question: ")

# Convert query to embedding
query_embedding = model.encode([query])

# Search similar docs
D, I = index.search(query_embedding, k=2)

context = "\n".join([documents[i] for i in I[0]])

prompt = f"""
Answer the question based on the context.

Context:
{context}

Question:
{query}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    }
)

print("\nAnswer:\n")
print(response.json()["response"])
