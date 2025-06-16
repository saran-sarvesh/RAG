import requests
import streamlit as st

def writeessay(topic):
    response = requests.post("http://localhost:8000/essay/invoke",json={'input':{'topic':topic}})
    return response.json()['output']

def writepoem(topic):
    response = requests.post("http://localhost:8000/poem/invoke",json={'input':{'topic':topic}})
    return response.json()['output']


input1 = st.text_input("enter topic for essay")
input2 = st.text_input("enter topic for poem")

if input1:
    st.write(writeessay(input1))

if input2:
    st.write(writepoem(input2))