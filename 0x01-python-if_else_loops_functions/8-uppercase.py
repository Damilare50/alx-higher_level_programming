#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char == str[-1]:
            print("{:s}".format(chr(ord(char) - 32)))
        else:
            print("{:s}".format(chr(ord(char) - 32)), end="")
