import ollama

result = ollama.generate(model="Llama3:latest", prompt="Tell me about the history of quantum computing.")
print(result["response"])