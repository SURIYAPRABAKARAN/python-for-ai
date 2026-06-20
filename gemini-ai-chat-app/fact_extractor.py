from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_user_facts(user_message):

    prompt = f"""
    Extract user information from the text.

    Return ONLY valid JSON.

    Example:

    {{
      "name": "Suriya",
      "age": 26,
      "profession": "Java Developer"
    }}

    User Message:
    {user_message}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)