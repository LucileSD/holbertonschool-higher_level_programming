#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import requests
import sys


"""
    fetches sends a request to the URL and displays the value of the variable
    X-Request-Id in the response header
"""


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
