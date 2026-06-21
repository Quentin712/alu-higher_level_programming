#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase, followed by a new line"""
    result = ""
    for char in str:
        n = ord(char)
        if 97 <= n <= 122:
            n -= 32
        result += chr(n)
    print("{}".format(result))
