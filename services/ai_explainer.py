import os
import openai
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_API_KEY')
if OPENAI_KEY:
    openai.api_key = OPENAI_KEY


def explain_build(build: Dict, role_hint: str = "advisor") -> str:
    """Send build summary to OpenAI and get explanation. The AI receives only the final selected builds."""
    system = (
        "You are an expert PC hardware advisor.\n"
        "Do NOT invent specifications or prices. Use the provided build data only.\n"
        "Explain why parts were chosen, tradeoffs, bottlenecks, and upgrades. Keep output concise and actionable."
    )

    user = f"Here is a build:\n{build}\nExplain choices, bottlenecks, and upgrade suggestions."

    if not OPENAI_KEY:
        return "OpenAI key not configured. Set OPENAI_API_KEY in your .env to enable AI explanations."

    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        max_tokens=450,
        temperature=0.7,
    )
    return resp['choices'][0]['message']['content']
