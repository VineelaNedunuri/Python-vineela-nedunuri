from geometry_shapes import Geometry

class Rectangle(Geometry):
    """A Rectangle has length and width with four sides"""
    # override _init__()
    def __init__(self, x, y, length, width) -> None:
        super().__init__(x,y)
        self.length = length
        self.width = width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        """Setter for value with error handling"""
      

        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be an int or float, not {type(value).__name__}")

        if not (0<= value ):
            raise ValueError(f"You can only enter non- neagtive values")
        
        self._length = value


    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        """Setter for value with error handling"""
      

        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be an int or float, not {type(value).__name__}")

        if not (0<= value ):
            raise ValueError(f"You can only enter non- neagtive values")
        
        self._width = value
    
    @property      
    def area(self) -> float: 
        """To calculate the area of  Rectangle """
        return self._length*self._width  # to find area of rectangle : l*b

    @property 
    def perimeter(self) -> float:
        """To calculate the perimeter of  Rectangle """
        return 2 *self._length + 2* self._width # To find perimeter of rectangle : 2l+2b
    
    def __repr__(self):
        return f"Rectangle(x = {self.x}, y = {self.y} , length={self.length}, width={self.width})"


    def __str__(self):
        return f"Rectangle  with co-ordinates  x and y are {self.x}, {self.y} and length is {self.length} ,width is {self.width}"
    
    # overloaded equality (==) operator  
    def __eq__(self, other) -> bool:
        return (self.length == other.length) and (self.width == other.width)

    # an operator overload of comparator operators <,>,<=,>= for comparison

    def __lt__(self, other)-> bool: # less than operator
        return self.perimeter < other.perimeter
    
    def __le__(self, other)-> bool: # less than or equal to  operator
        return self.perimeter <= other.perimeter
    
    def __gt__(self, other)-> bool: # greater than operator
        return self.perimeter > other.perimeter
        
    def __ge__(self, other)-> bool: # greater than or equal to operator
        return self.perimeter >= other.perimeter

rectangle1 = Rectangle(4,4,4,5)
print(rectangle1.area)
print(rectangle1.perimeter)
