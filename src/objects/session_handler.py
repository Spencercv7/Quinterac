from enum import Enum

class SessionTypes(Enum):
     ATM = 'atm'
     AGENT = 'agent'

class SessionHandler:
# Check if logged in, create agent or atm session, handle highlevel commands, loggout.

     def __init__(self, validAccountList):
          self.logged_in = False
          self.session_type = None
          self.validAccountList = validAccountList
          self.withdraw_dict = {}
          self.transfer_dict = {}
          self.deposit_dict = {}

     def login(self):
          while (not self.logged_in):
               session = input("ATM or Agent: ")
               session = session.lower()
               if (session == "atm"):
                    print("Session Type set to Atm")
                    self.session_type = SessionTypes.ATM
                    self.logged_in = True
               elif (session == "agent"):
                    print("Session Type set to Agent")
                    self.session_type = SessionTypes.AGENT
                    self.logged_in = True
               else:
                    print("Invalid Input")


     def logout(self):
          print("logging out")


     def get_command(self, command):
          if (not self.logged_in):
               if (command == "login"):
                    self.login()
               else:
                    print("Must login before doing a command")
          else:
               if (command == "login"):
                    print("Session already logged in")
               elif (command == "logout"):
                    self.logout()
               elif ((command == "createacct" or command == "deleteacct") and self.session_type == "atm"):
                    print("cannot perform command in atm mode")
               elif (command == "createacct"):
                    self.createacct()
               elif (command == "deleteacct"):
                    self.deleteacct()
               elif (command == "withdraw"):
                    self.withdraw()
               elif (command == "transfer"):
                    self.transfer()
               elif (command == "deposit"):
                    self.deposit()
               else:
                    print("Invalid Input")


     def createacct(self):
          print("Creating account")


     def deleteacct(self):
          print("Deleting account")



     def withdraw(self):
          print("Withdrawing")


     def deposit(self):
          print("Depositing")


     def transfer(self):
          print("Transfering")
