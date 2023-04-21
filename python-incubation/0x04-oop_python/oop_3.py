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
    def computer_science_students(cls, name):
        """
        An alternative constructor to __init__
        """
        return cls({"name": name, "course": "CSE"})

    @classmethod
    def education_students(cls, name):
        return cls({"name": name, "course": "EDS"})

    @staticmethod
    def stat_method():
        return "Static method called"


student1 = Student({'name': "John Doe", 'age': 12, 'gender': 'male'})
print(student1)
print(student1.stat_method())

cs_stud = Student.computer_science_students("Jane Doe")
ed_stud = Student.education_students("Marrisa Wiegler")
print(cs_stud)
print(ed_stud)