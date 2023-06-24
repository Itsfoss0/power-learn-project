#!/usr/bin/env python3

"""
Module with the timing context manager
to demonstreate the various uses and
applications of context managers
"""

import time


class Timer():
    """
    Timer class, whose objects will
    be used as context managers
    to compute the execution time of an op
    """

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *exec):
        self.end_time = time.time()
        t_time = self.end_time - self.start_time
        print(f"execution took {int(t_time)} seconds")
