from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

#prompt = ChatPromptTemplate.from_messages([
#    ("system", "You are a world class digital marketer."),
#    ("user", "{input}")
#])

model = OllamaLLM(model="llama2")

chain = prompt | model

response = chain.invoke({"question": "What is AWS?"})
#response = chain.invoke({"input": "Get me strategy for my online yoga classes campaign"})

print(response)
