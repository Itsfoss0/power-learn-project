#!/usr/bin/env python3

"""
Module with the repeat function decorator
to handle repeating function calls
"""

from functools import wraps
from typing import Callable

def repeat(n_time: int) ->  Callable:
    """
    Repeat function decorator
    Args:
        n_time (int): Number of time the decorated function
                      should be called
    Returns:
        return a Callable (function object) that you can call
        But we will use it to decorate other functions
    """

    def decorator(function: Callable) -> Callable:
        """This is the function that returns our wrapper"""

        @wraps(function)
        def wrapper(*args, **kwargs):
            """You guesed it, our wrapper function"""
            wrapper_return_value = {}
            for time in range(n_time):
                func_obj_return_value = function(*args, **kwargs)
                wrapper_return_value[f"call_{time}"] = func_obj_return_value

            return wrapper_return_value

        return wrapper
    
    return decorator
        


