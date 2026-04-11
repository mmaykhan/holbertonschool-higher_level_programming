#!/usr/bin/python3
"""
Module 4-square
Defines a Square class with getter and setter for size
"""


class Square:
    """
    Class Square that defines a square with controlled access to size
    """
    def __init__(self, size=0):
        """
        Initialize the square
        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter to retrieve the private __size attribute
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter to set the private __size attribute with validation
        Args:
            value (int): The new size value
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area
        Returns:
            The area of the square
        """
        return self.__size ** 2
