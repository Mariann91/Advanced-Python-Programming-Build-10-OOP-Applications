PAINT_FOR_SQ_UNIT = 2.5


class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return PAINT_FOR_SQ_UNIT * self.wall_area


class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets
