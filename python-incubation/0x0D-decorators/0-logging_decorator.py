#!/usr/bin/env python3

"""
Module to test out the logging decorator
defined in the decorators module of the
decorators package
"""

from decorators.decorators import logger


@logger
def say_hi(who: str) -> str:
    """
    Say Hello to the person named in the argument
    Args:
        who (str) : The person to say Hello to
    Returns:
        string
    """

    return "Hi {}".format(who)


if __name__ == "__main__":
    print(say_hi("Mom"))