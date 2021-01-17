class CompoundInterest:

    def __init__(self):
        self.principle = int(input('Enter the Priciple'))
        self.rate = int(input('Enter the Rate'))
        self.time = int(input('Enter the time'))

    def future_amount(self):

        return self.principle * (1 + self.rate/100)**self.time

    def interest(self):

        return self.future_amount() - self.principle


class XYZ:
    pass

class ABC:
    pass
