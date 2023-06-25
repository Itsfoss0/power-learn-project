#!/usr/bin/env python3

"""
Context manager for managing file resources
"""


class FileManager():
    """
    The FileManger instance will be bound to the
    identifier after the 'as' keyword and will provide
    an  object (file handler) for managing file resources
    """

    def __init__(self, file_name: str, o_mode: str):
        """
        The Constructor
        Args:
            file_name (str): Name of the file to open
            o_mode (str): Mode to open the file in
        Returns:
            None
        """
        self.file_name = file_name
        self.o_mode = o_mode

    def __enter__(self):
        """
        setup resources in the enter state
        """
        self.file_handler = open(self.file_name,
                                 mode=self.o_mode, encoding="utf-8")
        return self.file_handler

    def __exit__(self, *exit_args):
        self.file_handler.close()
