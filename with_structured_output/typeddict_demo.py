from typing import Annotated, Literal, Optional, TypedDict

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# Define output schema
class Review(TypedDict):
    summary: str
    sentiment: str


# Annotated schema
class AnnotatedReview(TypedDict):
    key_themes: Annotated[
        Optional[list[str]], "Write down all key themes discussed in a list"
    ]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return the sentiment of the review"]


# Load review
reviews = []
with open("../reviews.txt", "r") as f:
    text = f.read()
    text = text.split("---")

    for review in text:
        reviews.append(review.strip())

# Create structured output model
structured_model = model.with_structured_output(AnnotatedReview)

# Invoke and fetch result
result = structured_model.invoke(reviews[1])
print(result)
