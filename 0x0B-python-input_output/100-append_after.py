#!/usr/bin/python3
"""
     inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
        inserts a line of text to a file, after each line containing a
        specific string
        args:
            filename: the file
            search_string: the sentence searched
            new_string: the sentence which must been written
    """
    line_text = []
    with open(filename, "r+", encoding="utf-8") as buf:
        for line in buf:
            line_text.append(line)
            if search_string in line:
                line_text.append(new_string)

    with open(filename, "w", encoding="utf-8") as buf:
        buf.writelines(line_text)
