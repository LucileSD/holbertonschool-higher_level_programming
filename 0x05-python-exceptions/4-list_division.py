#!/usr/bin/python3
"""
a function that divides element by element 2 lists
Arguments:
    my_list_1: list of nominators
    my_list_2: list of denominators
    list_lenght: lenght of the new list which contains results
Return: the new list
"""


def list_division(my_list_1, my_list_2, list_length):
    count = 0
    new_list = [None] * list_length
    while list_length > 0:
        try:
            new_list[count] = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            print("division by 0")
            new_list[count] = 0
        except TypeError:
            print("wrong type")
            new_list[count] = 0
        except IndexError:
            print("out of range")
            new_list[count] = 0
        finally:
            list_length -= 1
            count += 1
    return new_list
