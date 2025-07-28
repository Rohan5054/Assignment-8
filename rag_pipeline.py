from sentence_transformers import SentenceTransformer
import chromadb
import json

model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("loan_rag")

with open("qa_data.json") as f:
    data = json.load(f)

for qa in data:
    vec = model.encode(qa["question"] + " " + qa["context"]).tolist()
    collection.add(documents=[qa["context"]], embeddings=[vec], metadatas=[{"question": qa["question"], "answer": qa["response"]}])

def get_context(query):
    vec = model.encode(query).tolist()
    result = collection.query(query_embeddings=[vec], n_results=2)
    return result["documents"][0][0] if result["documents"] else "No relevant info found"
