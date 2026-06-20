from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="Java Spring Boot"
)

print(len(result.embeddings[0].values))