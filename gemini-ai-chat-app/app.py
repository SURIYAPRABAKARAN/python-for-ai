from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

question = input("Ask something: ")
//
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)

print("\nAI Response:")
print(response.text)