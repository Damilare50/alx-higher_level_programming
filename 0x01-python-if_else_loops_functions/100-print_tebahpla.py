#!/usr/bin/python3
num = 1
for i in range(ord('z'), ord('a') - 1, -1):
    if num % 2 == 0:
        st = chr(i - 32)
    else:
        st = chr(i)
    num += 1
    print("{:s}".format(st), end="")
