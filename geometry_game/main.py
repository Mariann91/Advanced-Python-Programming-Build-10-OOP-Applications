from point import Point
from rectangle import Rectangle

point1 = Point(1, 1)
point2 = Point(3, 3)

rectangle = Rectangle(Point(5, 6), Point(7, 9))

print(point1.falls_in_rectangle(rectangle))

