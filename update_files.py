import os
import datetime
from git import Repo

# Define the path of the repository and the file to update
repo_path = os.getcwd()  # Assuming the script is in the repo directory
file_path = os.path.join(repo_path, "contribution.txt")

# Update the file with the current date and time
with open(file_path, "a") as file:
    file.write(f"Contribution on {datetime.datetime.now()}\n")

# Commit and push the changes
repo = Repo(repo_path)
repo.git.add(file_path)
repo.index.commit(f"Contribution on {datetime.datetime.now()}")
origin = repo.remote(name="origin")
origin.push()
