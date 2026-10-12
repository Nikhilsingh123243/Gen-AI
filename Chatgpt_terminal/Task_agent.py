import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser



llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key = os.environ["GEMINI_API_KEY"],
    temperature=0
    )


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{history}")
])

chain = prompt | llm | StrOutputParser()
store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = []  # Store inside Python Memory
    return store[session_id]


'''
start


session_id = session_1
User input

do you want to continue the session
yes
no

create new session or exit

'''
session_id = 1 

print("-----START-----")
while True:
    user_input= input('''
                       Enter your query.....
                       or 
                       For exit_type => exit
                       Query => ''').lower()
    if user_input=='exit':
        print("Thank you 😊👌")
        break
    try:
        history = get_session_history(session_id) #list
        history.append({'user_query':user_input})
        response = chain.invoke({'history':history})
        print('''
              User input => {user_input}
              Response => {response}
              ''')
    except Exception as e:
        print(f"error => {e}")
        break
    new_session=input('''
                      If you want to continue the same session type anything except no => Yes
                      For new session type => No
                      ''')

    if new_session == 'no':
        session_id+=1