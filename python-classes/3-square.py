#!/usr/bin/python3
"""
Module 3-square
Defines a Square class with private size, validation and area method
"""


class Square:
    """
    Class Square that defines a square by its size and calculates area
    """
    def __init__(self, size=0):
        """
        Initialize the square with validation
        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area
        Returns:
            The area of the square (size squared)
        """
        return self.__size ** 2
