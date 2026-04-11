#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Square class with getter and setter """

    def __init__(self, size=0):
        """ Initialize square """
        self.size = size

    @property
    def size(self):
        """ Getter to retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter to set size with validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns current square area """
        return self.__size ** 2
