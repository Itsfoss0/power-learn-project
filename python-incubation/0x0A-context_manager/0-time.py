#!/usr/bin/env python3

"""
Module to test out the functionality of the
Timer context manager
"""
from time import sleep
from contexts import Timer

with Timer():
    sleep(2)