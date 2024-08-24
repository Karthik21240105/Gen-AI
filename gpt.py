from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 
import os
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Listen to whatever user says"),
        ("user","Answer the question in 100 words {question}")
    ]
)
prompt1=ChatPromptTemplate.from_template(
    """ 
    answer it with 100 words {question}
    """
)


model=Ollama(model="llama2")

output=StrOutputParser()

chain=prompt1|model|output

st.title("Chat gpt")
input=st.text_input("Ask your query")
button=st.button("click here")
if button :
   st.write(chain.invoke({"question":input}))