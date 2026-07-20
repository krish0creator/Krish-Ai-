import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b:free")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TAVILY_URL = "https://api.tavily.com/search"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/krish-ai",
    "X-Title": "Krish AI v4"
}
