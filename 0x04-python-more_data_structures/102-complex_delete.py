#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for v in list(a_dictionary):
        if a_dictionary[v] == value:
            del a_dictionary[v]
    return a_dictionary
