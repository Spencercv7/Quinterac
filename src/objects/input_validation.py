from enum import Enum

class SessionTypes(Enum):
     ATM = 'atm'
     AGENT = 'agent'

class InputValidation:

     def __init__(self, session_type):
          self.session_type = session_type


     def valid_account_num(self, accountNum):
          if accountNum > 9999999:
               return False 
          return True

     
     def valid_account_name(self, accountName):
          if accountName[0] == ' ' or accountName[-1] == ' ':
               return False
          if 3 > len(accountName) or len(accountName) > 30:
               return False
          return True

     
     def valid_check_limits(self, atm_limit, agent_limit, amount):
          try:
               amount = int(amount)
          except ValueError:
               return False
          if self.session_type == SessionTypes.ATM:
               if (0 > amount or amount > atm_limit):
                    return False
          if self.session_type == SessionTypes.AGENT:
               if 0 > amount or amount > agent_limit:
                    return False
          return True


     
