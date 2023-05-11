#!/usr/bin/python3

if __name__ == "__main__":
    import sys
from calculator_1 import add, sub, mul, div

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <cal_method> <b>")
    sys.exit(1)

a = int(sys.argv[1])
cal_method = sys.argv[2]
b = int(sys.argv[3])

output = None
if cal_method == '+':
    output = add(a, b)
elif cal_method == '-':
    output = sub(a, b)
elif cal_method == '*':
    output = mul(a, b)
elif cal_method == '/':
    output = div(a, b)
else:
    print("Unknown cal_method. Available cal_methods: +, -, * and /")
    sys.exit(1)

print("{} {} {} = {}".format(a, cal_method, b, output))
