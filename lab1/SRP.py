import math

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def get_radius(self):
    return self.radius

  def set_radius(self, radius):
    self.radius = radius

  def get_area(self):
    return math.pi * self.radius * self.radius

class CirclePrinter:
  def print_circle(self, circle):
    print("Radius: " + str(circle.get_radius()))
    print("Area: " + str(circle.get_area()))

radius = input("Enter the radius of the circle: ")

circle = Circle(float(radius))

printer = CirclePrinter()
printer.print_circle(circle)


