#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

def fetch_status():
    response = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("- type:", type(response.text))
    print("- content:", response.text)

if __name__ == "__main__":
    fetch_status()
