#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the body of the response.
Prints an error message if the HTTP status code is greater than or equal to 400.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    print(response.text)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
