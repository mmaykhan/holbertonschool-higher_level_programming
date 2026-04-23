#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    token = sys.argv[2]
    
    r = requests.get(url, auth=(user, token))
    try:
        json_res = r.json()
        print(json_res.get("id"))
    except ValueError:
        print("None")
