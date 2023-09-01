#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys

def get_github_user_id(username, password):
    url = "https://api.github.com/users/{}".format(username)
    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data["id"])
    else:
        print("Error code: {}".format(response.status_code))

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    get_github_user_id(username, password)
