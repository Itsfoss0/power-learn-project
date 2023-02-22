#!/usr/bin/env python3

"""
Module that accepts integers from the user
Add them to list and compute their sum
"""

numbers = [int(x) for x in input("Enter Numbers seperated by space: ").split(" ")]
total = 0
for num in numbers:
    total += num

print("The sum of your numbers is {}".format(total))
