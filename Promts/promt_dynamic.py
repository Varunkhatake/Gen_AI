from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI(model_name="gpt-3", temperature=0.7)

st.header("Research Paper Summarizer")

paper_input=st.text_input("Enter your research paper text here:")

style_input=st.selectbox("Select the style of summary:", ["beginner", "Technical", "code-orianted","Mathematical","advanced"])

length_input=st.selectbox("Select the length of summary:", ["short(2-3 paragraphs)", "medium(5-6 paragraphs)", "long(10+ paragraphs)"])

#template for the prompt
promt_template = load_prompt("prompt_template.json")

promt= promt_template.invoke({
    'paper_input': paper_input, 
    'style_input': style_input,
    'length_input': length_input
    })
if st.button("Summarize"):
    result= model.invoke(promt)
    st.write(result.content)
 