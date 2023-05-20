#!/usr/bin/env python3

"""
Module to test the functionality of
The to_upper_case decorator defined
in the decorator package
"""

from decorators.decorators import to_upper_case


@to_upper_case
def say_hi(name: str) -> str:
    """
    Say Hi to name passed as an argument
    Args:
        name (str): The name to say `Hi` to
    """
    return (f"Hi {name}")


if __name__ == "__main__":
    print(say_hi("mom"))
