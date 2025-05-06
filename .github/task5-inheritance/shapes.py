import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle {self.width}×{self.height}"

# Example usage
if __name__ == "__main__":
    c = Circle(3)
    r = Rectangle(4, 5)
    print(c, "- Area:", c.area())
    print(r, "- Area:", r.area())
