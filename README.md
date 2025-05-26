# 🧠 Text Summarizer App – A Generative AI Project

This project is a hands-on journey into Generative AI, built around a Python-based **Text Summarization App**. Designed for rapid development and frequent feature shipping, it helps you get practical with **LLMs**, **Streamlit**, and **Git**—without unnecessary complexity.

---

## 🚀 Project Goals

- Build an MVP text summarization app powered by an LLM (e.g., OpenAI or Gemini).
- Practice version control using Git in a solo dev workflow.
- Rapidly iterate with Python, focusing on GenAI features, not boilerplate.

---

## ✨ Features

**MVP**
- Simple UI for text input
- LLM API integration (OpenAI/Gemini)
- Summary output display

**Planned Enhancements**
- Abstractive vs. extractive summaries
- User-defined summary length
- Prompt engineering controls (e.g., temperature, top_p)
- Long-text handling via chunking (LangChain)
- Source attribution (for extractive)
- Multi-language support

---

## 🛠️ Tech Stack

| Tool          | Purpose                                |
|---------------|-----------------------------------------|
| Python        | Core programming language               |
| OpenAI SDK / Google GenAI | LLM interaction              |
| Streamlit     | Web interface for prototyping           |
| LangChain     | Chunking & orchestration for long texts |
| Git           | Version control                         |

---

## 🧰 Setup Instructions

```bash
# 1. Create project folder
mkdir text-summarizer-app && cd text-summarizer-app

# 2. Setup virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install dependencies
pip install openai streamlit langchain

# 5. Save dependencies
pip freeze > requirements.txt
```

> Add `.venv/` to your `.gitignore`.

---

## 📈 Project Structure (Planned)

```bash
text-summarizer-app/
├── .venv/
├── app.py               # Streamlit frontend
├── core_summarizer.py   # Core LLM logic
├── requirements.txt
└── README.md
```

---

## 🔁 Development Workflow

- Use **feature branches** for new functionality
- Make **atomic commits** with clear messages
- Practice **squashing**, **rebasing**, and **merging** locally
- Deploy via [Streamlit Cloud](https://share.streamlit.io/)

---

## 🧪 Example Commit Message

```bash
feat: Add summarization length control

Users can now control the output length using a slider,
which adjusts the max_tokens parameter in the LLM request.
```

---

## 📚 Learning Outcomes

- Build GenAI apps from scratch
- Strengthen Python dev practices (venv, requirements.txt)
- Master Git branching, rebasing, and commit hygiene
- Understand prompt engineering & LLM orchestration

---

## 🌱 What's Next?

- Explore RAG pipelines
- Integrate multilingual support
- Try out HuggingFace or local LLMs
- Deploy on Docker + cloud platforms

---

## 📎 References

See full resource links in the original project plan.
