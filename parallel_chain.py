from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import BitsAndBytesConfig

# Load env file
load_dotenv()

# Load models
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True, bnb_4bit_compute_dtype="float16", bnb_4bit_quant_type="nf4"
)

llm = HuggingFacePipeline.from_model_id(
    model_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    pipeline_kwargs={"return_full_text": False, "max_new_tokens": 2048},
    model_kwargs={
        "quantization_config": quantization_config,
    },
)

model = ChatHuggingFace(llm=llm)

# Prompts
notes_template = PromptTemplate(
    template="Create notes based on the following text:\n{text}"
)

quiz_template = PromptTemplate(
    template="Generate a 5 question MCQ quiz based on the following text:\n{text}"
)

merge_template = PromptTemplate.from_template(
    "Merge the attached notes and quiz in a single document as they come. Do not modify or add anything to it."
    "Copy word for word. Output only the combined document, starting with '# Study Material\n\n"
    "Notes:\n{notes}\n\n"
    "Quiz:\n{quiz}"
)

# Chains
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "notes": notes_template | model | parser,
        "quiz": quiz_template | model | parser,
    }
)

chain = parallel_chain | merge_template | model | parser


# Invoke
with open("sample_text.txt", "r") as f:
    text = f.read()

result = chain.invoke({"text": text})

with open("parallel_result.txt", "w") as f:
    f.write(result)

chain.get_graph().print_ascii()
