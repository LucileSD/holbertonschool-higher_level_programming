#!/usr/bin/python3
"""
a function that prints the first x elements of a list and only integers

Arguments:
    my_list: the list can contain any type
    x: the number of elements to access in my_list

Return: the real number of integers printed

"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    element_printed = 0
    while x > 0:
        try:
            print("{:d}".format(my_list[count]), end="")
            x -= 1
            count += 1
        except TypeError:
            x -= 1
            count += 1
        except ValueError:
            x -= 1
            count += 1
        else:
            element_printed += 1
    print()
    return element_printed
