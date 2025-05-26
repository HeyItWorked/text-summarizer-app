import streamlit as st
import logging
from core_summarizer import summarize_text_openai, summarize_long_text_langchain

logging.basicConfig(level=logging.DEBUG)
st.set_page_config(layout="wide", page_title="Text Summarizer AI")

st.title("📝 Text Summarization App")
st.markdown("""
    Welcome to the Text Summarization App! Paste your text below and get a concise summary.
    This app uses a Large Language Model to generate summaries.
""")

API_KEY_NAME_IN_SECRETS = "api_key" # Change if using Google or a different name
LLM_API_KEY = st.secrets.get(API_KEY_NAME_IN_SECRETS)

# logging.debug(f"Value of api_key: {LLM_API_KEY}")

if not LLM_API_KEY:
    st.error(f"API Key not found. Please add it to your .streamlit/secrets.toml file.")
    st.stop()

summary_style = st.radio(
    "Choose Summarization Style:",
    ['Abstractive (Rewrite)', 'Extractive (Key Sentences - Basic)'],
    horizontal=True
)

input_text = st.text_area("Enter Text to Summarize:", height=200, placeholder="Paste your text here...")
st.info("Adjust the summary length and style using the options below.")

desired_length  = st.slider("Desired Summarzy Length (approx. tokens):", min_value=10, max_value=300, value=150, step=10)

col1, col2 = st.columns(2)
with col1:
    if st.button("Summarize text", type="primary"):
        if input_text:
            try:
                logging.debug(f"Length of input text: {len(input_text)}")
                with st.spinner("Summarizing... please wait."):
                    if len(input_text) > 300: # Basic threshold, consider making this more dynamic or configurable
                        logging.debug("Using Langchain for long text summarization.")
                        summary = summarize_long_text_langchain(
                            LLM_API_KEY, 
                            input_text,
                            desired_length, 
                            'abstractive' if summary_style == 'Abstractive (Rewrite)' else 'extractive'
                        )
                    else:
                        logging.debug("Using OpenAI directly for shorter text summarization.")
                        summary = summarize_text_openai(
                            LLM_API_KEY, 
                            input_text, 
                            'abstractive' if summary_style == 'Abstractive (Rewrite)' else 'extractive', 
                            desired_length
                        )
                
                if summary.startswith("Error"):
                    st.error(summary)
                else:
                    st.subheader("Generated Summary:")
                    st.success(summary) # Using st.success for positive feedback
            except Exception as e:
                logging.error(f"An unexpected error occurred in the summarization block: {type(e).__name__} - {str(e)}")
                st.error(f"An unexpected error occurred: {str(e)}. Please check the logs or try again.")
        else:
            st.warning("Please enter some text to summarize.")
with col2:
    if st.button("Clear Fields"):
        st.rerun()
