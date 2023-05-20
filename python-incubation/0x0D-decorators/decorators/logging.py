#!/usr/bin/env python3

"""
Module for logging decorators
This one includes typing annotations
"""

from time import ctime
from typing import Callable


def function_logger(function: Callable) -> Callable:
    """
    Logger function
    This function keeps tracks of all the function calls
    their arguments and return values in a log file
    Usage:
        @function_loggger
        def foo(*args, **kwargs):
            """ """"
            return (bar)
    Returns:
        This function returns a wrapper function (more of a closure)
    """

    def wrapper(*args, **kwargs) -> object:
        """The wrapper function"""
        c_time = ctime()
        return_val = function(*args, **kwargs)
        with open("function_calls.log", "a", encoding="utf-8") as file:
            log_content = f"Function {function.__name__} called on {c_time} with arguments: {args}, {kwargs}"
            file.write(log_content + "\n")
    
        return return_val
    
    return wrapper