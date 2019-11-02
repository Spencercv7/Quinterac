import sys
import os

# Library Imports
from enum import Enum

# Enum class for tracking session type.
class SessionTypes(Enum):
     ATM = 'atm'
     AGENT = 'agent'

# Validates all terminal input and validates amounts.
class InputValidation:

     def __init__(self, session_type):
          self.session_type = session_type

     # Varifies that account number is not larger or smaller then 7 digits.
     def valid_account_num(self, accountNum):
          try:
               accountNum = int(accountNum)
          except ValueError:
               return False
          if accountNum > 9999999 or accountNum < 1000000:
               return False 
          return True

     # Varifies that account name is no shorter then 3 and no longer then 30.
     # Does not check for leading or ending spaces as these are ignored in Python terminal
     def valid_account_name(self, accountName):
          accountName = str(accountName)
          if 3 >= len(accountName) or len(accountName) >= 30:
               return False
          return True

     # Varifies that amount is of type integer and that it is within permission 
     # for session type.
     def valid_amount(self, atm_limit, amount):
          try:
               amount = int(amount)
          except ValueError:
               return False
          if self.session_type.value == SessionTypes.ATM.value:
               if (0 > amount or amount > atm_limit):
                    return False
          elif self.session_type.value == SessionTypes.AGENT.value:
               if 0 > amount or amount > 99999999:
                    return False
          return True


     
