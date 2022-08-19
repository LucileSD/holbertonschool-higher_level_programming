#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import urllib.request
import sys


"""
    sends a request to the URL and displays the value of the X-Request-Id
    variable found in the header of the response.
"""


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
