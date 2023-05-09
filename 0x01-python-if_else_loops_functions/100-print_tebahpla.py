#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    print(chr(i).upper() if (i-ord('a'))%2==0 else chr(i).lower(), end='')
