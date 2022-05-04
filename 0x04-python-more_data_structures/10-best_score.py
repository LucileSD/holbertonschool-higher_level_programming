#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    if not a_dictionary:
        return None
    for score in a_dictionary.values():
        if score > biggest:
            biggest = score
    return list(
        a_dictionary.keys()
    )[list(a_dictionary.values()).index(biggest)]
