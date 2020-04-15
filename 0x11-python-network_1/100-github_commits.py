#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys
if __name__ == "__main__":
    auth = ('jormao', 'e28c968ac47559cb867111132d6a0bb807c8bd64')
    r = requests.get('https://api.github.com/repos/rails/rails/commits',
                     auth=auth).json()
    for _commit in r[:10]:
        author = _commit.get("commit").get("author").get("name")
        sha = _commit.get("sha")
        print("{}: {}".format(sha, author))
