# 💻 AI Code Writer

AI Code Writer is a simple web application built with **Streamlit** that uses **Llama 3.2** through **Ollama** to generate, explain, debug, optimize, and convert code.

## ✨ Features

* 📝 Generate code from a natural-language prompt
* 📖 Explain existing code
* 🐛 Debug code
* ⚡ Optimize code
* 🔄 Convert code between programming languages
* 🌐 Supports multiple programming languages
* 🎨 Simple dark-themed Streamlit interface
* 🤖 Runs Llama locally using Ollama

## 🛠️ Technologies Used

* Python
* Streamlit
* Ollama
* Llama 3.2
* Requests

## 📋 Supported Languages

* Python
* C
* C++
* Java
* JavaScript
* HTML/CSS
* SQL
* Bash

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-code-writer.git
cd ai-code-writer
```

### 2. Install the required Python packages

```bash
pip install streamlit requests
```

### 3. Install Ollama

Install Ollama and make sure it is running on your system.

Then download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 How It Works

1. Select a programming language.
2. Select the task you want to perform.
3. Describe your requirement.
4. If required, paste your existing code.
5. Click **Generate Code**.
6. Llama 3.2 processes the request through Ollama and returns the result.

## 📌 Example

**Prompt:**

```text
Create a Python program that reads a CSV file and calculates the average marks.
```

The AI will generate the corresponding code based on the selected language and task.

## ⚠️ Requirements

* Python 3.8+
* Ollama installed and running
* Llama 3.2 model downloaded
* Internet connection for initial package/model installation

## 👨‍💻 Author

**Shubham**

A simple AI-powered coding assistant built using **Llama 3.2 + Streamlit + Ollama**.
