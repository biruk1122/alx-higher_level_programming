#!/bin/bash
# Takes in a URL, sends a GET request to the URL
curl -sX GET "$1" -L 200
