import requests
try:
    resp = requests.post("http://127.0.0.1:8000/api/roast/github", json={"username": "octocat"})
    data = resp.json()
    with open("error.log", "w", encoding="utf-8") as f:
        f.write(data.get("roast", "No roast field"))
except Exception as e:
    with open("error.log", "w", encoding="utf-8") as f:
        f.write(str(e))
