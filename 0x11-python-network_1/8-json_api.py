#!/usr/bin/python3
"""Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""


import sys
import requests


def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    res = requests.post(url, data=data)

    if res.status_code == 200:
        if res.content:
            try:
                return res.json()
            except JSONDecodeError:
                return {}
        else:
            return {}
    else:
        return {}


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    result = search_user(letter)

    if result == {}:
        print("No result")
    else:
        print("[{}] {}".format(result.get("id"), result.get("name")))
