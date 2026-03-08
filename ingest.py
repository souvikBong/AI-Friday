import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
doc_folder = "documents"

for file in os.listdir(doc_folder):
    with open(os.path.join(doc_folder, file), "r", encoding="utf-8") as f:
        documents.append(f.read())

# Create embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "vector_store.index")

# Save documents
with open("documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Documents indexed successfully!")
