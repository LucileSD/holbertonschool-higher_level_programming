#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import requests


"""
    fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    req = r.text
    print("Body response:")
    print("\t- type:", type(req))
    print("\t- content:", req)
