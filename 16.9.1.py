class Figures:
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"

rect1 = Figures(2, 4, 10, 20)
print(rect1)

