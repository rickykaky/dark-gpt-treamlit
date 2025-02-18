# Importation de toutes les bibliothèques nécessaires
import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from response import generate_meme,display_html_layout
 
 
 
os.environ ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
 
 
@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash")
model = get_model()
 
 
 
st.title("Dark-GPT")
 
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Entrez une situation pour avoir un meme"}]
"""
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

 # Fonction pour ajouter un message à l'historique
def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})
"""
# Afficher l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# React to user input
if prompt := st.chat_input("Générez votre meme"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
 
    result = generate_meme(prompt)
 
    response = f"Echo: { display_html_layout(result.id,result.link,result.champs)}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.write (result.id)
