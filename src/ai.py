import requests
from config import OPENROUTER_API_KEY, OPENROUTER_URL, MODEL, HEADERS


SYSTEM_PROMPT = """
You are Krish AI.

You were created by Krish.

Never say Google created you.

If anyone asks who made you, always reply:

"Mujhe Krish ne banaya hai."

Always reply in Hinglish unless the user asks another language.

Be friendly, smart and helpful.
"""


class KrishAI:

    def __init__(self):
        self.history = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def chat(self, message):

        self.history.append({
            "role": "user",
            "content": message
        })

        data = {
            "model": MODEL,
            "messages": self.history
        }

        response = requests.post(
            OPENROUTER_URL,
            headers=HEADERS,
            json=data,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        reply = result["choices"][0]["message"]["content"]

        self.history.append({
            "role": "assistant",
            "content": reply
        })

        if len(self.history) > 21:
            self.history = [self.history[0]] + self.history[-20:]

        return reply
