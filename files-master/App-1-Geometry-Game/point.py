class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and \
                rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        two_points_distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return two_points_distance


class GraphicalPoint(Point):

    def draw(self, canvas, size=15, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
