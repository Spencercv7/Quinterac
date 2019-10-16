class SessionType:

# Hold min and max values for diffrent session types. Bunch of getters.

    def __init__(self, type):
        if (type == 'Agent'):
            self.type = 'Agent'
            self.max_WDR = 99999999
            self.max_DEP = 99999999
            self.max_XFR = 99999999
        else:
            self.type = 'Atm'
            self.max_DEP = 200000
            self.max_WDR = 100000
            self.max_XFR = 1000000
            self.day_limit_DEP = 500000
            self.day_limit_WDR = 500000
            self.day_limit_XFR = 1000000