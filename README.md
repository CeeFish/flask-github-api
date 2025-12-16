# Python Flask API

## Overview
This is a Python Flask API designed to dynamically load projects from GitHub to my personal portfolio.

## Tech Stack
- Python 3.11
- Flask

## Setup

**Clone the repository**
```bash
git clone https://github.com/yourusername/flask-api.git
cd flask-api

**Create a virtual environment**
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

**Install dependencies**
pip install -r requirements.txt

**Run the server**
export FLASK_APP=app.py       # Linux/macOS
set FLASK_APP=app.py          # Windows
flask run


The API will be available at http://127.0.0.1:5000
