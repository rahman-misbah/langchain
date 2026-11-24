from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

from offline_model import model

json_parser = JsonOutputParser()

prompt_template = PromptTemplate(
    template="Give me the name, age and city of a fictional person\n{format_instruction}",
    partial_variables={"format_instruction": json_parser.get_format_instructions()},
)

chain = prompt_template | model | json_parser
result = chain.invoke({})

print(result)
print(type(result))
