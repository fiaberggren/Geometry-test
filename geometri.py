#Python 3.6.2, Windows 10
#Fia Berggren Lindqvist
#Labbpartner: Kristina Ckalla

import math

class Punkt():
    
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

    def __str__(self):
        return "Point: (" + str(self.__x) + ", " + str(self.__y) + ")"


class Cirkel(Punkt):

    def __init__(self, radie, x = 0, y = 0):
        Punkt.__init__(self, x, y)
        self.__radie = radie

    def get_radie(self):
        return self.__radie

    def get_area(self):
        return math.pi * (self.__radie ** 2)

    def get_circumference(self):
        return math.pi * 2 * self.__radie

    def __eq__(self, other):
        return self.__radie == other.get_radie() and Punkt.__eq__(self, other)

    def __str__(self):
        return "Circle with the radius: " + str(self.__radie) + " and x = " + str(self.get_x()) + ", y = " + str(self.get_y())


#You create a class where you calculate the area and circumference of the rectangle, just like the circle above, this class inherits its instances from the Point class        
class Rektangel(Punkt):

    #Here below with __init__ we define the object's attributes and give them values
    def __init__(self, height, width, x = 0, y = 0):
        Punkt.__init__(self, x, y)
        self.__height = height
        self.__width = width

    #A defined method that retrieves attributes from _init_ and then returns to it, since it is private, it must be given access
    def get_height(self):
        return self.__height

    #A defined method that retrieves attributes from _init_ and then returns to it, since it is private, it must be given access
    def get_width(self):
        return self.__width

    #Here below, the height multiplies the width to calculate the area
    def get_area(self):
        return self.__height * self.__width

    #Below, you multiply the height twice, and the width twice separately to then add them, to get the perimeter of the rectangle
    def get_circumference(self):
        return (self.__height * 2) + (self.__width * 2)
    
    #__eq__ below compares two values against each other and gives a boolean value in response (True or False)
    def __eq__ (self, other):
        return self.__height == other.get_height() and self.__width == other.get_width() and Punkt.__eq__(self, other)

    #Below, everything is transformed into a string
    def __str__(self):
        return "Rectangle with the base: " + str(self.__width) + " and with the height: " + str(self.__height)
    
#You create a class where you calculate the area and circumference of the triangle, just like the other classes above, this class also inherits its instances from the Point class
class Triangel(Punkt):

    #Here below with __init__ we define the object's attributes and give them values
    def __init__(self, height, width, length, x = 0, y = 0):
        Punkt.__init__(self, x, y)
        self.__height = height
        self.__width = width
        self.__length = length

    #A defined method that retrieves attributes from _init_ and then returns to it, since it is private, it must be given access
    def get_height(self):
        return self.__height
    
    #A defined method that retrieves attributes from _init_ and then returns to it, since it is private, it must be given access
    def get_width(self):
        return self.__width

    #A defined method that retrieves attributes from _init_ and then returns to it, since it is private, it must be given access
    def get_length(self):
        return self.__length

    #Below, the height is multiplied by the width and then divided by two to give the area of the triangle
    def get_area(self):
        return (self.__height * self.__width) / 2

    #Below, it adds the three sides of the triangle to bring out the circumference
    def get_circumference(self):
        return self.__height + self.__width + self.__length

    #__eq__ below compares two values against each other and gives a boolean value in response (True or False)
    def __eq__ (self, other):
        return self.__height == other.get_height() and self.__width == other.get_width() and self.__length == other.get_length() and Punkt.__eq__(self, other)

    #Below, everything is transformed into a string
    def __str__(self):
        return "Triangle with the base: " + str(self.__width) + " and with the height: " + str(self.__height) + " and with the length: " + str(self.__length)
