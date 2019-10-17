
class ValidAccounts():

# Take in text file, generate dictonary with valid accounts, functions that 
# add, remove and check for elements of the dictonary
     def __init__(self, file_path):
          self.valid_account_list = {}
          with open(file_path) as fp:
               line = fp.readline()
               cnt = 1
               while line:
                    account_num = ("{}".format(line.strip()))
                    line = fp.readline()
                    cnt += 1
                    self.add_valid_account(account_num)

     # Adds an account to the valid account dictionary 
     def add_valid_account(self, account_num):
          account_num = int(account_num)
          self.valid_account_list[account_num] = 1

     # Deletes account from the valid account dictionary
     def delete_account(self, account_num):
          account_num = int(account_num)
          del self.valid_account_list[account_num]

     # Checks if account is in valid account dictionary
     def contains_account(self, account_num):
          account_num = int(account_num)
          if account_num in self.valid_account_list:
               return True
          else:
               return False
