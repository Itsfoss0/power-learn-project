#!/usr/bin/env python3
"""Introduction to oops in python"""


class MyClass:
    """Sample first class"""

    def __init__(self, my_id):
        """Constructor"""
        self.my_id = my_id

    def __getattr__(self, attr):
        """Get an attribute of the object"""
        if attr in self.__dict__.keys():
            return "{} = {}".format(attr, self.__dict__[attr])
        else:
            return "attribute '{}' not found!".format(attr)

    def __setattr__(self, name, value):
        """Overriding the set attribute function"""
        if not isinstance(name, str) or not isinstance(value, int):
            return "attribute '{}' has not been set".format(name)
        else:
            self.__dict__[name] = value

    @classmethod
    def class_attributes(self):
        return self.__class__.__dict__.keys()


if __name__ == "__main__":
    object1 = MyClass(12)
    print(object1.__getattr__('name'))
    object1.__setattr__('name', 12)
    print(object1.__getattr__('my_id'))
    print(object1.__getattr__('name'))
    print(object1.class_attributes())
