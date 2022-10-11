from geometry_shapes import Geometry
import matplotlib.pyplot as plt
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

        if value <= 0 :
            raise ValueError(f"You can only enter positive values")
        
        self._length = value


    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        """Setter for value with error handling"""
      

        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be an int or float, not {type(value).__name__}")

        if value <= 0:
            raise ValueError(f"You can only enter non- neagtive values")
        
        self._width = value
    
    @property      
    def area(self) -> float: 
        """To calculate the area of  Rectangle """
        return self.length*self.width  # to find area of rectangle : l*b

    @property 
    def perimeter(self) -> float:
        """To calculate the perimeter of  Rectangle """
        return 2 *self.length + 2* self.width # To find perimeter of rectangle : 2l+2b
    
    def __repr__(self):
        return f"Rectangle(x = {self.x}, y = {self.y} , length={self.length}, width={self.width})"


    def __str__(self):
        return f"Rectangle  with co-ordinates  x and y are {self.x}, {self.y} and length is {self.length} ,width is {self.width}"
    
    # overloaded equality (==) operator  
    def __eq__(self, other) -> bool:
        return (self.length == other.length) and (self.width == other.width)

    # a  method that checks whether point is inside or not in rectangle
    def is_inside_rec(self, x1, y1)-> bool:
        """ Point inside or in rectangle must be in limits"""
        x_min = self.x - (self.length/2)
        x_max = self.x + (self.length/2)
        y_min = self.x - (self.width/2)
        y_max = self.x + (self.width/2)
        
        return (x_min <= x1 <= x_max ) and (y_min <= y1 <= y_max)
            
    # a method that checks if the rectangle instance is a square
    def square(self):
        """ Square should have smae length and same width"""
        if self.length == self.width:
           return print("Rectangle is a Square")
        else:
            return print("Rectangle is not a Square")
     
    # to plot circle
    def plot_rectangle(self):
        fig, ax = plt.subplots()
        rectangle = plt.Rectangle((self.x ,self.y), self.length, self.width, alpha = 1)
        ax.add_patch(rectangle)
        ax.set_aspect(1)
        ax.autoscale()  
        ax.set(title="Rectangle", xlabel="x- axis", ylabel="y-axis")
        plt.show()

