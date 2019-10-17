
# Library Imports
from enum import Enum

# Object Imports
from objects.input_validation import InputValidation
from objects.transaction_summary import TransactionSummary
from objects.valid_accounts import ValidAccounts

#Helps to track which type of session is in use using constant values
class SessionTypes(Enum):
     ATM = 'atm'
     AGENT = 'agent'

class SessionHandler:
     #Attributes of class that are used to track the state of the class
     def __init__(self, valid_account_file, trans_summary_file):
          self.logged_in = False
          self.session_type = None
          self.validator = None  #will hold an InputValidation object
          self.trans_summary_file = trans_summary_file #reference to the path of the transaction summary file
          self.trans_summary = None  #will hold a TransactionSummary object
          self.valid_account_list = ValidAccounts(valid_account_file) #creates ValidAccount object created from valid account file
          self.withdraw_dict = {}   #dictionaries used to track ATM daily use limits
          self.transfer_dict = {}
          self.deposit_dict = {}

     #Prompts the user for a command and sends it to handle_command
     def get_command(self):
          if (not self.logged_in):
               print("\nType Login to login or Type Exit to End Program")
               command = input("Command: ")
          else:
               command = input("\nCommand: ")
          return self.handle_command(command.lower())

     #Handles the given command and sends it to the correct method, makes sure user can do command in their current session type
     #Return value indicates if the program not end
     def handle_command(self, command):
          if (not self.logged_in):
               if (command == "login"):
                    self.login()
               elif (command =="exit"):
                    print("Exiting System")
                    return False
               else:
                    print("Must login before doing an alternative command")
          else:
               if (command == "login"):
                    print("Session already logged in")
               elif (command == "logout"):
                    self.logout()
               elif ((command == "createacct" or command == "deleteacct") and self.session_type == SessionTypes.ATM):
                    print("Cannot perform command in ATM mode")
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
          return True


     #Handles login of the sessoin and prompts the user with which type of session they require
     def login(self):
          while (not self.logged_in):
               session = input("Machine or Agent: ")
               session = session.lower()
               if (session == "machine"):
                    print("\nATM Session Commands:\nTransfer Funds - transfer\nWithdraw Funds - withdraw\nDeposit Funds - deposit\nLogout - logout")
                    self.session_type = SessionTypes.ATM
                    self.validator = InputValidation(self.session_type)
                    self.trans_summary = TransactionSummary(self.trans_summary_file)
                    self.logged_in = True
               elif (session == "agent"):
                    print("\nAgent Session Commands:\nCreate Account - createacct\nDelete Account - deleteacct\nTransfer Funds - transfer\nWithdraw Funds - withdraw\nDeposit Funds - deposit\nLogout - logout")
                    self.session_type = SessionTypes.AGENT
                    self.validator = InputValidation(self.session_type)
                    self.trans_summary = TransactionSummary(self.trans_summary_file)
                    self.logged_in = True
               else:
                    print("Invalid Input")

     #closes transaction summary file and resets all attributes of the session
     def logout(self):
          self.logged_in = False
          self.session_type = None
          self.trans_summary.transaction_close()
          self.withdraw_dict = {}
          self.transfer_dict = {}
          self.deposit_dict = {}
          print("Session Logged Out")

     
     def createacct(self):
          print("Create New Account")
          account_num = input("New Account Number: ")
          account_name = input("New Account Name: ")
          #Check if account number and name are in the correct format
          if (self.validator.valid_account_num(account_num) and self.validator.valid_account_name(account_name)):
               #Check if the account number is not in the valid account list
               if (not self.valid_account_list.contains_account(account_num)):
                    print("Account Created")
                    self.trans_summary.add_transaction(transaction_type="NEW", to_account=account_num, name=account_name) #sends transaction to be written to file
               else:
                    print("Account Number Already in Use")
          else:
               print("Invalid Account Number or Name")          


     def deleteacct(self):
          print("Delete Account")
          account_num = input("Account Number: ")
          account_name = input("Account Name: ")
          #Check if account number and name are in the correct format
          if (self.validator.valid_account_num(account_num) and self.validator.valid_account_name(account_name)):
               #Check if the account number is in the valid account list
               if (self.valid_account_list.contains_account(account_num)):
                    print("Account Deleted")
                    self.valid_account_list.delete_account(account_num)
                    self.trans_summary.add_transaction(transaction_type="DEL", to_account=account_num, name=account_name) #sends transaction to be written to file
               else:
                    print("Account Number Not In Use")
          else:
               print("Invalid Account Number or Name") 


     def withdraw(self):
          print("Withdrawal")
          account_num = input("Account Number: ")
          amount = input("Withdrawal Amount: ")
          #Check if account number is valid and if amount is valid and in correct range
          if (self.validator.valid_account_num(account_num) and self.validator.valid_amount(100000, amount)):
               #Checks if account is in valid account list
               if (self.valid_account_list.contains_account(account_num)):
                    #If in Agent mode does not need to track daily limit
                    if (self.session_type == SessionTypes.AGENT):
                         self.trans_summary.add_transaction(transaction_type="WDR", to_account=account_num, amount=amount) #sends transaction to be written to file
                         print("Withdrawal Completed")
                    else:
                         #Checks if the daily limit stored in the withdraw dictionary has been reached
                         if (account_num in self.withdraw_dict):
                              if (self.withdraw_dict[account_num] + int(amount) > 500000):
                                   print("Exceeded ATM Withdrawal Limit")
                              else:
                                   self.withdraw_dict[account_num] = self.withdraw_dict[account_num] + int(amount)
                                   self.trans_summary.add_transaction(transaction_type="WDR", to_account=account_num, amount=amount) #sends transaction to be written to file
                                   print("Withdrawal Completed")
                         else:
                              self.withdraw_dict[account_num] = int(amount)
                              self.trans_summary.add_transaction(transaction_type="WDR", to_account=account_num, amount=amount) #sends transaction to be written to file
                              print("Withdrawal Completed")
               else:
                    print("Account Number Not In Use")
          else:
               print("Invalid Account Number or Amount")


     def deposit(self):
          print("Deposit")
          account_num = input("Account Number: ")
          amount = input("Deposit Amount: ")
          #Check if account number is valid and if amount is valid and in correct range
          if (self.validator.valid_account_num(account_num) and self.validator.valid_amount(200000, amount)):
               #Checks if account is in valid account list
               if (self.valid_account_list.contains_account(account_num)):
                    #If in Agent mode does not need to track daily limit
                    if (self.session_type == SessionTypes.AGENT):
                         self.trans_summary.add_transaction(transaction_type="DEP", to_account=account_num, amount=amount) #sends transaction to be written to file
                         print("Deposit Completed")
                    else:
                         #Checks if the daily limit stored in the deposit dictionary has been reached
                         if (account_num in self.deposit_dict):
                              if (self.deposit_dict[account_num] + int(amount) > 500000):
                                   print("Exceeded ATM Deposit Limit")
                              else:
                                   self.deposit_dict[account_num] = self.deposit_dict[account_num] + int(amount)
                                   self.trans_summary.add_transaction(transaction_type="DEP", to_account=account_num, amount=amount) #sends transaction to be written to file
                                   print("Deposit Completed")
                         else:
                              self.deposit_dict[account_num] = int(amount)
                              self.trans_summary.add_transaction(transaction_type="DEP", to_account=account_num, amount=amount) #sends transaction to be written to file
                              print("Deposit Completed")
               else:
                    print("Account Number Not In Use")
          else:
               print("Invalid Account Number or Amount")


     def transfer(self):
          print("Transfer")
          to_account_num = input("To Account Number: ")
          from_account_num = input("From Account Number: ")
          amount = input("Transfer Amount: ")
          #Check if account numbers are valid and if amount is valid and in correct range
          if (self.validator.valid_account_num(to_account_num) and self.validator.valid_account_num(from_account_num) and self.validator.valid_amount(1000000, amount)):
               #Checks if accounts are in valid account list
               if (self.valid_account_list.contains_account(to_account_num) and self.valid_account_list.contains_account(from_account_num)):
                    #If in Agent mode does not need to track daily limit
                    if (self.session_type == SessionTypes.AGENT):
                         self.trans_summary.add_transaction(transaction_type="XFR", to_account=to_account_num, amount=amount, from_account=from_account_num) #sends transaction to be written to file
                         print("Transfer Completed")
                    else:
                         #Checks if the daily limit stored in the transfer dictionary has been reached
                         if (from_account_num in self.transfer_dict):
                              if (self.transfer_dict[from_account_num] + int(amount) > 1000000):
                                   print("Exceeded ATM Transfer Limit")
                              else:
                                   self.transfer_dict[from_account_num] = self.transfer_dict[from_account_num] + int(amount)
                                   self.trans_summary.add_transaction(transaction_type="XFR", to_account=to_account_num, amount=amount, from_account=from_account_num) #sends transaction to be written to file
                                   print("Transfer Completed")
                         else:
                              self.transfer_dict[from_account_num] = int(amount)
                              self.trans_summary.add_transaction(transaction_type="XFR", to_account=to_account_num, amount=amount, from_account=from_account_num) #sends transaction to be written to file
                              print("Transfer Completed")
               else:
                    print("An Account Number Is Not In Use")
          else:
               print("Invalid Account Number or Amount")
