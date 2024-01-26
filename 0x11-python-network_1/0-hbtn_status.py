#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html.decode('utf-8'))
