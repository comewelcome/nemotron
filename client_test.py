from openai import OpenAI

# Point to the vLLM API server
client = OpenAI(
    api_key="EMPTY", # Required, but can be any string
    base_url="http://localhost:8000/v1"
)

# Example: Chat Completions
print("--- Chat Completions ---")
chat_response = client.chat.completions.create(
    model="nvidia/NVIDIA-Nemotron-Nano-9B-v2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=50,
    temperature=0.7
)
print(chat_response.choices[0].message.content)

# Example: Text Completions (legacy)
print("\n--- Text Completions ---")
text_response = client.completions.create(
    model="nvidia/NVIDIA-Nemotron-Nano-9B-v2",
    prompt="The capital of Germany is",
    max_tokens=20,
    temperature=0.7
)
print(text_response.choices[0].text)