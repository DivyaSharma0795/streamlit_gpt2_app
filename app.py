import streamlit as st
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

input_text = st.text_input("Enter some text")
generate_button = st.button("Generate")

if generate_button:
    output_text = generator(input_text)[0]["generated_text"]
    st.text(output_text)
