from openai import OpenAI
import logging

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
        # Default or error for unknown style
        system_prompt = "tell me Uhm can't perform well for some reason"
        # Or, return f"Error: Unknown summary style '{summary_style}'."

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
        return f"Error during summarization: {str(e)}"
