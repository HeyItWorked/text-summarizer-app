import streamlit as st
from core_summarizer import summarize_text_openai
import tomllib

st.set_page_config(layout="wide", page_title="Text Summarizer AI")

st.title("📝 Text Summarization App")
st.markdown("""
    Welcome to the Text Summarization App! Paste your text below and get a concise summary.
    This app uses a Large Language Model to generate summaries.
""")

with open("secret.toml", "rb") as f:
    config = tomllib.load(f)
    key = config["openai"]["api_key"]
    if not key:
        st.error(f"API Key ({API_KEY_NAME_IN_SECRETS}) not found. Please add it to your .streamlit/secrets.toml file.")
        st.stop()

input_text = st.text_area("Enter Text to Summarize:", height=200, placeholder="Paste your text here...")

if st.button("Summarize text", type="primary"):
    if input_text:
        with st.spinner("Summarizing... please wait."):
            summary = summarize_text_openai(key, input_text)
        st.subheader("Generated Summary:")
        st.markdown(f">{summary}")
    else:
        st.warning("Please enter some text to summarize.")