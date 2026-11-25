from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    provider="auto",
)

model = ChatHuggingFace(llm=llm)

prompt_template = PromptTemplate(template="Generate 5 interesting facts about {topic}")

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic": "CPUs"})
print(result)

# chain.get_graph().print_ascii()
