#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If ssize is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
