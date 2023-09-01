#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""


import requests
import sys

def get_request_id(url):
    response = requests.get(url)
    return response.headers.get("X-Request-Id")

if __name__ == "__main__":
    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)
