#!/usr/bin/python3
def uppercase(s):
    output = ""
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            output += '{}'.format(chr(ord(c) - 32))
        else:
            output += '{}'.format(c)
    print('{}'.format(output))
