class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

rectangle1 = Rectangle(height= 10, width= 15)
rectangle2 = Rectangle(height= 16, width= 11)

print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle2.area())
print(rectangle2.perimeter())

