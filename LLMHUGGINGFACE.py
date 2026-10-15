from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-360M-Instruct"
)

result = generator(
    "Tell me about IIIT NAGPUR.",
    max_new_tokens=100,
    do_sample=False
)

print(result[0]["generated_text"])