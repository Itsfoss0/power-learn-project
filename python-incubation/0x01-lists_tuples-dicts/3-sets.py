#!/usr/bin/env python3
"""
module to accept user input to create two sets of integers
and create a new set having common integers between the two
"""

set_1 = set(map(lambda x: int(x),
            set(input("Enter numbers seperated by space: ").split(" "))))
set_2 = set(map(lambda x: int(x),
            set(input("Enter numbers seperated by space: ").split(" "))))

new_set = set(set_1 & set_2)
print(new_set)
