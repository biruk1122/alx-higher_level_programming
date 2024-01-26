#!/usr/bin/python3
"""
Script that lists 10 commits (from most recent to oldest) of a repository by a specified owner.
"""

import requests
import sys

def list_commits(repo_name, owner_name):
    """
    List 10 commits (from most recent to oldest) of a repository by a specified owner.
    Args:
        repo_name (str): Repository name.
        owner_name (str): Owner name.

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {"per_page": 10}
    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    list_commits(repository_name, owner_name)
