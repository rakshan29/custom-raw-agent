import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Loads environment variables from .env file
load_dotenv()

@dataclass(frozen=True)
class ModelConfig():
	# Hold model parameters and its  configuration
	model_name: str = "gemini-3.6-flash" 
	temperature: float = 0.7
	max_output_tokens: int = 2048

@dataclass(frozen=True)
class AppConfig():
	# Configuration container for Agent in whole
	api_key: str
	model: ModelConfig=ModelConfig()

def load_config() -> AppConfig:

	# Retrieves KEY safely from .env file
	api_key=os.getenv("GEMINI_API_KEY")

	# Handles Error
	if not api_key:
		raise ValueError("GEMINI_API_KEY is missing! Please set it in your .env file.")

	return AppConfig(api_key=api_key)
