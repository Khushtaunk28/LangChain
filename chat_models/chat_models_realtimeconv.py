from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
load_dotenv()
model=GoogleGenerativeAI(model="gemini-2.5-flash")


chat_history=[] #list to store a the conv history

#initial system message
system_msg=SystemMessage(content="Help me in trading master")
chat_history.append(system_msg)

#chat loop
while True:
    query=input("You: ")
    if query.lower()=="exit": #used to end the convo
        break
    chat_history.append(HumanMessage(content=query)) #user msg
    
    #get AI response using history
    result=model.invoke(chat_history)
    response=result
    chat_history.append(AIMessage(content=response)) #adding the ai message
    
    print(f"Ai: {response}")

