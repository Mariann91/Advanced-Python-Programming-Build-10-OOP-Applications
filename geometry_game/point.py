class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Both parameters are tuples (1, 3) (2, 4)
    def falls_in_rectangle(self, rectangle):
        if rectangle.lower_left_point.x < self.x < rectangle.upper_right_point.x and \
                rectangle.lower_left_point.y < self.y < rectangle.upper_right_point.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        two_points_distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return two_points_distance
