class Property():

    def __init__(self, owner, rent=0):
        self.owner = owner
        self.rent = rent

    def sell_to(self, acquiror, price):
        acquiror.pay(self.owner, price)
        self.owner = acquiror

    def pay_rent(self):
        pass
