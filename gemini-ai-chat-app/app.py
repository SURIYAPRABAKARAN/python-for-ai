from google import genai
from dotenv import load_dotenv
import os
# Load variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

question = input("Ask something: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)

print("\nAI Response:")
print(response.text)