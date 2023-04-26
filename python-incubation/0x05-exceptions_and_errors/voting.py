#!/usr/bin/env python3

"""Lets determine if a citizen is eligle to vote"""

citizens = {
    "john": 18,
    "jane": 22,
    "david": 19,
    "sean": 15,
    "pascal": 13,
    "charlie": 20,
    "dennis": 44,
    "marrisa": 31,
    "wendy": 24,
    "mercy": 21
}


def can_vote(citizen: str) -> str:
    """
    Can this citizen be allowed to vote
    Args:
        citizen(str): Name of the citizen
    """
    if not isinstance(citizen, str):
        raise TypeError("Provide the right name of the citizen")
    if citizen not in citizens.keys():
        raise KeyError(f"'{citizen}' is not in the Government Database")
    else:
        if citizens.get(citizen) < 18:
            raise ValueError(f"{citizen} is too young to vote")
        else:
            return f"{citizen} just cast their vote"


if __name__ == "__main__":
    while True:
        try:
            print(can_vote(input("Citizen's name: ").strip()))
        except Exception as e:
            print(e)
        else:
            break
