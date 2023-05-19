#!/usr/bin/env python3

"""
Module with functions to be used as
decorator to other functions. 
For the assignments at Power Learn Project
"""

from time import time


def logger(function):
    """
    Logger function: Logs a function name and parameters before calling it
    Args:
        function: (object) the function to the called
    """

    def wrapper(*args, **kwargs):
        """ 
        The wrapper function
        Args:
            *args: numbered arguments
            **kwargs: named arguments
        """
        if args:
            print(f"Calling function {function.__code__.co_name} with argument(s): {args}.")
        # else:
        #     print(f"Calling function {function.__code__.co_name} with argument(s) {kwargs}")
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper


def timer(function):
    """
    Timer function: times the execution time of a function
    Args:
        function (object) the function to be called
    Returns:
        returns a wrapper function (as you might have guesed)
    """
    
    def wrapper(*args, **kwargs):
        """The wrapper function"""
        s_time = time()
        return_value = function(*args, **kwargs)
        e_time = time()
        total_time = e_time - s_time
        print(f"The function {function.__code__.co_name} took {total_time} seconds to execute.")

        return return_value
    
    return wrapper

