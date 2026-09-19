import os
from dotenv import load_dotenv

load_dotenv()

from google import genai

client=genai.Client()

chat = client.chats.create(model="gemini-3.6-flash")

response = chat.send_message("Explain how AI works in a few words"
)

print(response.text)

