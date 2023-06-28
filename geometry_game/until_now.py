

# 1. Create Rectangle class from two points lower_left and upper right
class Rectangle:
    def __init__(self, lower_left_point, upper_right_point):
        self.lower_left_point = lower_left_point
        self.upper_right_point = upper_right_point


# 2. Create Point class with x and y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 3. create method to check whether point is in rectangle
    def point_falls_in_rectangle(self, input_rectangle):
        if input_rectangle.lower_left_point.x < self.x < input_rectangle.upper_right_point.x \
                and input_rectangle.lower_left_point.y < self.y < input_rectangle.upper_right_point.y:
            return True
        return False

# 4. create method to check the distance between two points
    def calculate_distance(self, input_point):
        return ((self.x - input_point.x) ** 2 + (self.y - input_point.y)) ** 0.5


rectangle = Rectangle(Point(1, 1), Point(2, 2))
