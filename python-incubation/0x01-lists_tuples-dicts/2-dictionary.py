#!/usr/bin/env python3
"""
Module to store information
about a person in a dictionary
"""

person = {
    "first_name": " ",
    "last_name": " ",
    "age":  0,
    "fav_color": " "
}

# update the details
for key in person.keys():
    person[key] = input("What's your {}: ".format(key))

print("=================================")
# print the details to stdout
for key, value in person.items():
    print("{} = {}".format(key, value))
