#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import urllib.request


"""
    fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")
