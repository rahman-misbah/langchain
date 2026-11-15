from langchain_huggingface import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}  # GPU architecture outdated    
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the captial of France"
]

query = "What is the capital of India?"

document_result = model.embed_documents(documents)
query_result = model.embed_query(query)

print(document_result)
print(query_result)