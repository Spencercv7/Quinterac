class Account:

    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance
        self.valid = True

    def setInvalid(self):
        self.valid = False
