#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""

import urllib.request
import sys

def send_request(url):
    with urllib.request.urlopen(url) as response:
        if response.getcode() != 200:
            raise urllib.error.HTTPError(response.getcode())
        return response.read().decode("utf-8")

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = send_request(url)
        print(response)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
