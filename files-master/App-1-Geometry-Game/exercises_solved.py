class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return self.wall_area * 2.5


class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class DiscountedPaint(Paint):

    def discounted_price(self, discount_percentage):
        price_without_discount = self.total_price()
        discount = price_without_discount * (discount_percentage / 100)
        final_price = price_without_discount - discount
        return final_price
