#!/usr/bin/env python3

"""
Rectangle class module
using class method as an alternative constructor
"""

from math import sqrt


class Rectangle():
    """Rectangle class"""

    def __init__(self, length: int, width: int) -> object:
        self.length = length
        self.width = width

    def area(self) -> int:
        """Compute the area of rectangle object"""
        return self.width * self.length

    def perimeter(self) -> int:
        """Compute the perimter of rectangle object"""
        return (self.length + self.width) * 2

    def __repr__(self) -> str:
        """String representation of the rectangle"""
        return "[Rectangle] {} by {}".format(self.width, self.length)

    @classmethod
    def from_diagonal(cls, diagonal: int) -> object:
        """
        Return a new object with height and width
        computed from the diagonal using pythogorean theorem
        Args:
            diagonal (int) : length of the diagonal
        Return
            Rectangle object
        """
        width = int(sqrt(diagonal * diagonal / 2))
        height = int(sqrt(diagonal**2 - width**2))

        return cls(width, height)


if __name__ == "__main__":
    rect_1 = Rectangle(12, 13)
    print(rect_1)
    print("Area = {}" .format(rect_1.area()))
    print("Perimeter = {}".format(rect_1.perimeter()))

    # creating an object using the classmethod
    new_rect = Rectangle.from_diagonal(24)
    print(new_rect)
