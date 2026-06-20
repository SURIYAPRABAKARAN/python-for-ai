from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

HISTORY_FILE = "chat_history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


history = load_history()

print("AI Chatbot Started")
print("Type 'exit' to quit\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        save_history(history)
        print("Chat history saved.")
        break

    history.append(
        {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    ai_response = response.text

    print(f"\nAI: {ai_response}\n")

    history.append(
        {
            "role": "model",
            "parts": [{"text": ai_response}]
        }
    )

    save_history(history)