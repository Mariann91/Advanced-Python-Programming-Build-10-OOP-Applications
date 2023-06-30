from point import Point, GraphicalPoint
from rectangle import Rectangle, GraphicalRectangle
from random import randint
import turtle

random_lower_left_point = Point(randint(0, 400), randint(0, 400))
random_upper_right_point = Point(randint(10, 400), randint(10, 400))

rectangle = Rectangle(random_lower_left_point, random_upper_right_point)

print("Guess a point that is in a random rectangle: ")
user_guess = GraphicalPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess and area: "))

print(f"Rectangle Coordinates: {rectangle.point1.x, rectangle.point1.y} "
      f"and {rectangle.point1.y, rectangle.point2.y}")

print("Your point is inside the rectangle: ", end="")
print(user_guess.falls_in_rectangle(rectangle))
print(f"Your area was of by {rectangle.rectangle_area() - user_area}")

canvas_turtle = turtle.Turtle()

graphical_rectangle = GraphicalRectangle(random_lower_left_point, random_upper_right_point)
graphical_rectangle.draw(canvas_turtle)

graphical_point = GraphicalPoint(user_guess.x, user_guess.y)
graphical_point.draw(canvas_turtle)

turtle.done()
