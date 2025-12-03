import ollama
import json  # to pretty-print the message list

message = []

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ('/exit', ''):
        break

    # Add the user's message
    message.append({"role": "user", "content": user_input})

    # Send chat history to Ollama
    response = ollama.chat(
        model="Llama3:latest",
        messages=message
    )

    # Print assistant's reply
    print("Llama:", response["message"]["content"])

    # Store assistant's reply in history
    message.append({"role": "assistant", "content": response["message"]["content"]})

    # Debug: Show entire conversation so far
    print("\n--- Conversation history so far ---")
    print(json.dumps(message, indent=2))
    print("-----------------------------------\n")
