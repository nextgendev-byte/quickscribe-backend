import os
from google import genai
from dotenv import load_dotenv
from google.genai.chats import Content

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()
myfile = client.files.upload(file="app/example.srt")


# Keep a list of previous messages
history = []


def ai(prompt):
    # Append the new user message
    history.append({"role": "user", "parts": [{"text": prompt}]})

    # Send entire conversation history
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=[prompt, myfile]
    )
    text = response.text

    # Append the AI's reply so it's included next time
    history.append({"role": "model", "parts": [{"text": text}]})
    print(f"{text}")
    return text
