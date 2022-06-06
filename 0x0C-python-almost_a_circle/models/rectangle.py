#!/usr/bin/python3
"""2. First Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Write the class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class contructor __init__"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """generic comments"""
        return self.__height

    @property
    def width(self):
        """generic comments"""
        return self.__width

    @property
    def x(self):
        """generic comments"""
        return self.__x

    @property
    def y(self):
        """generic comments"""
        return self.__y

    @height.setter
    def height(self, height):
        """generic comments"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @width.setter
    def width(self, width):
        """generic comments"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @x.setter
    def x(self, x):
        """generic comments"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """generic comments"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """generic comments"""
        return self.__height * self.__width

    def display(self):
        """generic comments"""
        out = ""
        out += "\n" * self.__y
        for i in range(self.__height):
            out += str(" " * self.__x)
            for j in range(self.__width):
                out += str('#')
            out += "\n"
        print(out[:-1])

    def __str__(self):
        """generic comments"""
        return(f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """generic comments"""
        if args is not None and len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.__width = arg
                elif i == 3:
                    self.__height = arg
                elif i == 4:
                    self.__x = arg
                elif i == 5:
                    self.__y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """generic comments"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
