from typing import Annotated

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    provider="featherless-ai",
)

model = ChatHuggingFace(llm=llm)


class TopicFacts(BaseModel):
    fact_1: Annotated[str, Field(description="First fact about the topic")]
    fact_2: Annotated[str, Field(description="Second fact about the topic")]
    fact_3: Annotated[str, Field(description="Third fact about the topic")]


json_parser = JsonOutputParser(pydantic_object=TopicFacts)

prompt_template = PromptTemplate(
    template="Tell me facts about the topic {topic}.\n{format_instructions}",
    partial_variables={"format_instructions": json_parser.get_format_instructions()},
)

chain = prompt_template | model | json_parser
result = chain.invoke({"topic": "GPU"})

print(type(result))

for fact in result.values():
    print(fact)
