import streamlit as st 
import warnings
warnings.filterwarnings("ignore")

import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"


# Define Model
from langchain.llms import HuggingFaceHub
llm = HuggingFaceHub(repo_id = "google/flan-t5-large")

# Function to Return the Response
def load_answer(question):
    answer = llm(question)
    return answer


# App UI Build
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Question Answer App")


# Gets User Input
def get_text():
    input_text = st.text_input("You : ", key= "input")
    return input_text


user_input = get_text()
response = load_answer(user_input)

submit = st.button("Generate")

if submit:
    st.subheader("Answer")
    st.write(response)