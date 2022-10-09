from __future__ import annotations
class Geometry(): # create main class as Geometry
    def __init__(self, x:(int|float), y:(int|float)): # x, y are co- ordinates 
        # assigns arguments to instance attributes 
        self.x = x
        self.y = y 

    # getter      
    @property   
    def x(self):
        return self._x 

    # setter    
    @x.setter
    def x(self, value):
        """Setter for value with error handling"""

        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be an int or float, not {type(value).__name__}")
        
        self._x = value

    # getter     
    @property
    def y(self):
        return self._y 

    #setter    
    @y.setter
    def y(self, value):
        """Setter for value with error handling"""

        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be an int or float, not {type(value).__name__}")
            
        self._y = value

    # overrided dunder string method
    def __str__(self):
        return f"Geomerty with co-ordinates  x and y are {self.x}, {self.y}"

    # overrided dunder reper method    
    def __repr__(self):
        return f"Geometry(x = {self.x}, y = {self.y})"
    
   
    # translate method that makes it possible to move x and y 
    def translate(self, new_x, new_y):
            self._x +=  new_x
            self._y +=  new_y
            
            if not isinstance(self._x, (float,int)):
                raise TypeError(f"value must be an int or float, not {type(self._x).__name__}")

            
            if type(new_x) or type(new_y) == str:
                raise ValueError(f" x  and y must be numbers not letter")

             
            return self._x, self._y          
        

       

g1 = Geometry(1,2)
print(g1)

g1.translate(7,2)
print(g1)
