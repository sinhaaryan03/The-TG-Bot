import os
from git import Repo
from shutil import copytree, rmtree
GITHUB_REPO = os.environ.get("GITHUB_REPO_LINK", "https://github.com/techyminati/The-TG-Bot").split()
GITHUB_REPO_LINK = GITHUB_REPO[0]
try:
  GITHUB_REPO_BRANCH = GITHUB_REPO[1]
except:
  GITHUB_REPO_BRANCH = "Mod-v1"
print("Downloading latest version of The-TG-Bot Mod by TechyMinati..")
Repo.clone_from(GITHUB_REPO_LINK, ".ota", branch=GITHUB_REPO_BRANCH)
copytree(".ota", ".", dirs_exist_ok=True)
rmtree(".ota")
import thetgbot
