from account import Account
from field_validator import number_is_valid, name_is_valid, amount_is_valid

class MasterAccounts:

      def __init__(self, _masteraccounts):
            self.master_accounts = self.from_file(_masteraccounts)
            

      def from_file(self, _masteraccounts):

            master_file = open(_masteraccounts, 'r')
            line = master_file.readline()
            account_valid = True
            master_accounts = {}

            while line and account_valid:

                  fields = line.split()
                  account = Account()

                  number_check = number_is_valid(fields[0])
                  balance_check = amount_is_valid(fields[1])
                  name_check = name_is_valid(fields[2])

                  if (number_check and balance_check and name_check):
                        account.number = int(fields[0])
                        account.balance = int(fields[1])
                        account.name = str(fields[2])
                        account.valid = True
                        master_accounts[account.number] = account
                  else:
                        print(fields[0], fields[1], fields[2])
                        account_valid = False
                  
                  line = master_file.readline()

            if account_valid == False:
                  print('ERROR')
                  exit()
                  # Error Handling

            return master_accounts

      
                  