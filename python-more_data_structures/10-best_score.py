#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    # Find the key with the maximum value
    best = None
    max_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best = key

    return best
