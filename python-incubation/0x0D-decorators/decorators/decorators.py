#!/usr/bin/env python3

"""
Module with functions to be used as
decorator to other functions. 
For the assignments at Power Learn Project
"""

def logger(function):
    """
    Logger function: Logs a function name and parameters before calling it
    Args:
        function: (object) the function to tbe called
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
