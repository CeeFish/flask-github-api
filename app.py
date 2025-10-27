from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

GITHUB_USERNAME = "CeeFish"

ALLOWED_PROJECTS = {
    "flask-github-api": {
        "display_name": "Flask GitHub API",
        "description": "A Python Flask API that fetches GitHub projects dynamically."
    },
    "rails-portfolio": {
        "display_name": "Rails Portfolio",
        "description": "My personal portfolio built with Ruby on Rails connected to Python API."
    }
}

@app.route("/projects")
def projects():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    repos = response.json()

    filtered_project_list = []
    for repo in repos:
        if repo["name"] in ALLOWED_PROJECTS:
            info = ALLOWED_PROJECTS[repo["name"]]
            filtered_project_list.append({
                "name": info["display_name"],
                "description": info["description"],
                "html_url": repo["html_url"],
                "language": repo["language"],
            })

    return jsonify(filtered_project_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
