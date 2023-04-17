#!/usr/bin/env python3

"""
Determine number of
lines, words and characters in the file.

Usage: ./0-words_lines_chars.py <file_name>
"""

from os import path
from sys import argv

def calculate_chars_words_lines(file_name: str):
    print("Working on this feature")


if __name__ == "__main__":
    if len(argv) < 2 :
        print("Usage: ./0-words_lines_chars.py <file_name")
    else:
        calculate_chars_words_lines('file_name')