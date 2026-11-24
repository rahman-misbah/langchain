from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import AutoTokenizer, StoppingCriteriaList, StopStringCriteria

# Preparing model
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id)

STOP_STRINGS = ["\nuser", "<|user|>"]

llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation",
    pipeline_kwargs={
        "do_sample": True,
        "temperature": 0.3,
        "return_full_text": False,
        "eos_token_id": tokenizer.eos_token_id,
        "pad_token_id": tokenizer.eos_token_id,
        "repetition_penalty": 1.1,
        "stopping_criteria": StoppingCriteriaList(
            [StopStringCriteria(tokenizer=tokenizer, stop_strings=STOP_STRINGS)]
        ),
    },
)

SYSTEM_PROMPT = (
    "You are a helpful assistant. Answer only the user's question. "
    "Match the length of your reply to the request: a greeting or simple "
    "question gets one or two sentences; a request for an essay, story, or "
    "detailed explanation gets a full, detailed answer. "
    "Do not invent details about the user or continue the conversation "
    "on their behalf. Stop once the question is answered."
)

base_prompt = ChatPromptTemplate.from_messages(
    [("system", SYSTEM_PROMPT), ("human", "{input}")],
)


def trim_stop(text: str) -> str:
    for s in STOP_STRINGS:
        text = text.split(s)[0]
    return text.strip()


model = (
    base_prompt
    | ChatHuggingFace(llm=llm)
    | StrOutputParser()
    | RunnableLambda(trim_stop)
)
