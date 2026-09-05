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
    '<div class="subtitle">Generate, explain and improve code using Llama 3.2</div>',
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
        "Explain Code",
        "Debug Code",
        "Optimize Code",
        "Convert Code"
    ]
)

model = st.sidebar.text_input(
    "Llama Model",
    value="llama3.2"
)

# -----------------------------
# User Input
# -----------------------------
st.subheader("📝 Describe your task")

prompt = st.text_area(
    "What do you want the AI to do?",
    placeholder="Example: Create a Python program that reads a CSV file and calculates the average marks.",
    height=150
)

# -----------------------------
# Existing Code
# -----------------------------
if task_type in ["Explain Code", "Debug Code", "Optimize Code", "Convert Code"]:

    st.subheader("📄 Existing Code")

    existing_code = st.text_area(
        "Paste your code here",
        height=250,
        placeholder="Paste your code..."
    )

else:
    existing_code = ""


# -----------------------------
# Generate Button
# -----------------------------
if st.button("🚀 Generate Code", use_container_width=True):

    if not prompt.strip():
        st.warning("Please describe what you want the AI to do.")
        st.stop()

    # -------------------------
    # System Instructions
    # -------------------------
    system_prompt = f"""
You are an expert programming assistant.

Your task is to help the user with {task_type.lower()}.

Programming language:
{language}

Rules:

1. Provide correct and executable code.
2. Do not add unnecessary explanations.
3. Use clean and readable code.
4. Add comments where they improve understanding.
5. If debugging code, identify the problem and provide the corrected version.
6. If explaining code, explain the important parts clearly.
7. If optimizing code, preserve the original functionality.
8. Return code inside a Markdown code block.
"""

    # -------------------------
    # User Message
    # -------------------------
    user_prompt = f"""
User request:

{prompt}

Existing code:

{existing_code}
"""

    payload = {
        "model": model,
        "prompt": system_prompt + "\n" + user_prompt,
        "stream": False
    }

    # -------------------------
    # Call Ollama
    # -------------------------
    try:

        with st.spinner("🤖 Llama is writing your code..."):

            response = requests.post(
                "http://localhost:11434/api/generate",
                json=payload,
                timeout=120
            )

        if response.status_code == 200:

            result = response.json()

            generated_code = result.get(
                "response",
                "No response received."
            )

            st.subheader("💡 AI Response")

            st.markdown(generated_code)

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
