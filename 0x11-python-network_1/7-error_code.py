#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import requests
import sys


"""
    sends a request to the URL and displays the body of the response
"""


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
