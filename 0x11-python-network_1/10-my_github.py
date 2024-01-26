#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user id.
"""

import requests
import sys

def get_user_id(username, token):
    """
    Get GitHub user id using Basic Authentication with a personal access token.
    Args:
        username (str): GitHub username.
        token (str): Personal access token.

    Returns:
        int: User id.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return data['id']

if __name__ == "__main__":
    github_username = sys.argv[1]
    personal_access_token = sys.argv[2]

    user_id = get_user_id(github_username, personal_access_token)
    print("GitHub User ID:", user_id)
