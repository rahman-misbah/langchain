from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

chat_template = ChatPromptTemplate(
    [
        ("system", "you are a {domain} expert"),
    ]
)

chat_prompt = chat_template.invoke({"domain": "computer science"})

chat_history = []
chat_history.extend(chat_prompt.to_messages())

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(user_input))

    result = model.invoke(chat_history)

    print("AI:", result.text)
    chat_history.append(AIMessage(result.text))
