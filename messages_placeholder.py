from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create template
chat_template = ChatPromptTemplate(
    [
        ("system", "you are an expert assistant for {company}"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{query}"),
    ]
)

# Load history
history = []

with open("sample_chat_history.txt", "r") as f:
    while line := f.readline():
        line = line.split(":")
        role = line[0].strip()
        message = line[1].strip()

        history.append((role, message))

# Define other variables
company = "Amazon"
query = "What is the status of my refund?"

# Generate the final prompt
prompt = chat_template.invoke({"company": company, "history": history, "query": query})

# Final preview
print(prompt)
