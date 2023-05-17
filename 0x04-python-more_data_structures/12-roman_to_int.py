#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    output = 0
    prev_value = 0
    
    for c in roman_string[::-1]:
        current_value = roman_values.get(c, 0)
        
        if current_value < prev_value:
            output -= current_value
        else:
            output += current_value
        
        prev_value = current_value
    
    return output
