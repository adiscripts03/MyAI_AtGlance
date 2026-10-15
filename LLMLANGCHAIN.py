
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

response = llm.invoke(
    "what is iiit nagpur"
)

print(response.content)
