import streamlit as st 
import requests 

def e_request(input_text):
    response = requests.post(
    "http://localhost:8000/essay/invoke",
    json={"input":{"topic":input_text}}    
    )

    return response.json()["output"]

def p_request(input_text):
    response = requests.post(
    "http://localhost:8000/poem/invoke",
    json={"input":{"topic":input_text}}    
    )

    return response.json()["output"]


st.title("API Client")
e_input = st.text_input("Enter the topic for essay")
e_button = st.button("Click for essay")

p_input = st.text_input("Enter the topic for poem")
p_button = st.button("Click for poem")

if e_input and e_button:
    output = e_request(e_input)
    st.write(output)

if p_input and p_button:
    output1 = p_request(p_input)
    st.write(output1)