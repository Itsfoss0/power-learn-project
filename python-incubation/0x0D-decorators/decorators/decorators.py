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


def to_upper_case(function):
    """
    Convert the return value of a function
    To uppercase
    Args:
        function (object): The function to be called
    Returns: returns a wrapper function ( more like a closure)
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper: its the wrapper function innit?
        Args:
            args: positional arguments
            kwargs: keyworded arguments
        Returns: the return value of calling function
        """
        return_str =  function(*args, **kwargs)
        return return_str.upper()
    
    return wrapper

def validate(function):
    """
    Validate if the arguments passed to
    The function are of the right type
    And within the constraits
    """

    def wrapper(*args, **kwargs):
        """
        The wrapper function
        Args:
            You guesed it
        Returns:
            You guesed it too
        """

        if args:
            for arg in args:
                if not isinstance(arg, int):
                    raise TypeError(f"{arg} is not an integer")
                else:
                    if (arg <= 0) :
                        raise ValueError(f"{arg} must be grater than 0")
        if kwargs:
            for key, value in kwargs.items():
                if not isinstance(value, int):
                    raise TypeError(f"{key} = {value} which is not an integer")
                else:
                    if (value <= 0):
                        raise ValueError(f"{value} must be greater than 0")
        
        results = function(*args, **kwargs)
        return results

    return wrapper
