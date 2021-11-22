class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_square(self):
        return self.a * self.b

sq1 = Rectangle(5, 8)
print(sq1.set_square())
