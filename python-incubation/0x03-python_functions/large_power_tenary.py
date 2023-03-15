#!/usr/bin/env python3

"""
return True if base ^ exponent
is grater than 5000
"""


def is_big_power(base, exp) -> bool:
    """
    determine if base raised to exp > 5000
    Args:
         base (int)
         exp (int)
    """
    return (base ** exp) > 5000


print(is_big_power(4, 5))
print(is_big_power(500, 4))
