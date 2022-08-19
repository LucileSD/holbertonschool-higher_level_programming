#!/usr/bin/python3
"""
    import Python module for fetching URLs
"""
import requests
import sys


"""
    sends a POST request to http://0.0.0.0:5000/search_user with the letter
    as a parameter
"""


if __name__ == "__main__":
    if len(sys.argv) == 1:
        obj = {'q': ""}
    else:
        obj = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', obj)

    try:
        dict = r.json()
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dict['id'], dict['name']))
    except ValueError:
        print("Not a valid JSON")
