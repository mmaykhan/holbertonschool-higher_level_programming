#!/usr/bin/python3
"""
Module 3-safe_print_division
Divides 2 integers and prints the result in finally block
"""


def safe_print_division(a, b):
    """
    Divides two integers and prints the result using finally.
    Returns: Result of division or None.
    """
    div_result = None
    try:
        div_result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(div_result))
    return div_result
