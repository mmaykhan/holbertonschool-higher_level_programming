#!/usr/bin/python3
"""
Module 5-square
Defines a Square class with a method to print it using #
"""


class Square:
    """
    Class Square that defines a square and can print itself
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
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size with validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in stdout with the character #
        If size is 0, prints an empty line
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
