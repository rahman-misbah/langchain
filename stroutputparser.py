# Parser approach
# Generate a detailed report on a topic
# Then generate a summary based on the report

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    provider="featherless-ai",
)

model = ChatHuggingFace(llm=llm)

# 1st Prompt -> Detailed Report
report_template = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd Prompt -> Summary
summary_template = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"],
)

# Output
parser = StrOutputParser()

chain = report_template | model | parser | summary_template | model | parser

result = chain.invoke({"topic": "Black Hole"})

print(result)
