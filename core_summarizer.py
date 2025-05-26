from openai import OpenAI
import logging
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

logging.basicConfig(level=logging.DEBUG)
def summarize_text_openai(api_key, text_to_summarize, summary_style, desired_length, model="gpt-4o"):
    if not text_to_summarize.strip():
        return "Error: No text provided for summarization."

    if summary_style == 'abstractive':
        system_prompt = "You are a helpful assistant that summarizes text by rewriting it concisely."
    elif summary_style == 'extractive':
        # This is a simplified way to ask an LLM for something *like* extractive.
        # True extractive usually involves sentence scoring and selection.
        system_prompt = "You are a helpful assistant. Extract the most important key sentences from the following text to form a summary. Present them as a list or a coherent paragraph made of these exact sentences."
    else:
        logging.error(f"Unknown summary style received: {summary_style}")
        return f"Error: Unknown summary style '{summary_style}'. Please choose 'abstractive' or 'extractive'."

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Please summarize the following text based on the system instruction:\n\n{text_to_summarize}"}
            ],
            temperature=0.7,
            max_tokens=desired_length
        )
        logging.debug(f"Response: {response.usage.completion_tokens}")
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"OpenAI API error in summarize_text_openai: {type(e).__name__} - {str(e)}")
        return f"Error during summarization with OpenAI: {str(e)}"

def summarize_long_text_langchain(api_key, text_to_summarize, desired_length_tokens, summary_style, model_name="gpt-4o"):
    if not text_to_summarize.strip():
        return "Error: No text provided for summarization."
    if summary_style == 'abstractive':
        system_prompt = "You are a helpful assistant that summarizes text by rewriting it concisely."
    elif summary_style == 'extractive':
        system_prompt = "You are a helpful assistant. Extract the most important key sentences from the following text to form a summary. Present them as a list or a coherent paragraph made of these exact sentences."
    else:
        logging.error(f"Unknown summary style received for Langchain: {summary_style}")
        return f"Error: Unknown summary style '{summary_style}'. Please choose 'abstractive' or 'extractive'."

    try:
        client = ChatOpenAI(api_key=api_key, model_name=model_name, temperature=0.7, max_tokens=desired_length_tokens) # Note: max_tokens here applies to individual LLM calls in the chain
        text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=200) # Consider making chunk_size and overlap configurable
        docs = text_splitter.create_documents([text_to_summarize])
        
        # Map prompt: process each chunk
        map_prompt_template = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_prompt),
            HumanMessagePromptTemplate.from_template("Summarize the following text chunk:\n\n{text}")
        ])
        
        # Combine prompt: combine summaries of chunks
        # The {text} variable here will contain the concatenated summaries from the map step.
        # For ChatOpenAI, the combine prompt also needs to be a ChatPromptTemplate
        combine_prompt_template = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_prompt), # You can have a different system message for combining if needed
            HumanMessagePromptTemplate.from_template(
                "The following are summaries of different parts of a long document:\n{text}\n\n"
                "Please combine them into a single, coherent summary that captures the main points of the overall document, "
                "adhering to the initial instruction about the summarization style. "
                "Ensure the final summary is well-structured and easy to read."
            )
        ])

        chain = load_summarize_chain(
            client,
            chain_type="map_reduce",
            map_prompt=map_prompt_template,
            combine_prompt=combine_prompt_template # Added combine_prompt
        )
        summary = chain.invoke(docs)["output_text"]
        return summary
    except Exception as e:
        logging.error(f"Langchain error in summarize_long_text_langchain: {type(e).__name__} - {str(e)}")
        return f"Error during summarization with Langchain: {str(e)}"
