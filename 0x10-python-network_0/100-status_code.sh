#!/bin/bash
# sends request URL, and displays only the status code of the response.
curl -sI "$1" | awk 'NR==1 {print $2}'
