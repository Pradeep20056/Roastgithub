import requests

def fetch_github_data(username: str):
    user_resp = requests.get(f"https://api.github.com/users/{username}")
    if user_resp.status_code != 200:
        return None, "User not found"

    user = user_resp.json()
    repos_resp = requests.get(f"https://api.github.com/users/{username}/repos?per_page=30")
    repos = repos_resp.json()
    print(repos)

    languages = {}
    for r in repos:
        lang = r.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    top_lang = max(languages, key=languages.get) if languages else "None"

    summary = {
        "name": user.get("name", username),
        "bio": user.get("bio", ""),
        "public_repos": user.get("public_repos", 0),
        "followers": user.get("followers", 0),
        "top_language": top_lang,
        "top_repos": sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:3],
    }
    return summary, None
