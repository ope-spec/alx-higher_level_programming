#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    
    for symbol in reversed(roman_string):
        current = roman_number.get(symbol, 0)
        
        if current >= prev:
            output += current
        else:
            output -= current
        
        prev = current
    
    return output
