
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
#dotenv_path = os.path.join(os.path.dirname(".env"))
#print(dotenv_path)
load_dotenv()
os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGSMITH_ENDPOINT"]= os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_TRACING_V2"] = "true"
output_parser=StrOutputParser()
model = ChatGroq(model="qwen-qwq-32b")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a comedian"),
        ("user","{input}")
    ]
)
prompt
chain=prompt|model|output_parser
st.title("GPs Chatbot with Groq")
user_text = st.text_input("Enter some text:")
if user_text:
    response = chain.invoke({"input": user_text})
    st.write("Response:",response)