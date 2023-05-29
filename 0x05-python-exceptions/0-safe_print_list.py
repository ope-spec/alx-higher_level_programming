#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    
    try:
        for element in my_list:
            print(element, end=' ')
            
            count += 1
            
            # Check if the required number of elements has been printed
            if count == x:
                break
    
    except TypeError:
        print("Error: Unable to print the list elements.")
    
    print()  # Print a new line
    
    return count
