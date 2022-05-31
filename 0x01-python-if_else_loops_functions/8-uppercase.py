#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = char(ord(char) - 32)
        if char == str[-1]:
            print("{:s}".format(char))
        print("{:s}".format(char), end="")
