from __future__ import annotations
from geometry_shapes import Geometry
import matplotlib.pyplot as plt

class Rectangle(Geometry):  # sub class
    """A Rectangle has length and width with four sides"""
    # override _init__()
    def __init__(self, x, y, length, width) -> None:
        super().__init__(x,y)
        self.length = length
        self.width = width
    
    #getter
    @property
    def length(self)-> int|float:
        return self._length

    # setter
    @length.setter
    def length(self, value):
        """Setter for value with error handling"""

        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be an int or float, not {type(value).__name__}")

        if value <= 0 :
            raise ValueError(f"You can only enter positive values")
        
        self._length = value

    # getter
    @property
    def width(self)-> int|float:
        return self._width
    
    # setter
    @width.setter
    def width(self, value):
        """Setter for value with error handling"""

        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be an int or float, not {type(value).__name__}")

        if value <= 0:
            raise ValueError(f"You can only enter non- neagtive values")
        
        self._width = value

     # to find area of rectangle : l*b
    @property      
    def area(self) -> int|float: 
        """To calculate the area of  Rectangle """
        return self.length*self.width 
    
    # To find perimeter of rectangle : 2l+2b
    @property 
    def perimeter(self) -> int|float:
        """To calculate the perimeter of  Rectangle """
        return 2 *self.length + 2* self.width 
    
    #  overrided dunder reper method
    def __repr__(self):
        return f"Rectangle(x = {self.x}, y = {self.y} , length={self.length}, width={self.width})"

    # overrided dunder string method
    def __str__(self):
        return f"Rectangle  with co-ordinates  x and y are {self.x}, {self.y} and length is {self.length} ,width is {self.width}"
    
    # overloaded equality (==) operator  
    def __eq__(self, other: Rectangle) -> bool:
        """ Checking equality condition for Rectangles"""
        if type(self.length) != type(other.length) and type(self.width) != type(other.width):
            raise TypeError(f"Both the length and width must be same as int or float")
        return (self.length == other.length) and (self.width == other.width)

    # a  method that checks whether point is inside or not in rectangle
    def is_inside_rec(self, x1, y1)-> bool:
        """ Checking  point inside or on rectangle """
        if not (isinstance(x1, (float,int)) or not isinstance(y1, (float,int))) :
            raise TypeError(f"Radius must be an int or float, not {type(x1).__name__}, {type(y1).__name__}")
 
        x_min = self.x - (self.length/2)
        x_max = self.x + (self.length/2)
        y_min = self.x - (self.width/2)
        y_max = self.x + (self.width/2)
        
        return (x_min <= x1 <= x_max ) and (y_min <= y1 <= y_max)
            
    # a method that checks if the rectangle instance is a square
    def square(self)-> None:
        """ Square should have smae length and same width"""
    
        if self.length == self.width:
           return print("Rectangle is a Square")
        else:
            return print("Rectangle is not a Square")
     
    # to plot circle
    def plot_rectangle(self):
        """ To draw Rectangle in co-ordinate axis"""
        fig, ax = plt.subplots()
        rectangle = plt.Rectangle((self.x ,self.y), self.length, self.width, alpha = 1)
        ax.add_patch(rectangle)
        ax.set_aspect(1)
        ax.autoscale()  
        ax.set(title="Rectangle", xlabel="x- axis", ylabel="y-axis")
        plt.show()

