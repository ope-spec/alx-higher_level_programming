#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for roman_numerals in reversed(roman_string):
        value = digits.get(roman_numerals, 0)
        total += value if total < value * 5 else -value

    return total
