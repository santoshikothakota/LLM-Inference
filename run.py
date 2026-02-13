from llama_cpp import Llama

# Path to your downloaded GGUF model
model_path = "path_to_your_model.gguf"

# Load model into memory
llm = Llama(
    model_path=model_path,
    n_ctx=2048,     # context length
    n_threads=8     # adjust based on your CPU
)

# Personalized user input
user_question = input("Enter your question: ")
prompt = f"### Question: {user_question}\n### Answer:"

# Run inference
output = llm(prompt, max_tokens=64)

# Display model response

print(output["choices"][0]["text"].strip())