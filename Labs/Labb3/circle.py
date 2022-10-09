from geometry_shapes import Geometry
import math
class Circle:
    """A Circle has radius"""
    def __init__(self, x, y, radius) -> None:
        super().__init__(x,y)
        self.radius = radius
    
    # getter
    @property    
    def radius(self): 
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
    

    @property
    def area(self): # to find out area of circle: pi*r**2
        """To calculate the area of Circle """
        return math.pi*(self._radius **2)
    
    @property
    def circumference(self): # to find out circumference of circle: 2*pi*r
        """To calculate the circumference of  Rectangle """
        return 2* math.pi *self._radius
   
     
    # overrided dunder reper method   
    def __repr__(self):
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"

    # overrided dunder string method
    def __str__(self):
        return f"circle with co-ordinates  x and y are {self.x}, {self.y} and the radius is {self.radius}"
