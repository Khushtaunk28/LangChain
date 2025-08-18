from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from dotenv import load_dotenv
load_dotenv()

#setup firebase
PROJECT_ID="langchaintutorial-26614"
SESSION_ID="user_session_new"
COLLECTION_NAME="chat_history"

#initialize firestore client
print("Initialising firestore client")
client=firestore.Client(project=PROJECT_ID)

#initialize firestore chat msg history
print("iniitial chat msg history")
chat_history=FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

#initialise the chat model
model=GoogleGenerativeAI(model="gemini-2.5-flash")
print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response)

    print(f"AI: {ai_response}")



