#!/bin/bash

# Make a request to 0.0.0.0:5000/catch_me using curl
curl -s -X PUT -L 0.0.0.0:5000/catch_me -d "user_id=98" > /dev/null
