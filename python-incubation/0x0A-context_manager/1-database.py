#!/usr/bin/env python3

"""
This module test the functionality of the
DatabaseConnection context managers I've written
in the contexts package. Just using it for practice
"""

from contexts import DatabaseConnection

if __name__ == "__main__":
    with DatabaseConnection('localhost', 'todoist_db', 'root', 'root') as db:
        db.execute('SELECT name, email FROM app_users')
        results = db.fetchall()
        print(results)
