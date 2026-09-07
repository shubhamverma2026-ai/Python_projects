# 💻 AI Code Writer
<img width="1915" height="970" alt="image" src="https://github.com/user-attachments/assets/c7cd2687-be5e-4809-8ae4-379ec0ae5e27" />


A simple Streamlit app that uses a local Llama model (via Ollama) to **write** or **explain** code.

## Features
- **Write Code** – describe what you want, get generated code back.
- **Explain Code** – paste existing code and get a clear, step-by-step explanation.
- Choose the programming language and Llama model from the sidebar.

## Requirements
- Python 3.9+
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/) running locally with a model pulled (e.g. `llama3.2`)

## Setup
```bash
pip install streamlit requests
ollama pull llama3.2
ollama serve
```

## Run
```bash
streamlit run ai_code_writer.py
```

The app will open in your browser at `http://localhost:8501`.

## Usage
1. Pick a **Programming Language** and **Task** (Write Code / Explain Code) in the sidebar.
2. For **Write Code**: describe what you want in the text box.
3. For **Explain Code**: paste your code (and optionally note what to focus on).
4. Click the button and wait for the AI's response.

## Notes
- Requires Ollama to be running locally on port `11434`.
- If you see a connection error, make sure `ollama serve` is active and the model name matches a model you've pulled.
