#!/usr/bin/env python3


"""
Employee class module
"""


class Employee:
    """employee class"""

    def __init__(self, name: str, id_number: str, salary: int):
        """The constructor"""
        self.name = name
        self.id_number = id_number
        self.salary = salary

    def __str__(self):
        """String repr"""
        return "[Employee] {} of id {}".format(self.name, self.id_number)

    @staticmethod
    def is_salary_high(salary):
        """Determine if salary is enough"""
        return "Good pay" if salary > 10000 else "Need a raise"


emp_1 = Employee("John Doe", "5Y-AZT", 1000)
print(emp_1)

print(emp_1.is_salary_high(emp_1.salary))
