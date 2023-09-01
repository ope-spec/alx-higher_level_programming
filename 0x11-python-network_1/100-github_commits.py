#!/usr/bin/python3
""" Python script that takes 2 arguments
to list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
import sys

def get_github_commits(repo_name, owner_name):
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)
    params = {"per_page": 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            print("{}: {}".format(commit["sha"], commit["author"]["name"]))
    else:
        print("Error code: {}".format(response.status_code))

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_github_commits(repo_name, owner_name)
