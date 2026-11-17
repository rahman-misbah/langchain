from typing import Annotated, Literal

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# Schema
class Review(BaseModel):
    key_themes: Annotated[list[str], Field(description="Write the list of key themes")]
    summary: Annotated[str, Field(description="A brief summary of the review")]
    sentiment: Annotated[
        Literal["pos", "neg"], Field(description="Return the sentiment of the review")
    ]
    reviewer: Annotated[
        str | None, Field(description="Name of the reviewer if available")
    ] = None


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
