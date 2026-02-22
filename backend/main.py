import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.github_fetch import fetch_github_data

# Use OpenAI library to call Gemini via OpenAI compatibility
from openai import OpenAI
from openai import OpenAI as OpenAIClient  # alias for clarity

# Load env vars (for GEMINI_API_KEY)
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set in environment")

# Create OpenAI client configured for Gemini endpoint
gemini_client = OpenAIClient(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

class RoastRequest(BaseModel):
    username: str
    intensity: str = "mild"

def generate_gemini_roast(summary: dict, intensity: str = "mild") -> str:
    # Define tone
    tone = {
        "mild": "light and playful",
        "medium": "sarcastic but funny",
        "savage": "brutal and witty"
    }.get(intensity, "light and playful")

    prompt = f"""
You are a witty AI comedian. ROAST this GitHub user in a {tone} tone.
Facts:
- Name: {summary['name']}
- Bio: {summary['bio']}
- Top language: {summary['top_language']}
- Public repos: {summary['public_repos']}
- Followers: {summary['followers']}
- Top repos: {', '.join([r['name'] for r in summary['top_repos']])}

Write 4–6 lines of roast; be funny, sarcastic, exaggerate flaws.
End with at most one subtle compliment about their skills.
"""

    try:
        response = gemini_client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": "You are a roast bot."},
                {"role": "user", "content": prompt}
            ],
            # You could add temperature, max_tokens, etc.
        )
        # The response format: choices[0].message.content
        roast_text = response.choices[0].message.content
        return roast_text
    except Exception as e:
        print("Gemini API error:", e)
        return f"Could not roast {summary['name']} — Error: {str(e)}"

@app.post("/api/roast/github")
async def roast_github(req: RoastRequest):
    username = req.username.strip()
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")
    print(username)

    summary, error = fetch_github_data(username)
    if error:
        raise HTTPException(status_code=404, detail=error)


    roast = generate_gemini_roast(summary, req.intensity)
    return {"roast": roast}

@app.get("/")
async def root():
    return {"message": "Roast My Profile (Gemini) running!"}

@app.get("/api/test-rate")
async def test_rate():
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    r = requests.get("https://api.github.com/rate_limit", headers=headers)
    return r.json()
