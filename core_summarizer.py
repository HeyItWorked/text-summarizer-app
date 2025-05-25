from openai import OpenAI
import tomllib

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

if __name__ == '__main__':
    with open("secret.toml", "rb") as f:
        config = tomllib.load(f)
        key = config["openai"]["api_key"]
        if not key:
            print("API key not found. Set OPENAI_API_KEY in secret.toml")
        else:
            sample_tex = "This is a long piece of text about artificial intelligence and its implications for the future. It discusses various aspects including machine learning, natural language processing, and robotics. The goal is to understand the potential benefits and risks associated with these rapidly advancing technologies."
            summary= summarize_text_openai(key, sample_tex)
            print("Sample Text:", sample_tex)
            print("Summary:", summary)