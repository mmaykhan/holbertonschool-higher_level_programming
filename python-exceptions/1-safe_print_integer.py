#!/usr/bin/python3
"""
Module 1-safe_print_integer
Contains a function that prints an integer safely
"""


def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format()
    Args:
        value: Can be any type
    Returns:
        True if value has been correctly printed, otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
