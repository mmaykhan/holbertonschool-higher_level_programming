#!/usr/bin/python3
"""
Module 1-safe_print_integer
Function that prints an integer with "{:d}".format()
"""


def safe_print_integer(value):
    """
    Prints an integer and returns True if successful.
    Returns False if value is not an integer.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
