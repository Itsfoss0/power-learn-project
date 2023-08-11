#!/usr/bin/env python3

import logging

# create a logger object
custom_logger = logging.getLogger("root")

# create the log handlers
file_handler = logging.FileHandler("application.log")
stream_handler = logging.StreamHandler()

# create formatters
f_formatter = logging.Formatter("%(asctime)s - %(name)s: %(levelname)s -> %(message)s")
s_formatter = logging.Formatter("%(asctime)s - %(name)s: %(levelname)s -> %(message)s")

# set the logging levels for the handlers
file_handler.setLevel(logging.WARNING)  # Capture all levels in the file
stream_handler.setLevel(logging.DEBUG)  # Capture DEBUG and INFO for stdout

# set the logging format for the handlers
file_handler.setFormatter(f_formatter)
stream_handler.setFormatter(s_formatter)

# add the handlers to the logger
custom_logger.addHandler(file_handler)
custom_logger.addHandler(stream_handler)

# Log messages
custom_logger.warning('This is a warning level log')
custom_logger.critical('This is a critical level log')
custom_logger.debug('Just debugging')
custom_logger.info('I hope this has been informative for you')
