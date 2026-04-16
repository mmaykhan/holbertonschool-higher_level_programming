#!/usr/bin/python3
"""
Module 2-safe_print_list_integers
Prints only integers from the first x elements of a list
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints integers from a list and skips other types silently.
    Returns the number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
