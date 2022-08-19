#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import requests
import sys


"""
    takes your GitHub credentials (username and password) and uses
    the GitHub API to display your id
"""


if __name__ == "__main__":
    req = requests.get('https://api.github.com/user', auth=(sys.argv[1],
                       sys.argv[2]))
    res = req.json()
    try:
        print(res['id'])
    except KeyError:
        print("None")
