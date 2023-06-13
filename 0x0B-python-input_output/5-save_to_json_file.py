#!/usr/bin/python3
"""Function that creates an Object from a “JSON file”"""
import json


def save_to_json_file(my_obj, filename):
    """Creates an object to a text file using JSON format"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
