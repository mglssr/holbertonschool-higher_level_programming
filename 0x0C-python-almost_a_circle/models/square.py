#!/usr/bin/python3
"""10. And now, the Square!"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Write the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """generic comment"""
        return self.width

    @size.setter
    def size(self, value):
        """generic comment"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """generic comment"""
        if args is not None and len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.width = value
                        self.heigth = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """generic comment"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
