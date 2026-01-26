import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("No API Key found")
    exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
resp = requests.get(url)
if resp.status_code == 200:
    models = resp.json().get("models", [])
    with open("models.log", "w", encoding="utf-8") as f:
        for m in models:
            f.write(f"Name: {m['name']}\n")
            f.write(f"Supported methods: {m.get('supportedGenerationMethods', [])}\n")
            f.write("-" * 20 + "\n")
else:
    with open("models.log", "w", encoding="utf-8") as f:
        f.write(f"Error: {resp.status_code} - {resp.text}")
