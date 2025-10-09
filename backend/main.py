from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.github_fetch import fetch_github_data
import ollama

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request model
# -----------------------------
class RoastRequest(BaseModel):
    username: str
    intensity: str = "mild"  # optional: mild, medium, savage

# -----------------------------
# Helper function: generate AI roast
# -----------------------------
def generate_ai_roast(summary: dict, intensity: str = "mild") -> str:
    """
    Uses Ollama locally to generate a roast based on GitHub user summary.
    """
    tone = {
        "mild": "light and playful",
        "medium": "sarcastic but funny",
        "savage": "brutal but humorous"
    }.get(intensity, "light and playful")

    prompt = f"""
You are a witty AI comedian roasting a GitHub user in a {tone} tone.
Here is the user's data:

- Name: {summary['name']}
- Bio: {summary['bio']}
- Top language: {summary['top_language']}
- Public repos: {summary['public_repos']}
- Followers: {summary['followers']}
- Top repos: {', '.join([r['name'] for r in summary['top_repos']])}

Write 4–6 lines of roast, funny but safe for work.
End with one nice compliment about their skills.
"""

    try:
        response = ollama.chat(model="phi", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        print("Ollama error:", e)
        return f"Could not generate roast for {summary['name']}, but you are awesome! 😎"

# -----------------------------
# API endpoint: roast GitHub
# -----------------------------
@app.post("/api/roast/github")
async def roast_github(data: RoastRequest):
    username = data.username.strip()
    if not username:
        raise HTTPException(status_code=400, detail="GitHub username required")

    # Fetch GitHub user data
    summary, error = fetch_github_data(username)
    if error:
        raise HTTPException(status_code=404, detail=error)

    # Generate AI roast
    roast_text = generate_ai_roast(summary, data.intensity)
    return {"roast": roast_text}

# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
async def root():
    return {"message": "🔥 RoastMyProfile API is running!"}
