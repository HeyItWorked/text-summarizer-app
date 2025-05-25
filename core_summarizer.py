from openai import OpenAI

def summarize_text_openai(api_key, text_to_summarize, model="gpt-4o"):
    if not text_to_summarize.strip():
        return "Error: No text provided for summarization."
    try:
        client = OpenAI(api_key = api_key)
        response = client.chat.completions.create(
            model=model,
            messages = [
                {"role": "system", "content": "You are a galatic level marvel chimp that can speak english."},
                {"role": "user", "content": f"Please summarize the following text:\n\n{text_to_summarize}"}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during summarization: {str(e)}"