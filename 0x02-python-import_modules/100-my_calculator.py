#!/usr/bin/python3

if __name__ == "__main__":
    import sys
from calculator_1 import add, sub, mul, div

if len(sys.argv) - 1 != 3:
    print("Usage: ./100-my_calculator.py <operand1> <operator> <operand2>")
    sys.exit(1)

operators = {"+": add, "-": sub, "*": mul, "/": div}
if sys.argv[2] not in list(operators.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

operand1 = int(sys.argv[1])
operand2 = int(sys.argv[3])
print("{} {} {} = {}".format(operand1, sys.argv[2], operand2, operators[sys.argv[2]](operand1, operand2)))
