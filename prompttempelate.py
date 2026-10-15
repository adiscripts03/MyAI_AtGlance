
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a witty stand-up comedian. "
        "Format your answer as 3 distinct, short punchy jokes or observations. "
        "Do NOT use markdown blockquotes ('>') or tables. Keep it clean and readable plain text."
    )),
    ("human", "Tell jokes about: {joke_topic}")
])

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3,
    max_tokens=300
)

chain = prompt | llm

topic = input("Enter ur topic which u want to joke about: ")

result = chain.invoke({
    "joke_topic": topic,
})

print(result.content)
