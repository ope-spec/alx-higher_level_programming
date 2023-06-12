#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """class that inherits from int and inverts the behavior of == and != operators"""

    def __eq__(self, value):
        """Overrides the == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Overrides the != operator with == behavior"""
        return self.real == value
