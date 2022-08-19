#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import urllib.request
import sys
from urllib.error import HTTPError


"""
    sends a request to the URL and displays the body of the response
    (decoded in utf-8)
"""


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
