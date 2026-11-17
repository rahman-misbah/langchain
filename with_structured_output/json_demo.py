from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

Review = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Write down all the key themes discussed in the review in a list",
        },
        "summary": {"type": "string", "description": "A brief summary of the review"},
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return sentiment of the review as positive or negative",
        },
        "reviewer": {
            "type": ["string", "null"],
            "description": "name of the reviewer, if available",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}


# Load review
reviews = []
with open("../reviews.txt", "r") as f:
    text = f.read()
    text = text.split("---")

    for review in text:
        reviews.append(review.strip())

# Create structured output model
structured_model = model.with_structured_output(Review)

# Invoke and fetch result
result = structured_model.invoke(reviews[1])
print(result)
print(type(result))
