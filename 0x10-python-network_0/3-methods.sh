#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -si -X OPTIONS "$1" | grep "Allow:" | cut -c 8-
