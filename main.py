import os
from dotenv import load_dotenv

load_dotenv()

from google import genai

client=genai.Client()

chat = client.chats.create(model="gemini-3.6-flash")

# Ask anything anytime inside the chat.send_message("....")

response = chat.send_message("Explain Onepiece")

print(response.text)

