#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    element_division = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError
                if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                    raise TypeError
                if my_list_2[i] == 0:
                    raise ZeroDivisionError
                result = my_list_1[i] / my_list_2[i]
            except IndexError:
                print("out of range")
                result = 0
            except TypeError:
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            finally:
                element_division.append(result)
    finally:
        return element_division
