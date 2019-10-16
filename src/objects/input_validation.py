from session_handler import SessionTypes

class InputValidation:

      def __init__(self, session_type)
          loggedIn = False
          sessionType = session_type


     def valid_account_num(accountNum):
          if accountNum > 9999999:
               return False 
          return True

     
     def valid_account_name(accountName):
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
          if session_type = SessionTypes.ATM:
               if 0 > amount or amount > atm_limit
                    return False
          if session_tyoe = SessionTypes.AGENT:
               if 0 > amount or amount > agent_limit:
                    return False
          return True


     
