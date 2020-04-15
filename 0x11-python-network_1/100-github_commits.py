#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/repos/{owner}/{repo}/commits"
    uri = url.format(repo=sys.argv[2], owner=sys.argv[1])
    r = requests.get(uri).json()
    for _commit in r[:10]:
        author = _commit.get("commit").get("author").get("name")
        sha = _commit.get("sha")
        print("{}: {}".format(sha, author))
