#!/usr/bin/env python3

"""
module has classes that Inherits from the Shape class of the
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

    @classmethod
    def total_perimeter(cls):
        """Total permimeters"""
        perimeters = list(cls._objects.values())
        return perimeters

class Rectangle(Shapes):
    """Rectangle class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def area(self):
        """find area of the rectangle and add it to _objects"""
        props = self.__dict__.keys()
        if 'width' in  props and 'length' in props:
            area = int(self.width * self.length)
            self.__class__._objects[self.shape_id]['area'] = area
            return area
        else:
            raise AttributeError("Rectangle missing width and length")

    def perimeter(self):
        """Culculate the permiter and it to class attrs"""
        props = self.__dict__.keys()
        if 'width' in  props and 'length' in props:
            perimeter = 2 * (self.length + self.width)
            self.__class__._objects[self.shape_id]['perimeter'] = perimeter
            return perimeter
        else:
            raise AttributeError("Rectangle missing width and length")


if __name__ == "__main__":
    circle_1 = Circle(shape="circle", radius=12)
    circle_1.area()
    circle_1.perimeter()
    print(Circle._objects)
    
    # print()
    # print(circle_1.total_perimeter())
    # print()

    circle_2 = Circle(shape="circle", radius=13)
    circle_2.area()
    circle_2.perimeter()
    print(Circle._objects)

    # print()
    # rectangle_1 = Rectangle(shape="rectangle", width=12, length=13)
    # rectangle_1.area()
    # rectangle_1.perimeter()
    # print(Rectangle._objects)
