#!/usr/bin/python3
"""
Module 2-square
Defines a Square class with private size and validation
"""


class Square:
    """
    Class Square that defines a square by its size with validation
    """
    def __init__(self, size=0):
        """
        Initialize the square with validation
        Args:
            size (int): The size of the square (default 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
