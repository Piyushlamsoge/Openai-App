# Importing required packages
import streamlit as st
import openai

# Set the API key
openai.api_key = "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"

st.set_page_config(page_title="OpenAI Text Completion", page_icon=":guardsman:", layout="wide")
st.title("OpenAI Text Completion")

prompt = st.text_input("Enter your prompt:")
if st.button("Generate Text"):
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)
    text = completions.choices[0].text
    st.write(text)
