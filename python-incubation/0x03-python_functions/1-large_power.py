#!/usr/bin/env python3

"""
Module to determine a large power
"""


def large_power(base, exponent) -> bool:
    """
    determine if base to power exponent > 5000
    Args:
         base (int): base number
         exponent (int): exponent number
    """
    result = (base ** exponent)
    if result > 5000:
        return True
    return False


if __name__ == "__main__":
    print(large_power(3, 4))
    print(large_power(400, 50))
