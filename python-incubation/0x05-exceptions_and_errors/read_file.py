#!/usr/bin/env python3

"""
A simple script to print the contents of the file
passed as an argument to this script
Usage: ./read_file.py <filename>
"""
from sys import argv


def read_file(filename: str) -> str:
    """Read the contents of a file and print them out"""
    # I could use a context manager to handle all these,
    # But where's the fun in that? Let's learn Exceptions and
    # Handle them as they come.
    try:
        file = open(filename, "r", encoding="utf-8")
        content = file.read()
        return content
    except (FileNotFoundError, IOError):
        return f" file '{filename}' not found"
    finally:
        if 'file' in locals():
            file.close()


if __name__ == "__main__":
    if len(argv) >= 2:
        print(read_file(argv[1]))
    else:
        print("Usage: ./read_file.py <filename>")
