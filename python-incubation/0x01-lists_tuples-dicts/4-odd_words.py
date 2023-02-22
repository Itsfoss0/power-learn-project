#!/usr/bin/env python3
""""
stores a list of words. Then, use list comprehension
to create a new list that contains only the words
that have an odd number of characters.
"""

words = ["John", "Doe", "I", "love", "Python", "React", "Angular", "Vue"]
odd_words = [word for word in words if len(word) % 2 != 0]
print(odd_words)
