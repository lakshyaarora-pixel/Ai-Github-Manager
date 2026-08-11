import os

from dotenv import load_dotenv
from github import Github

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN not found")

github = Github(GITHUB_TOKEN)

user = github.get_user()

print("GitHub username:", user.login)

