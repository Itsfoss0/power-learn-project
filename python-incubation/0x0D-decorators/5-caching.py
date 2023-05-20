#!/usr/bin/env python3

"""
Module to test the functionality of
the caching decorator
"""

from decorators.caching import cache


@cache
def feed_dog(name: str) -> str:
    """
    Feed a dog
    Args:
        name (str): name of the dog to feed
    Return:
        returns a string
    """
    return f"Feeding {name}"


if __name__ == "__main__":
    print(feed_dog("Bulldog"))
    print(feed_dog("Bulldog"))
    print(feed_dog("Barbara"))