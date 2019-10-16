import sys

# Object Imports
from objects.transaction_summary import TransactionSummary
from objects.input_validation import InputValidation
from objects.valid_accounts import ValidAccounts
from objects.session_types import Agent, Atm

sessionType = None



def frontend(accountList, transactionSummary):
     print(accountList, transactionSummary)
     session = input("Input Session Type: ")
     if session == "Agent" or session == "agent":
          sessionType = Agent()
     elif session == "ATM" or session == "atm":
          sessionType == Atm()
     else:



perm1 = sys.argv[1]
perm2 = sys.argv[2]
frontend(perm1, perm2)
