import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY wurde nicht gefunden.")

client = OpenAI(api_key=api_key)

history = []

while True:
    user_input = input("Du: ")

    if user_input.strip().lower() == "exit":
        break

    history.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions="Du bist ein hilfreicher Assistent. Antworte auf Deutsch.",
            input=history
        )

    except Exception as e:
        print("API-Fehler:", e)
        continue

    answer = response.output_text

    print("Bot:", answer)

    print("Input-Tokens:", response.usage.input_tokens)
    print("Output-Tokens:", response.usage.output_tokens)
    print("Total-Tokens:", response.usage.total_tokens)

    history.append({
        "role": "assistant",
        "content": answer
    })