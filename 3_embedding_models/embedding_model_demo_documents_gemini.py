from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2", output_dimensionality=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the captial of West Bengal",
    "Paris is the captial of France"
]

result = model.embed_documents(documents)

print(str(result))