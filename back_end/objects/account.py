class Account:

    def __init__(self, number, name, balance):
        self.number = None
        self.name = None
        self.balance = 0
        self.valid = True

    def setInvalid(self):
        self.valid = False
