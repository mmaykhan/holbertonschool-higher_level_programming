#!/usr/bin/python3
"""
Module 6-square
Defines a Square class with size, position and coordinate printing
"""


class Square:
    """
    Class Square that defines a square by size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square with size and position """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter for position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for position with strict validation """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns square area """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with # and uses spaces for position
        """
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan boşluq (position[1] qədər boş sətir)
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")

        # Kvadratın özü və soldan boşluq (position[0] qədər boşluq)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
