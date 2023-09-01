#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

import requests


def get_status():
    response = requests.get('https://alx-intranet.hbtn.io/status')

    if response.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    else:
        print("Error code: {}".format(response.status_code))


if __name__ == '__main__':
    get_status()
