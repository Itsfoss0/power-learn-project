#!/usr/bin/env python3

"""
module to learn different kinds of
methods in a class
"""

class Student:

    """
    Student class
    """
    
    def __init__(self, kwargs):
        """constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "[Student]: {}".format(self.__dict__)

    @classmethod
    def students(cls):
        return "Class method called on {}".format(cls)

    @staticmethod
    def stat_method():
        return "Static method called"


student1 = Student({'name': "John Doe", 'age': 12, 'gender': 'male'})
print(student1)
print(student1.stat_method())
print(student1.students())
