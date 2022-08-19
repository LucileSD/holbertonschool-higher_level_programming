#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import urllib.request


"""
    fetches https://intranet.hbtn.io/status
"""


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
print("Body response:")
print(f"    - type: {type(html)}")
print(f"    - content: {html}")
print(f"    - utf8 content: {html.decode('utf-8')}")
