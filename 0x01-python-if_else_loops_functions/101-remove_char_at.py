#!/usr/bin/python3
def remove_char_at(str, n):
    # Check if n is a valid index
    if 0 <= n < len(str):
        result = str[:n] + str[n + 1:]
        return result
    else:
        return str
