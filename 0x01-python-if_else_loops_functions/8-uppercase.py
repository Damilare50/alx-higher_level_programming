#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            st = chr(ord(char) - 32)
        else:
            st = char
        print("{:s}".format(st), end="")
    print("")
