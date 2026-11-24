# Generate a detailed report on a topic
# Then generate a summary based on the report

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    provider="featherless-ai"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Hello HuggingFace!")
print(result.text)

# 1st Prompt -> Detailed Report


# 2nd Prompt -> Summary