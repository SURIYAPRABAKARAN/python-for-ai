from chroma_service import search_chunks
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_question(question):

    results = search_chunks(question)

    context = "\n".join(
        results["documents"][0]
    )

    prompt = f"""
    Answer using only the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text