from back_end.objects.account import Account
from back_end.objects.field_validator import number_is_valid, name_is_valid, amount_is_valid

class MasterAccounts:

      def __init__(self, _masteraccounts):
            self.accounts = self.from_file(_masteraccounts)
            
      def add(self, to_account, name):
            self.accounts[to_account] = Account(to_account, 0, name)

      def remove(self, to_account):
            self.accounts[to_account] = None

      def from_file(self, _masteraccounts):

            with open(_masteraccounts) as master_file:
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
                              master_accounts[number] = Account(number, name, balance)
                        else:
                              account_valid = False
                        
                        line = master_file.readline()

                  if account_valid == False:
                        print('ERROR')
                        exit()
                        # Error Handling

                  return master_accounts
      
      def create_valid_account_list(self, file_name):
            try:
                  valid_account_file = open(file_name, 'w+')
                  for account_num in sorted(self.accounts):
                        account = self.accounts[account_num]
                        if account.valid == True:
                              valid_account_file.write(str(account_num) +"\n")
                  valid_account_file.close()
            except IOError:
                  print("Could not open Valid Accounts File.")

            
      
      def create_new_master_account_file(self, file_name):
            try:
                  master_account_file = open(file_name, 'w+')
                  for account_num in sorted(self.accounts):
                        account = self.accounts[account_num]
                        if account.valid == True:
                              master_account_file.write(str(account_num) + " " + str(account.balance) + " " + str(account.name) + "\n")
                  master_account_file.close()
            except IOError:
                  print("Could not open Master Account file.")


      
                  