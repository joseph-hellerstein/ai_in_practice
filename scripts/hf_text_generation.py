'''Text generation'''
from transformers import pipeline  #  type: ignore

generator = pipeline("text-generation",
        model="HuggingFaceTB/SmolLM2-360M")
result = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print(result)