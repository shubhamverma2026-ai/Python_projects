import ollama

print("🤖 AI Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    bot_reply = response["message"]["content"]

    print("Bot:", bot_reply)
