class SimpleInterest:

    def __init__(self):
        self.principle = int(input('Enter the Priciple'))
        self.rate = int(input('Enter the Rate'))
        self.time = int(input('Enter the time'))

    def si(self):

        return self.principle * self.rate * self.time / 100

    def future_amount(self):

        return self.principle + self.si()
