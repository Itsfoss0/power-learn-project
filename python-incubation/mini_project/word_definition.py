#!/usr/bin/env python3
"""
Module to the definition(s) of a word in
a dictionary, by finding the closest match(es)

Usage: ./word_defintion.py <word>
"""
from sys import argv, exit
from json import load
from difflib import get_close_matches


def find_word_definition(word: str, dictionary: str) -> list:
    """
    Find the dictionary defition of a word
    Args:
        word (str): The word to find its definition
        dictionary (str): The dictionary to compare agains
    Return:
        list of match words
    """
    try:
        with open(dictionary, 'r', encoding="utf-8") as dictionary_file:
            dict_words = load(dictionary_file)

        matches = get_close_matches(word, dict_words.keys(), n=2, cutoff=0.8)
        return matches
    except FileNotFoundError:
        return "Cannot find the dictionary file"


if __name__ == "__main__":
    if len(argv) < 3:
        print('Usage: ./word_definition.py <word> <dictionary_file>')
        exit(-1)
    matched_words = find_word_definition(str(argv[1]).strip().lower(), argv[2])
    with open(argv[2], 'r', encoding="utf-8") as data_set:
        data = load(data_set)

    for word in matched_words:
        print("{} can mean {}".format(word, data[word][0]))
