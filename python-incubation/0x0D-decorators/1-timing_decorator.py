#!/usr/bin/env python3

"""
Module to test out the timing
decorator defined in the decorator
module of the package
"""

from decorators.decorators import timer
from time import sleep


@timer
def just_sleep(seconds):
    """Sleep and do nothing else"""
    sleep(seconds)


if __name__ == "__main__":
    print(just_sleep(3))