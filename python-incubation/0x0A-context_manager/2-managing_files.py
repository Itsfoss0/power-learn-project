#!/usr/bin/env python3


"""
Module to test out the functionality of the
file managing context manager I've just written
and learn more about context management in python
"""


from contexts import FileManager

if __name__ == "__main__":
    with FileManager("hello.txt", "a") as file:
        file.write("Hi Mom!\n")

    with FileManager("hello.txt", "r") as file:
        print(file.read())