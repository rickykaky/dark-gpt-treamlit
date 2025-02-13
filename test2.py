import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

if 'count' not in st.session_state:
    st.session_state['count'] = 0

@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash")


model = get_model()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", """Answer the user's query. 
                      Give them some advice based on their feelings."""),
        ("user", "{query}")
    ]
)

user_query = st.text_input("How do you feel today?")


@st.cache_data
def generate_response(user_query):
    st.session_state['count'] += 1
    prompt = prompt_template.invoke({"query": user_query})
    response = model.invoke(prompt)
    return response.content


f"You have asked me {st.session_state['count']} times"


if user_query:
    st.write(generate_response(user_query))