from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

llm=GoogleGenerativeAI(model="gemini-2.5-flash")
template="Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength.Keep it to 4 lines max"


prompt_temp=ChatPromptTemplate.from_template(template)

# prompt=prompt_temp.invoke({
#     "tone":"excited",
#     "company":"maersk",
#     "position":"intern",
#     "skill":"GenAi"
# })
# Example 2: Prompt with System and Human Messages (Using Tuples)
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = llm.invoke(prompt)
print(result)