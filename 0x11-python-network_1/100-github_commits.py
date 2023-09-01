#!/usr/bin/python3
""" Python script that takes 2 arguments
to list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""


import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    params = {"per_page": 10}
    res = requests.get(url, params=params)

    if res.status_code == 200:
        commits = res.json()
        for commit in commits:
            print("{}: {}".format(commit["sha"], commit["author"]["login"]))
    else:
        print("Error code: {}".format(res.status_code))
