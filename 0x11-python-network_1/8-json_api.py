#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
Displays the id and name if the response body is properly JSON formatted and not empty.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={'q': q})
        data = response.json()

        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
