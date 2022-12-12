class Shape:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__('rectangle')
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__('triangle')
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

shapes = [
    Circle(5),
    Rectangle(3, 4),
    Triangle(6, 8)
]

for shape in shapes:
    print("Area of" + str(shape.get_type()) + str(shape.get_area()))