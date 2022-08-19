#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import urllib


"""
    fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
    print("Body response:")
    print(f"\t- type: {type}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
