import streamlit as st
from transformers import pipeline

# Set page title and description
st.set_page_config(
    page_title="Text Generation App", page_icon=":pencil2:", layout="wide"
)

# Add a title and a description
st.title("Text Generation App")
st.write(
    "This application generates text using the GPT-2 model from Hugging Face. Enter some text and click 'Generate' to see the results."
)

# Initialize the Hugging Face model
generator = pipeline("text-generation", model="gpt2")

# Create a sidebar for input parameters
st.sidebar.title("Input Options")
input_text = st.sidebar.text_input("Enter some text")

# Create a button to generate text
generate_button = st.sidebar.button("Generate")

# Generate and display text when the button is clicked
if generate_button:
    with st.spinner("Generating text..."):
        output_text = generator(input_text)[0]["generated_text"]
    st.subheader("Generated Text:")
    st.write(output_text)
