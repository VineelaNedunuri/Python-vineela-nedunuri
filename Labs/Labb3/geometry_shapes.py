from __future__ import annotations


class Geometry:  # create main class as Geometry
    def __init__(self, x: int | float, y: int | float) -> None:  # x, y are co- ordinates
        # assigns arguments to instance attributes
        self.x = x
        self.y = y

    # getter
    @property
    def x(self) -> int|float:
        return self._x

    # setter
    @x.setter
    def x(self, value):
        """Setter for value with error handling"""

        if not isinstance(value, (float, int)):
            raise TypeError(
                f"value must be an int or float, not {type(value).__name__}"
            )

        self._x = value

    # getter
    @property
    def y(self)-> int| float:
        return self._y

    # setter
    @y.setter
    def y(self, value):
        """Setter for value with error handling"""

        if not isinstance(value, (float, int)):
            raise TypeError(
                f"value must be an int or float, not {type(value).__name__}"
            )

        self._y = value

    # overrided dunder string method
    def __str__(self):
        return f"Geomerty with co-ordinates  x and y are {self.x}, {self.y}"

    # overrided dunder reper method
    def __repr__(self):
        return f"Geometry(x = {self.x}, y = {self.y})"
    
    
    # an operator overload of comparator operators <,>,<=,>= for comparison

    def __lt__(self, other)-> bool: # less than operator
        """ Less than operator to compare geometry shapes"""
        if type(self.area) < type(other.area):
            raise ValueError(f"Both areas must be same as int or float")
    
        return self.area < other.area
    
    def __le__(self, other)-> bool: # less than or equal to  operator
        """ Less than or operator to compare geometry shapes"""
        return self.area <= other.area
    
    def __gt__(self, other)-> bool: # greater than operator
        """ Greater than operator to compare geometry shapes"""
        return self.area > other.area
        
    def __ge__(self, other)-> bool: # greater than or equal to operator
        """ Greater than or equal operator to compare geometry shapes"""
        return self.area >= other.area


    # translate method that makes it possible to move x and y
    def translate(self, new_x, new_y):
        """ Translate is to move the position of geometry shape"""

        if not isinstance(new_x, (float, int)) or not isinstance(new_y, (float, int)):
            raise TypeError(f"value must be an int or float not {type(new_x).__name__}")

        self._x += new_x
        self._y += new_y
   
