import os
from google import genai
from dotenv import load_dotenv

# Loads secrets variables
load_dotenv()

# Initiate Gemini Client
client=genai.Client()

chat = client.chats.create(model="gemini-3.6-flash")

# Giving input as data / information
response1 = chat.send_message_stream("I have 2 computers in my house.")
for chunk in response1:
	print(chunk.text,end="",flush=True)
print()

# Ask question regarding the input data given 
response2 = chat.send_message_stream("How many computers are in my house?")
for chunk in response2:
	print(chunk.text,end="",flush=True)
print()
