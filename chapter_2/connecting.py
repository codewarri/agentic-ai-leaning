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
        contents=contents,
        config={
            "temperature": 0.7,
            "system_instruction": "You are a helpful assistant."
        }
    )
    return response.text
 
contents = [
    "What is the capital of France?",
    "The capital of France is Paris.",

]


# Test it
user = "What is an interesting fact about Paris?"
contents.append(user)
response = ask_gemini(user)
print(response)