import streamlit as st
from core_summarizer import summarize_text_openai

st.set_page_config(layout="wide", page_title="Text Summarizer AI")

st.title("📝 Text Summarization App")
st.markdown("""
    Welcome to the Text Summarization App! Paste your text below and get a concise summary.
    This app uses a Large Language Model to generate summaries.
""")

API_KEY_NAME_IN_SECRETS = "api_key" # Change if using Google or a different name
LLM_API_KEY = st.secrets.get(API_KEY_NAME_IN_SECRETS)

if not LLM_API_KEY:
    st.error(f"API Key not found. Please add it to your .streamlit/secrets.toml file.")
    st.stop()

input_text = st.text_area("Enter Text to Summarize:", height=200, placeholder="Paste your text here...")

if st.button("Summarize text", type="primary"):
    if input_text:
        with st.spinner("Summarizing... please wait."):
            summary = summarize_text_openai(LLM_API_KEY, input_text)
        st.subheader("Generated Summary:")
        st.markdown(f">{summary}")
    else:
        st.warning("Please enter some text to summarize.")