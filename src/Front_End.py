import sys

# Object Imports
from objects.transaction_summary import TransactionSummary
from objects.input_validation import InputValidation
from objects.valid_accounts import ValidAccounts
from objects.session_handler import SessionHandler


def frontend(accountList, transactionSummary):
     print(accountList, transactionSummary)
     validAccountList = ValidAccounts(accountList)
     sessionHandler = SessionHandler(validAccountList)
    
     running = True
     while (running):
          input_command = input("What would you like to do: ")
          if (input_command == "exit"):
               running = False
          else:
               sessionHandler.get_command(input_command)


accountFile = sys.argv[1]
transFile = sys.argv[2]
frontend(accountFile, transFile)