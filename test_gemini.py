import os
from dotenv import load_dotenv
from google import genai

print("Starting Gemini test...", flush=True)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found!")
    raise SystemExit(1)

client = genai.Client(api_key=api_key)

try:
    print("Sending question to Gemini...", flush=True)

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Explain Artificial Intelligence in 3 simple sentences."
    )

    print("\nGemini Response:")
    print(response.text)

except Exception as error:
    print("\nError:", error)

finally:
    client.close()

print("\nGemini test completed!")