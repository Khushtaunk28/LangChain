from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
llm=GoogleGenerativeAI(model="gemini-2.5-flash")
messages = [
    SystemMessage("You are an expert in social media content strategy"), 
    HumanMessage("Give a short tip to create engaging posts on Instagram"), 
]
result=llm.invoke(messages)
print(result)