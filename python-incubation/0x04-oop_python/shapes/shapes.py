#!//usr/bin/env python3

"""
Shapes module
"""

from uuid import uuid1

class Shapes:
    """
    The Base class
    """
    _objects = {

    }

    def __init__(self, shape_id=uuid1(), **kwargs):
        """
        Since the Shapes class will be inherited
        We dont know what properties the subclasses will
        need to implement, we use **kwargs instead
        """
        self.shape_id = str(shape_id)
        for key, value in kwargs.items():
            self.__setattr__(key, value)

        self.__class__._objects[self.shape_id] = self.__dict__

    def __str__(self):
        """String representation of the object"""
        return "[Shape] {} = {}".format(self.shape_id, self.__dict__)

    def area(self):
        """Culculate area of the shape"""

    def perimeter(self):
        """Culculate perimeter of the shape"""

    @classmethod
    def total_perimeter(cls):
        """The total perimeters of all objects"""




if __name__ == "__main__":
    shape_obj = Shapes(name="Circle", radius=89)
    print(shape_obj)
