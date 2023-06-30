from random import randint


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point_falls_in_rectangle(self, input_rectangle):

        if input_rectangle.point1.x < self.x < input_rectangle.point2.x and \
                input_rectangle.point1.y < self.y < input_rectangle.point2.y:
            return True
        return False

    def two_points_distance(self, input_point):
        return ((self.x - input_point.x) ** 2 + (self.y - input_point.y) ** 2) ** 0.5


point1 = Point(randint(0, 9), randint(0, 9))
point2 = Point(randint(10, 19), randint(10, 19))

random_rectangle = Rectangle(point1, point2)

user_guess_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
user_guess_area = float(input("Guess rectangle area: "))

print(f"Your point is inside the rectangle: {user_guess_point.point_falls_in_rectangle(random_rectangle)}")
print(f"Your area was of by: {random_rectangle.area() - user_guess_area} ")
