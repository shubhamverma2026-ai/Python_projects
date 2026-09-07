import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Code Writer",
    page_icon="💻",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #111111;
        color: #eeeeee;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #aaaaaa;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown(
    '<div class="title">💻 AI Code Writer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Generate and explain code using Llama 3.2</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙️ Settings")

language = st.sidebar.selectbox(
    "Programming Language",
    [
        "Python",
        "C",
        "C++",
        "Java",
        "JavaScript",
        "HTML/CSS",
        "SQL",
        "Bash"
    ]
)

task_type = st.sidebar.selectbox(
    "Task",
    [
        "Write Code",
        "Explain Code"
    ]
)

model = st.sidebar.text_input(
    "Llama Model",
    value="llama3.2"
)

# -----------------------------
# User Input
# -----------------------------
if task_type == "Write Code":
    st.subheader("📝 Describe your task")

    prompt = st.text_area(
        "What do you want the AI to do?",
        placeholder="Example: Create a Python program that reads a CSV file and calculates the average marks.",
        height=150
    )

    existing_code = ""

else:  # Explain Code
    st.subheader("📄 Paste the code you want explained")

    existing_code = st.text_area(
        "Existing code",
        height=250,
        placeholder="Paste your code here..."
    )

    prompt = st.text_area(
        "Anything specific you want explained? (optional)",
        placeholder="Example: Focus on what the recursive function does.",
        height=100
    )

# -----------------------------
# Generate Button
# -----------------------------
button_label = "🚀 Generate Code" if task_type == "Write Code" else "🔍 Explain Code"

if st.button(button_label, use_container_width=True):

    # -------------------------
    # Validation
    # -------------------------
    if task_type == "Write Code" and not prompt.strip():
        st.warning("Please describe what you want the AI to do.")
        st.stop()

    if task_type == "Explain Code" and not existing_code.strip():
        st.warning("Please paste the code you want explained.")
        st.stop()

    # -------------------------
    # System Instructions
    # -------------------------
    if task_type == "Write Code":
        system_prompt = f"""
You are an expert programming assistant.

Your task is to write code based on the user's request.

Programming language:
{language}

Rules:

1. Provide correct and executable code.
2. Do not add unnecessary explanations.
3. Use clean and readable code.
4. Add comments where they improve understanding.
5. Return the code inside a Markdown code block.
"""

        user_prompt = f"""
User request:

{prompt}
"""

    else:  # Explain Code
        system_prompt = f"""
You are an expert programming assistant.

Your task is to clearly explain the following {language} code to the user.

Rules:

1. Summarize what the code does overall in 1-2 sentences first.
2. Then walk through the important parts step by step, in plain language.
3. Point out any notable logic, edge cases, or potential issues you notice.
4. Do not rewrite or "fix" the code unless something is broken and relevant to explaining it.
5. Keep the explanation clear and avoid unnecessary jargon.
6. Only use short inline code snippets (not a full code block) when referencing specific lines.
"""

        user_prompt = f"""
Code to explain:

{existing_code}

Additional focus from the user (if any):
{prompt if prompt.strip() else "None"}
"""

    payload = {
        "model": model,
        "prompt": system_prompt + "\n" + user_prompt,
        "stream": False
    }

    # -------------------------
    # Call Ollama
    # -------------------------
    spinner_text = "🤖 Llama is writing your code..." if task_type == "Write Code" else "🤖 Llama is analyzing your code..."

    try:

        with st.spinner(spinner_text):

            response = requests.post(
                "http://localhost:11434/api/generate",
                json=payload,
                timeout=120
            )

        if response.status_code == 200:

            result = response.json()

            generated_text = result.get(
                "response",
                "No response received."
            )

            header = "💡 AI Response" if task_type == "Write Code" else "🧠 Explanation"

            st.subheader(header)

            st.markdown(generated_text)

        else:

            st.error(
                f"Ollama returned an error: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to Ollama. "
            "Make sure Ollama is running."
        )

    except requests.exceptions.Timeout:

        st.error(
            "⏳ Request timed out. "
            "Try a shorter prompt or make sure Ollama is running properly."
        )

    except Exception as e:

        st.error(f"Something went wrong: {e}")
