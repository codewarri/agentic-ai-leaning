import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No Gemini API key found.")

client = genai.Client(api_key=api_key)


def ask_gemini(prompt, model="gemini-flash-latest"):
    """
    Native Gemini call.
    prompt = list of {role, content}
    """

    text = ""

    for msg in prompt:
        if msg["role"] == "system":
            text += f"{msg['content']}\n\n"
        elif msg["role"] == "user":
            text += msg["content"]

    response = client.models.generate_content(
        model=model,
        contents=text,
        config={
            "temperature": 0.7
        }
    )

    return response.text
