#!/usr/bin/python3
"""
    Module to add indentation in a text
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
    these characters: ., ? and :"""
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(f"{text[i]}\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(f"{text[i]}", end="")
            i += 1
