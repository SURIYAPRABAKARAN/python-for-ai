from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
print("AI Chatbot Started")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print(f"AI: {response.text}")
    print()