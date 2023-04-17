#!/usr/bin/env python3

"""
My dictionary module
"""

from json import load
from difflib import get_close_matches

class MyDictionary:
    """
    dictionary to find word definitions from
    A data set
    """
    data_set="data.json"

    def __init__(self, search_term: str) -> str:
        """
        The constructor
        Args:
            search_term (str): the term to search for
        """
        self.search_term = search_term

    def __repr__(self):
        return "Search: {}".format(self.search_term)

    def search_word(self):
        try:
            with open(self.__class__.data_set, 'r', encoding="utf-8") as data:
                full_dictionary = load(data)
            match = get_close_matches(self.search_term, full_dictionary.keys(), n=1)
            definition = full_dictionary[match[0]][0]
            return "{} is {}".format(self.search_term, definition)

        except FileNotFoundError:
            return "Cannot find {}".format(self.__class__.data_set)

if __name__ == "__main__":
    search_1 = MyDictionary('Computer')
    print(search_1.search_word())

    search_2 = MyDictionary('docker')
    print(search_2.search_word())

    search_3 = MyDictionary('Kubernetes')
    print(search_3.search_word())