#!/usr/bin/env python3

"""
Module to test the logging decorator
defined in the decorators module
"""

from decorators.logging import function_logger
from decorators.decorators import validate

@function_logger
def make_me_awesome(*args: list, **kwargs: dict) -> list:
    """
    Lets make you awesome shall we
    Args:
        args (list): A list of  positional arguments
        kwargs (dict): A dictionary of keyworded(named arguments)
    """
    if args:
        return [f"{x} is awesome" for x in args]
    return [f"{name} is awesome" for name in kwargs.values()]

@validate
@function_logger
def add(number_a: int, number_b: int) -> int:
    """Add two numbers
    Args:
        number_a (int): First number to add
        number_b (int): Second number to add
    Return:
        returns an interger
    """
    return (number_a + number_b)

if __name__ == "__main__":
    print(make_me_awesome("Jane Doe", "Kurt Weller", "Edgar Reed", "Remmy Briggs", "Keaton"))
    print(make_me_awesome("Python", "JavaScript", "C", "Docker", "K8S", "Bash"))
    print(add(number_a = 12, number_b = [1, 3]))
