import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("gemini_key")

if not GEMINI_API_KEY:
    raise ValueError("API key not found. Check .env file")