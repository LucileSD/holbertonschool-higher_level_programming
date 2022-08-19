#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import urllib.request
import sys


"""
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        html = response.read()
    print(html.decode('utf-8'))
