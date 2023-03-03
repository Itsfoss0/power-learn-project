#!/usr/bin/env python3
"""
Module to ask interact with the user
"""

name = input("Whats your name? ").strip()
age = int(input("How old are you {} ? ".format(name)))
location = input("Where do you stay {} ".format(name))

print("Hello {}, you are {} years old and live in {}".format(name, age, location))

