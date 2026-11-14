
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
st.header('Research tools')
user_input=st.text_input("Enter your promt")
if(st.button('Summarize')):
    result=model.invoke(user_input)
    st.write(result.content)
