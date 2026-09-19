import os
from google import genai
from dotenv import load_dotenv

# Loads secrets variables
load_dotenv()

# Initiate Gemini Client
client=genai.Client()

chat = client.chats.create(model="gemini-3.6-flash")

# Ask anything anytime inside chat.send_message("....")
response = chat.send_message_stream("Explain Onepiece")

# Iterate through text chunks as they arrive from Google's servers
# Human reading sychronization, Real-Time Feedback & Cancellation
for chunk in response:
	print(chunk.text,end="",flush=True)
print()
