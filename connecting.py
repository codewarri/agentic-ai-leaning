import os
from google import genai  # Optimized for Gemini
from dotenv import load_dotenv

load_dotenv()

# Get the Gemini key instead of OpenAI
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError("No Gemini API key found. Please check your .env file.")

# Initialize the Google GenAI client
client = genai.Client(api_key=api_key)

def ask_gemini(user_message):
    # Gemini uses 'models.generate_content' instead of 'chat.completions'
    response = client.models.generate_content(
        model="gemini-flash-latest", 
        contents=user_message,
        config={
            "temperature": 0.7,
            "system_instruction": "You are a helpful assistant."
        }
    )
    return response.text

# Test it
user = "do u remember i called u again what i said to you ?"
response = ask_gemini(user)
print(response)