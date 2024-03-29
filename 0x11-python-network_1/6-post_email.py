#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import requests
import sys


"""
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response.
"""


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
