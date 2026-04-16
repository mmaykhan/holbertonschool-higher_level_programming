#!/usr/bin/python3
"""
Module 4-list_division
Divides element by element 2 lists
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists.
    Handles TypeError, ZeroDivisionError, and IndexError.
    """
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
