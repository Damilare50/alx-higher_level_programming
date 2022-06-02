#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    lent = len(sys.argv)
    if lent != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    oper = sys.argv[2]
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if oper == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif oper == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    elif oper == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    elif oper == '/':
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown Operator. Available operators: +, -, * and /")
        exit(1)
