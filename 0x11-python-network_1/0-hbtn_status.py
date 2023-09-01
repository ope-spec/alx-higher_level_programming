#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

def fetch_status():
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

if __name__ == "__main__":
    fetch_status()
