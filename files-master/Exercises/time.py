class Rectangle:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def distance_to_point(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2) ** 0.5
        return dist

    def time_to_point(self, x, y, speed):
        time = self.distance_to_point(x, y) / speed
        return time


rectangle = Rectangle(width=3, height=4, x=1, y=2)
print(rectangle.time_to_point(x=2, y=3, speed=20))
