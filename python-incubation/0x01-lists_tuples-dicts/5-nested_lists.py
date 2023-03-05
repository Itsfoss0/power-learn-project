#!/usr/bin/env python3
"""
Nested lists challenge
"""

records = [["Chi", 20], ["alpha", 50], ["beta", 50]]

marks = {details[0]: details[1] for details in records}

print(marks)