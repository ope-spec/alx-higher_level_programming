#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
         with urllib.request.urlopen(url) as res:
               print(res.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
