from __future__ import annotations
from geometry_shapes import Geometry
import math
import matplotlib.pyplot as plt

# create sub class of Geometry
class Circle(Geometry): 
    """A Circle has radius"""
    def __init__(self, x, y, radius) -> None:
        super().__init__(x,y)
        self.radius = radius
    
    # getter
    @property    
    def radius(self)->int|float: 
        return self._radius

    # setter 
    @radius.setter
    def radius(self, value):
        """Setter for value with error handling"""

        if not isinstance(value, (float,int)):
            raise TypeError(f"Radius must be an int or float, not {type(value).__name__}")
 
        if value <= 0:
            raise ValueError(f"You can only enter non- neagtive values")
        
        self._radius = value
    
    # to find out area of circle: pi*r**2
    @property
    def area(self)->int|float: 
        """To calculate the area of Circle """
        return math.pi*(self._radius **2)

     # to find out circumference of circle: 2*pi*r
    @property
    def circumference(self)->int|float:
        """To calculate the circumference of Circle """
        return 2* math.pi *self._radius
   
     
    # overrided dunder reper method   
    def __repr__(self):
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"

    # overrided dunder string method
    def __str__(self):
        return f"circle with co-ordinates  x and y are {self.x}, {self.y} and the radius is {self.radius}"

    # overloaded equality (==) operator  
    def __eq__(self, other:Circle) -> bool:
        """ Checking equality condition for Circles"""
        if type(self.radius) != type(other.radius):
            raise TypeError(f"Both the radius must be same like int or float")
        return self.radius == other.radius
        
    
    # a method that checks if the point is inside the ciecle or not

    def is_inside(self, x1, y1)-> bool: 
        """Cicle point is inside or on boundary """ 
        if not (isinstance(x1, (float,int)) or not isinstance(y1, (float,int))) :
            raise TypeError(f"Radius must be an int or float, not {type(x1).__name__}, {type(y1).__name__}")
 
        return math.sqrt((self.x - x1)**2 + (self.y - y1)**2) <= self.radius**2
    
             
    # a method that checks if the circle instance is a unit circle
    def unit_circle(self):
        """ Unit circle is the circle of radius is one at the origin"""
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return print("It is a Unit Circle")


    # to plot circle
    def plot_circle(self):
        """ To draw Rectangle in co-ordinate axis"""
        fig, ax = plt.subplots()
        circle1 = plt.Circle((self.x ,self.y), self.radius, color = 'r', alpha = 1)
        ax.add_patch(circle1)
        ax.set_aspect(1)
        ax.autoscale()  
        ax.set(title="Circle", xlabel="x-axis", ylabel="y-axis")
        plt.show()

