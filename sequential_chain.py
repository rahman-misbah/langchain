from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import BitsAndBytesConfig

# Load environment variables
load_dotenv()

# Load model
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True, bnb_4bit_compute_dtype="float16", bnb_4bit_quant_type="nf4"
)

llm = HuggingFacePipeline.from_model_id(
    model_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    model_kwargs={
        "quantization_config": quantization_config,
    },
)

model = ChatHuggingFace(llm=llm)


# Supporting functions
def trim_response(response: str):
    response = response.split("<|assistant|>")[-1]
    return response.strip()


# Prompts
report_prompt = PromptTemplate(
    template="Generate a detailed report on the topic {topic}"
)

summary_prompt = PromptTemplate(
    template="Generate a summary based on the the following report\n{report}"
)

# Test model
str_parser = StrOutputParser()
process_response = RunnableLambda(trim_response)

chain = (
    report_prompt
    | model
    | str_parser
    | process_response
    | summary_prompt
    | model
    | str_parser
    | process_response
)

result = chain.invoke({"topic": "GPUs"})

print(result)

# chain.get_graph().print_ascii()
