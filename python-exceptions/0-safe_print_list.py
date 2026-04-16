#!/usr/bin/python3
"""
Module 0-safe_print_list
Prints x elements of a list
"""


def safe_print_list(my_list=[], x=0):
    """
    Function that prints x elements of a list.
    Returns the real number of elements printed.
    """
    nb_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nb_print += 1
        except IndexError:
            break
    print("")
    return nb_print
