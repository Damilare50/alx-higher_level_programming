#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    if len(sys.argv) == 2:
        sum = int(sys.argv[1])
    elif len(sys.argv) > 2:
        a = 1
        while a < len(sys.argv):
            sum += int(sys.argv[a])
            a += 1
    print(sum)
