# 🤖 AI Chatbot using Ollama

A simple command-line AI chatbot built with **Python** and **Ollama**.
The chatbot uses the **Llama 3.2** language model to generate responses to user messages locally.

## 📌 Features

* 💬 Interactive command-line chatbot
* 🧠 Powered by the Llama 3.2 AI model
* 🖥️ Runs locally using Ollama
* 🚪 Type `exit` to stop the chatbot
* ⚡ Simple and beginner-friendly Python implementation

## 🛠️ Technologies Used

* **Python**
* **Ollama**
* **Llama 3.2**

## 📋 Prerequisites

Before running the project, make sure you have:

1. Python installed on your computer.
2. Ollama installed and running.
3. The `llama3.2` model downloaded in Ollama.

## ⚙️ Installation

### 1. Install Ollama

Download and install Ollama from the official website:

[Ollama](https://ollama.com/?utm_source=chatgpt.com)

### 2. Download the Llama 3.2 Model

Open your terminal and run:

```bash
ollama pull llama3.2
```

### 3. Install the Python Ollama Package

Install the required Python library:

```bash
pip install ollama
```

## ▶️ How to Run

Save the Python code in a file such as:

```text
chatbot.py
```

Then run:

```bash
python chatbot.py
```

You should see:

```text
🤖 AI Chatbot
Type 'exit' to quit

You:
```

Enter your message and the chatbot will generate a response.

### Example

```text
🤖 AI Chatbot
Type 'exit' to quit

You: What is Python?
Bot: Python is a high-level programming language...

You: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄

You: exit
Bot: Goodbye!
```

## 🧩 How the Code Works

### 1. Import Ollama

```python
import ollama
```

The `ollama` library allows Python to communicate with the locally running Ollama model.

### 2. Get User Input

```python
user_input = input("You: ")
```

The program continuously asks the user to enter a message.

### 3. Exit Condition

```python
if user_input.lower() == "exit":
    print("Bot: Goodbye!")
    break
```

If the user types `exit`, the chatbot stops running.

### 4. Send Message to the AI

```python
response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ]
)
```

The user's message is sent to the **Llama 3.2** model through Ollama.

### 5. Display the AI Response

```python
bot_reply = response["message"]["content"]

print("Bot:", bot_reply)
```

The generated response is extracted and displayed in the terminal.

## 📁 Project Structure

```text
AI-Chatbot/
│
├── chatbot.py
└── README.md
```

## ⚠️ Troubleshooting

### Ollama is not running

Make sure the Ollama application/service is running before starting the Python program.

### Model not found

If you get an error related to `llama3.2`, run:

```bash
ollama pull llama3.2
```

### Python package not found

If Python shows an error such as:

```text
ModuleNotFoundError: No module named 'ollama'
```

Install the package using:

```bash
pip install ollama
```

## 🚀 Future Improvements

The chatbot can be extended with:

* 💾 Conversation history
* 👤 Custom system prompts
* 📝 Chat logging
* 🎨 Graphical user interface
* 🌐 Web-based interface
* 🔄 Support for multiple Ollama models
* ⚙️ Configurable model selection

## 📄 License

This project is created for educational and learning purposes.
