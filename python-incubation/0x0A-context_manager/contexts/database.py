#!/usr/bin/env python3

"""
database resource handling context manager
"""

from MySQLdb import connect
from MySQLdb.cursors import DictCursor


class DatabaseConnection():
    """
    Database connection context manager
    to optimize database resource utilization
    when this class is instantiated, it binds the
    identier after the 'as' statement to a database cursor
    with the configurations passed when creating the object
    """

    def __init__(self, host: str, db_name: str, db_user: str, db_passwd: str):
        """
        The constructor
        Args:
            host (str): database host
            db_name (str): database name
            db_user (str): database username
            db_passwd (str): database password
        Returns:
            None
        """
        self.host = host
        self.db_name = db_name
        self.db_user = db_user
        self.db_passwd = db_passwd

    def __enter__(self):
        """"
        Enter state for the context manager
        """
        self.db_connection = connect(
            host=self.host,
            user=self.db_user,
            db=self.db_name,
            passwd=self.db_passwd
        )
        self.cursor = self.db_connection.cursor(cursorclass=DictCursor)
        return self.cursor

    def __exit__(self, *exec):
        """Exit state for the context manager"""
        self.cursor.close()
        self.db_connection.close()
