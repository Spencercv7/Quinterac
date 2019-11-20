# Library Imports
import sys
import os
from back_end.objects.field_validator import transaction_is_valid
from back_end.objects.master_accounts import MasterAccounts

master_accounts = MasterAccounts(sys.argv[1])

def main():
      generate_merge_transaction()  #create merged transaction summary file
      try:
            with open('merged_transaction.txt') as merged:
                  transactions = merged.readlines()
                  for line in transactions:
                        handle_transaction(line)

      except IOError:
            print("Count not open Merged Transaction File")

      master_accounts.create_valid_account_list()
      master_accounts.create_new_master_account_file()


def handle_transaction(transaction_string):
      transaction = transaction_string.split()
      length = len(transaction)

      code = transaction[0]
      to_account = transaction[1]
      amount = int(transaction[2])
      from_account = transaction[3]
      
      name = ''
      for i in range(4, length):
            if (i == length-1):
                  name += transaction[i]
            else:
                  name += transaction[i] + ' '
      
      valid_transaction = False

      if (code == 'NEW'):
            valid_transaction = handle_new_account(to_account, name)
      
      elif (code == 'DEL'):
            valid_transaction = handle_del_account(to_account, name)

      elif (code == 'XFR'):
            valid_transaction = handle_transfer(to_account, from_account, amount)

      elif (code == 'DEP'):
            valid_transaction = handle_deposit(to_account, amount)

      elif (code == 'WDR'):
            valid_transaction = handle_withdraw(to_account, amount)

      if (not valid_transaction and code != 'EOS'):
            print("Transaction: " + transaction_string)
      


def handle_new_account(to_account, name):
      if not (to_account in master_accounts.accounts):
            master_accounts.add(to_account, name)
            return True
      else:
            print("Error: Duplicate account creation attempt " + str(to_account))
            return False


def handle_del_account(to_account, name):
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


def handle_transfer(to_account, from_account, amount):
      if (to_account in master_accounts.accounts and from_account in master_accounts.accounts):
            if (master_accounts.accounts[to_account].balance <= 99999999-amount and master_accounts.accounts[from_account].balance >= amount):
                  master_accounts.accounts[to_account].balance += amount
                  master_accounts.accounts[from_account].balance -= amount
                  return True
            else:
                  print("Transfer Error: Failed transfer to account " + str(to_account) + ' from ' + str(from_account))
                  return False
      else:
            print("Transfer Error: Transfer declined due to one or more non-existent accounts")
            return False


def handle_deposit(to_account, amount):
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

def handle_withdraw(to_account, amount):
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
'''
def generate_merge_transaction():
      transaction_dir = os.path.dirname(os.path.realpath(__file__)) + '/transaction_files'
      try: # Attempts to create new file for writing transactions to
            merged_trans_file = open('merged_transaction.txt', 'w')
            try: # Attempts to read files in folder
                  for file in os.listdir(transaction_dir): 
                        try:
                              with open(transaction_dir + '/' + file) as f:
                                    content = f.readlines()
                                    for transaction in content:
                                          transaction_list = transaction.split()
                                          if transaction_is_valid(transaction_list) and transaction_list[0] != "EOS":  # do not print EOS from transaction files
                                                merged_trans_file.write(transaction)
                                          elif (transaction_list[0] != 'EOS'):
                                                print("INVALID TRANSACTION READ: " + transaction)  #INVALID TRANSACTION FROM TRANSACTION FILE
                                                exit()
                        except IOError:
                              print("Error Reading File")
                  merged_trans_file.write("EOS 0000000 000 0000000 ***")  # add EOS
            except IOError:
                  print("Could not find transaction directory")
      except IOError:
            print("Failed to Create new File.")



