from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

GITHUB_USERNAME = "CeeFish"
ALLOWED_PROJECTS = {"flask-github-api"}

@app.route("/projects")
def projects():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    repos = response.json()

    filtered_project_list = [
      {
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"],
        "language": repo["language"],
      }
      for repo in repos
      if repo["name"] in ALLOWED_PROJECTS
    ]
    return jsonify(filtered_project_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
