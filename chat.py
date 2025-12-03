import ollama

message = []

while True:
    user_inpit = input("You: ")
    if user_inpit.strip().lower() in ('/exit', ''):
        break

    message.append({"role": "user", "content": user_inpit})
    response = ollama.chat(
        model="Llama3:latest",
        messages=message
    )
    print("Llama: ", response["message"]["content"])
    message.append({"role": "assistant", "content": response["message"]["content"]})
