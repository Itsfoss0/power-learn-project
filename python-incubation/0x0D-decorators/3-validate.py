#!/usr/bin/env python3

"""
Module to test the functionality of the validate
function decorator defined in the decorators module
"""

from decorators.decorators import validate


@validate
def add_numbers(num_a: int, num_b: int) -> int:
    """
    Simple function to add numbers
    Args:
        num_a (int): first number to add
        num_b (int): second number to add
    Returns:
        int
    """
    return (num_a + num_b)


if __name__ == "__main__":
    print(add_numbers(1, 2))
    print(add_numbers("John", 2))
    print(add_numbers(num_a=0, num_b=0))
