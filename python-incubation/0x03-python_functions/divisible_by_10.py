#!/usr/bin/env python

"""
determine if  num is divisible by 10
"""


def divisible_by_ten(num: int) -> bool:
    """
    return true if num is divisible by 10
    Args:
         num (int): the number to check
    """
    return num % 10 == 0


print(divisible_by_ten(10))
print(divisible_by_ten(13))
