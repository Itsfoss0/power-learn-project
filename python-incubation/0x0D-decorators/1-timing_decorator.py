#!/usr/bin/env python3

"""
Module to test out the timing
decorator defined in the decorator
module of the package
"""

from decorators.decorators import timer
from time import sleep


@timer
def just_sleep(seconds: int) -> int:
    """Sleep and do nothing else"""
    sleep(seconds)


@timer
def add_numbers(number_a: int, number_b: int) -> int:
    """Add two integer numbers
    Args:
        number_a (int): First number to add
        number_b (int): Second number to add
    Returns
        An integer
    """
    return (number_a + number_b)


if __name__ == "__main__":
    print(just_sleep(3))
    print(add_numbers(12, 45))
