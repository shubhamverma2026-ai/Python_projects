# 🔌 Electronics Mentor

<img width="1917" height="1031" alt="image" src="https://github.com/user-attachments/assets/a505a491-d713-4818-99af-39e116978854" />


A simple AI chatbot built using **Python, Streamlit, Ollama, and Llama 3.2**.

The chatbot is designed to answer **Electronics-related questions only**.

## Features

* 🤖 Uses Llama 3.2
* 🔌 Electronics-focused AI mentor
* 💬 Chat interface using Streamlit
* 🧠 Maintains chat history
* 📚 Beginner-friendly explanations
* 🚫 Rejects questions unrelated to Electronics
* 🌙 Simple dark UI

## Technologies

* Python
* Streamlit
* Ollama
* Llama 3.2
* Requests

## Installation

Install the required libraries:

```bash
pip install streamlit requests
```

Install and run Llama 3.2 using Ollama:

```bash
ollama pull llama3.2
```

## Run the Project

```bash
streamlit run app.py
```

The app will open at:

```text
http://localhost:8501
```

## How It Works

```text
User Question
      ↓
Streamlit
      ↓
System Prompt
      ↓
Ollama
      ↓
Llama 3.2
      ↓
Electronics Mentor Response
```

## Topics Covered

The chatbot can help with:

* Circuit Theory
* Analog Electronics
* Digital Electronics
* Diodes
* Transistors
* Op-Amps
* Semiconductors
* Microcontrollers
* Embedded Systems
* PCB Design
* Sensors
* Power Electronics
* Signal Processing

## Note

This project currently uses **Ollama locally**, so Ollama and the `llama3.2` model must be running on the computer where the application is being used.

> **Built for learning Electronics with AI. 🔌🤖**
