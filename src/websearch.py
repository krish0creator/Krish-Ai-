import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TAVILY_API_KEY")

URL = "https://api.tavily.com/search"


def web_search(query):
    payload = {
        "api_key": API_KEY,
        "query": query,
        "max_results": 3
    }

    response = requests.post(URL, json=payload)
    response.raise_for_status()

    data = response.json()

    text = ""

    for result in data.get("results", []):
        text += f"{result['title']}\n"
        text += f"{result['content']}\n"
        text += f"{result['url']}\n\n"

    return text
