# Library Imports
import sys
import os
from back_end.objects.field_validator import transaction_is_valid
from back_end.objects.master_accounts import MasterAccounts

'''
python -m back_end master_account.txt merged_trans.txt new_valid_accounts.txt new_master_account.txt transactions_1.txt transactions_2.txt

Paramaters
1. Current Master Account Text File
2. Name for Merged Transaction Text File
3. Name for New Valid Account List Text File
4. Name for New Master Account Text File
5 and on. List The Transaction Summary Text Files to be Processed

'''



'''
Handles main execution of the program. Takes in the parameters from the command line
Calls creation of merged transaction file and subsequently processes the merged file line by line
Creates new valid account list and master account file
'''
def main():
      
      master_accounts = MasterAccounts(sys.argv[1])

      merged_trans_file = sys.argv[2]  #recieves command line parameters
      new_valid_account_file = sys.argv[3]
      new_master_account_file = sys.argv[4]

      transaction_files = sys.argv[5:]

      generate_merge_transaction(merged_trans_file, transaction_files, master_accounts)  #create merged transaction summary file
      try:
            with open(merged_trans_file) as merged:  # process transaction line by line
                  transactions = merged.readlines()
                  for line in transactions:
                        handle_transaction(line, master_accounts)

      except IOError:
            print("Count not open Merged Transaction File")

      master_accounts.create_valid_account_list(new_valid_account_file)
      master_accounts.create_new_master_account_file(new_master_account_file)

'''
Takes in a transaction string describing a transaction
Passes string to appropriate function for it to be further processed
These handling functions do not need to check validity of transaction string format as that is checked upon creation of merged transaction file
'''
def handle_transaction(transaction_string, master_accounts):
      transaction = transaction_string.split()
      length = len(transaction)

      code = transaction[0]
      to_account = transaction[1]
      amount = int(transaction[2])
      from_account = transaction[3]
      
      name = ''
      for i in range(4, length):  #concatenate names with spaces
            if (i == length-1):
                  name += transaction[i]
            else:
                  name += transaction[i] + ' '
      
      valid_transaction = False

      if (code == 'NEW'):
            valid_transaction = handle_new_account(to_account, name, master_accounts)
      
      elif (code == 'DEL'):
            valid_transaction = handle_del_account(to_account, name, master_accounts)

      elif (code == 'XFR'):
            valid_transaction = handle_transfer(to_account, from_account, amount, master_accounts)

      elif (code == 'DEP'):
            valid_transaction = handle_deposit(to_account, amount, master_accounts)

      elif (code == 'WDR'):
            valid_transaction = handle_withdraw(to_account, amount, master_accounts)

      if (not valid_transaction and code != 'EOS'):
            print("Transaction: " + transaction_string) # display transaction string of invalid transactions
      

'''
Checks validity of transactions attempt to create a new account
Produces errors if account already exists
'''
def handle_new_account(to_account, name, master_accounts):
      if not (to_account in master_accounts.accounts):
            master_accounts.add(to_account, name)
            return True
      else:
            print("Error: Duplicate account creation attempt " + str(to_account))
            return False


'''
Checks validity of transactions attempt to delete a new account
Produces errors if account does not exist or has non-zero balance
'''
def handle_del_account(to_account, name, master_accounts):
      if (to_account in master_accounts.accounts):
            if (master_accounts.accounts[to_account].name == name and master_accounts.accounts[to_account].balance == 0):
                  master_accounts.remove(to_account)
                  return True
            else:
                  print("Error: Invalid attempt to delete account " + str(to_account))
                  return False
      else:
            print("Error: Invalid attempt to delete non-existent account " + str(to_account))
            return False

'''
Checks validity of transactions attempt to transfer funds
Produces errors if one or more accounts do not exist or do not have valid balances
'''
def handle_transfer(to_account, from_account, amount, master_accounts):
      if (to_account in master_accounts.accounts and from_account in master_accounts.accounts):
            if (master_accounts.accounts[to_account].balance <= 99999999-amount and master_accounts.accounts[from_account].balance >= amount): # if fund reciever will go over limit or if giver has insufficient funds
                  master_accounts.accounts[to_account].balance += amount
                  master_accounts.accounts[from_account].balance -= amount
                  return True
            else:
                  print("Transfer Error: Failed transfer to account " + str(to_account) + ' from ' + str(from_account))
                  return False
      else:
            print("Transfer Error: Transfer declined due to one or more non-existent accounts")
            return False


'''
Checks validity of transactions attempt to deposit funds
Produces errors if account does not exist or if the deposit amount will cause account to exceed balance limit
'''
def handle_deposit(to_account, amount, master_accounts):
      if (to_account in master_accounts.accounts):
            if (master_accounts.accounts[to_account].balance <= 99999999-amount):
                  master_accounts.accounts[to_account].balance += amount
                  return True
            else:
                  print("Deposit Error: Account " + str(to_account) + " balance exceeds limit")
                  master_accounts.accounts[to_account].setInvalid()
                  return False
      else:
            print("Deposit Error: Account " + str(to_account) + " does not exist")
            return False


'''
Checks validity of transactions attempt to withdraw funds
Produces errors if account does not exist or if the account has insufficient funds
'''
def handle_withdraw(to_account, amount, master_accounts):
      if (to_account in master_accounts.accounts):
            if (master_accounts.accounts[to_account].balance >= amount):
                  master_accounts.accounts[to_account].balance -= amount
                  return True
            else:
                  print("Withdraw Error: Account " + str(to_account) + " has insufficient funds")
                  master_accounts.accounts[to_account].setInvalid()
                  return False
      else:
            print("Withdraw Error: Account " + str(to_account) + " does not exist")
            return False



'''
Gets transaction files from transaction_files dir and merges them to create a merged transaction summary file
Checks validity of each transaction and causes fatal error if one is in incorrect format
'''
def generate_merge_transaction(merged_file_name, transaction_files, master_accounts):
      try: # Attempts to create new file for writing transactions to
            merged_trans_file = open(merged_file_name, 'w')  # create and open new merge transaction file
            for file in transaction_files:   # list of transaction summary files
                  try:
                        with open(file) as f:   # open each transaction summary file
                              content = f.readlines()
                              for transaction in content:
                                    transaction_list = transaction.split() # split each part of the transaction into a list
                                    if transaction_is_valid(transaction_list) and transaction != "EOS 0000000 000 0000000 ***":  # do not print EOS from transaction files
                                          merged_trans_file.write(transaction)
                                    elif (transaction != "EOS 0000000 000 0000000 ***"): # if the transaction invalid and does not equal EOS transaction
                                          print("INVALID TRANSACTION READ: " + transaction + "from " + file + '\n') 
                                          exit() # Exit progarm due to invalid format of transaction file
                  except IOError:
                        print("Error Reading File")
            merged_trans_file.write("EOS 0000000 000 0000000 ***")  # add EOS to end of merged transaction file
      except IOError:
            print("Failed to Create new File.")



