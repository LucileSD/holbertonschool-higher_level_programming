#!/bin/bash
#  takes in a URL and displays all HTTP methods the server will accept
curl -s "$1" -i -L -X OPTIONS | grep "Allow: " | cut -d' ' -f 2-
