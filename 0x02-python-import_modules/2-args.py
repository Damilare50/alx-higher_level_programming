#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        a = 1
        while a < len(sys.argv):
            print("{:d}: {:s}".format(a, sys.argv[a]))
            a += 1
