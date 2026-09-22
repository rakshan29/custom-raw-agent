import os
from dotenv import load_dotenv

load_dotenv()

# Retrieves KEY safely from .env file
api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
	raise ValueError("GEMINI_API_KEY is missing! Please set it in your .env file.")
