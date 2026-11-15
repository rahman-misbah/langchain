from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me about Virat Kohli"

document_embeddings = model.embed_documents(documents)
query_embedding = model.embed_query(query)

scores = cosine_similarity([query_embedding], document_embeddings)[0]      # Takes 2D lists as input, with query as first argument. Returns a 2D list.
doc_index, similarity_score = sorted(list(enumerate(scores)), reverse=True, key=lambda x: x[1])[0]

print("*" * 30)
print("User Query:", query)
print("Answer:", documents[doc_index])
print("Similarity Score:", similarity_score)