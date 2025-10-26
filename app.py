from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_USERNAME = "CeeFish"

@app.route("/projects")
def projects():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    repos = response.json()

    project_list = []
    for repo in repos:
        if not repo.get("fork"):
            project_list.append({
                "name": repo["name"],
                "description": repo["description"],
                "url": repo["html_url"],
                "language": repo["language"],
            })
    return jsonify(project_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
