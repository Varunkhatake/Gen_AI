from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st  

load_dotenv()
model=ChatOpenAI(model_name="gpt-3", temperature=0.7)

st.header("reasearch paper summerizer")
user_input=st.text_input("Enter your research paper text here:") 

if st.button("summerize"):
    result= model.invoke(user_input)
    st.write(result.content)

