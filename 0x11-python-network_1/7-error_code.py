#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""


import requests
import sys

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.exceptions.HTTPError as e:
        print(e)

if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
