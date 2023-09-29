#!/bin/bash
# this bash script takes in URL sends a request to that url and displays the size of body of response
curl -so /dev/null -w "%{size_download}\n" "$1" 
