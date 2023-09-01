#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests

def get_status():
    res = requests.get('https://alx-intranet.hbtn.io/status')

    if res.status_code == 200:
        print("Body res:")
        print("\t- type: {}".format(type(res.text)))
        print("\t- content: {}".format(res.text))
    else:
        print("Error code: {}".format(res.status_code))


if __name__ == '__main__':
    get_status()
