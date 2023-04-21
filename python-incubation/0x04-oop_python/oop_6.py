#!/usr/bin/env python3

"""
Square module Inherits from the Shape class of the
shapes module of the shapes package
"""
from math import pi
from shapes.shapes import Shapes

class Circle(Shapes):
    """Cirlce class"""

    def __init__(self, **kwargs):
        """The Constructor"""
        super().__init__(**kwargs)

    def area(self):
        """Culculate the area add it to the class Attrs"""
        area = int(pi * (self.radius)**2)
        self.__class__._objects[self.shape_id]['area'] = area
        return area
    
    def perimeter(self):
        """Culculate the permiter and it to class attrs"""
        perimeter = int((2 * pi * self.radius))
        self.__class__._objects[self.shape_id]['perimeter'] = perimeter


# if __name__ == "__main__":
#     circle_1 = Circle(shape="circle", radius=12)
#     circle_1.area()
#     circle_1.perimeter()

# print(Circle._objects)