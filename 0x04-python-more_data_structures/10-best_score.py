#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = max(a_dictionary.values())
    for i, j in a_dictionary.items():
        if j == best:
            return i
