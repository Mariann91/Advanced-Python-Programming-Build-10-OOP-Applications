class Flatmate:
    """
    Create flatmate object that receive name and days in house and calculate share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    # the method calculates flatmate share of the bill
    def pays(self, bill, other_flatmate):
        share = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house) * bill.amount
        return share
