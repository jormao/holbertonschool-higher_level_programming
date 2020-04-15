#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/rails/rails/commits').json()
    for _commit in r[:10]:
        author = _commit.get("commit").get("author").get("name")
        sha = _commit.get("sha")
        print("{}: {}".format(sha, author))
