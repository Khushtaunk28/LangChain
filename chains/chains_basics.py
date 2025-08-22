from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()
model=GoogleGenerativeAI(model="gemini-2.5-flash")
# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

#create a chain

chain=prompt_template | model | StrOutputParser()
# Run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Output
print(result)