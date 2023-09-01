#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys

def get_request_id(url):
    with urllib.request.urlopen(url) as response:
        return response.headers.get("X-Request-Id")

if __name__ == "__main__":
    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)
