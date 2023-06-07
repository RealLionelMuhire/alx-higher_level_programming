#!/usr/bin/python3
def remove_char_at(str, n):
    if n not in range(0, len(str)):
        return str
    return (str[:n] + str[n+1:])
