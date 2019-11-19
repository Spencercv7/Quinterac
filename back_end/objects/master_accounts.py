from objects.account import Account
from objects.field_validator import number_is_valid, name_is_valid, amount_is_valid

class MasterAccounts:

      def __init__(self, _masteraccounts):
            self.accounts = self.from_file(_masteraccounts)
            
      def add(self, to_account, name):
            self.accounts[to_account] = Account(to_account, 0, name)

      def remove(self, to_account):
            self.accounts[to_account] = None

      def from_file(self, _masteraccounts):

            master_file = open(_masteraccounts, 'r')
            line = master_file.readline()
            account_valid = True
            master_accounts = {}

            while line and account_valid:
                  fields = line.split()

                  number_check = number_is_valid(fields[0])
                  balance_check = amount_is_valid(fields[1])
                  name = ''

                  for i in (range(2, len(fields))):
                        if (i == len(fields)-1):
                              name += fields[i]
                        else:
                              name += fields[i] + ' '

                  name_check = name_is_valid(name)

                  if (number_check and balance_check and name_check):
                        number = fields[0] #changed to stay as string
                        balance = int(fields[1])
                        print(balance)
                        name = str(fields[2])
                        master_accounts[number] = Account(number, balance, name)
                  else:
                        print(fields[0], fields[1], fields[2])
                        account_valid = False
                  
                  line = master_file.readline()

            if account_valid == False:
                  print('ERROR')
                  exit()
                  # Error Handling

            return master_accounts

      
                  