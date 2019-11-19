class Account:

    def __init__(self, number, name, balance = 0):
        self.number = number
        self.name = name
        self.balance = balance
        self.valid = True

    def __string__(self):
        return ""

    def setInvalid(self):
        self.valid = False
