#!/usr/bin/python3
"""
Module 1-square
Defines a Square class with a private instance attribute size
"""


class Square:
    """
    Class Square that defines a square by its size
    """
    def __init__(self, size):
        """
        Initialize the square with a private size attribute
        Args:
            size: The size of the square (no type/value validation yet)
        """
        self.__size = size
