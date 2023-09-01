#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""


import urllib.request
import sys

def send_request(url):
    with urllib.request.urlopen(url) as res:
        if res.getcode() != 200:
            raise urllib.error.HTTPError(res.getcode())
        return res.read().decode("utf-8")

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        res = send_request(url)
        print(res)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
