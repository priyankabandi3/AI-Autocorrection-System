import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Autocorrection System")

st.title("AI-Powered Autocorrection and Grammar Correction")

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="vennify/t5-base-grammar-correction"
    )

model = load_model()

text = st.text_area("Enter your text")

if st.button("Correct Text"):
    if text:
        result = model(
            "grammar: " + text,
            max_length=128
        )

        corrected = result[0]["generated_text"]

        st.subheader("Corrected Text")
        st.success(corrected)