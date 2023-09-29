#!/bin/bash
# Finding all HTTP  methods a server can support
curl -sIlx "OPTIONS" "$1" | grep -i "allow" | cut -f 2 -d ":" | xargs
