import os
from google import genai
from dotenv import load_dotenv

# Loads secrets variables
load_dotenv()

# Initiate Gemini Client
client=genai.Client()

chat = client.chats.create(model="gemini-3.6-flash")

# Giving input as data / information
response1 = chat.send_message("I have 2 computers in my house.")
print("Response 1:", response1.text)

# Ask question regarding the input data given 
response2 = chat.send_message("How many computers are in my house?")
print("Response 2:", response2.text)
