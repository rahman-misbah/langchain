from typing import Annotated

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
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


# Output Schema
class Person(BaseModel):
    name: Annotated[str, Field(description="Name of the person")]
    age: Annotated[int, Field(description="Age of the person", gt=18)]
    city: Annotated[str, Field(description="City the person belongs to")]


pydantic_parser = PydanticOutputParser(pydantic_object=Person)

# Prompt
prompt_template = PromptTemplate(
    template="Generate data of a random person strictly following the specified schema:\n{format_instructions}",
    partial_variables={
        "format_instructions": pydantic_parser.get_format_instructions()
    },
)

# Main
chain = prompt_template | model | pydantic_parser

result = chain.invoke({})

print(result)
print(type(result))
