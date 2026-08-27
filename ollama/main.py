import streamlit as st
import requests

st.set_page_config(page_title="Local Chatbot", page_icon="🤖")
st.markdown("<style>body{background-color:#111;color:#eee;}</style>", unsafe_allow_html=True)
st.title("🤖 Llama 3.2 Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",
        "messages": st.session_state.messages,
        "stream": False
    }).json()

    reply = response["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
