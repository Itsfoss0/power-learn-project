#!//usr/bin/env python3

"""
Shapes module
"""

class Shapes:
    """
    The Base class
    """
    _objects = {

    }

    def __init__(self, **kwargs):
        """
        Since the Shapes class will be inherited
        We dont know what properties the subclasses will
        need to implement, we use **kwargs instead
        """
        for key, value in kwargs.items():
            self.__setattr__(key, value)

        self.__class__._objects[list(self.__dict__.values())[0]] = self.__dict__

    def area(self):
        """Culculate area of the shape"""

    def perimeter(self):
        """Culculate perimeter of the shape"""
