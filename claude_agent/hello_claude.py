import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY nicht gefunden. Prüfe .env")

client = Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1024,
    messages=[
        {"role": "user","content": "Hallo Claude! Sag mir kurz was Agenten in der KI sind."}
    ]
)

for block in response.content:
    if block.type == "text":
        print(block.text)

print("Input-Tokens:", response.usage.input_tokens)
print("Output-Tokens:", response.usage.output_tokens)