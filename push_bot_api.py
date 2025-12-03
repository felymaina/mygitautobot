from dotenv import load_dotenv
import os

load_dotenv()  # load .env file

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # safe access

REPO_OWNER = "felymaina"           # your GitHub username
REPO_NAME = "gitautobot"           # your repository name
BASE_BRANCH = "main"               # or "master" if that is your default branch
HEARTBEAT_FILE = "bot_log.py"
PR_MARKER_FILE = "pr_marker.txt"

