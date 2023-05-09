#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    char = chr(i).upper() if (i - ord('a')) % 2 == 0 else chr(i).lower()
    print('{0}'.format(char), end='')
