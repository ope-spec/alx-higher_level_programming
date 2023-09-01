#!/usr/bin/python3
"""Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

import requests
import sys

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        if response.content:
            try:
                user = json.loads(response.content)
                print("[{}] {}".format(user["id"], user["name"]))
            except JSONDecodeError:
                print("Not a valid JSON")
        else:
            print("No result")
    else:
        print("Error code: {}".format(response.status_code))

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
