'''
Checks if the number inputed as a parameter (account_num) is valid.
'''
def number_is_valid(account_num):
      if (account_num == '0000000'): # For file end 'blank' account.
            return True
      try:
            account_num = int(account_num)
      except ValueError:
            return False

      if account_num > 9999999 or account_num < 1000000:
            return False 

      return True


'''
Checks if the 'amount' inputed as a parameter (amount) is valid.
'''      
def amount_is_valid(amount):
      try:
            amount = int(amount) # Insures that no non-numerical characters were supplied in the amount.
      except ValueError:
            return False
      
      if 0 > amount or amount > 99999999:
            return False

      return True


'''
Checks if the name inputed as a parameter (account_name) is valid.
'''
def name_is_valid(account_name):
    
      account_name = str(account_name) # Casts to string before checking length.
      
      if 3 > len(account_name) or len(account_name) > 30:
            return False

      return True


'''
Checks if the transaction (a line from the transaction summary file) inputed as a parameter (transaction) is valid
by utalizing the functions name_is_valid, number_is_valid and amount_is_valid.
'''
def transaction_is_valid(transaction):
      transactions = ['EOS', 'NEW', 'DEL', 'XFR', 'DEP', 'WDR']
      print(transaction)
      length = len(transaction)
      if (length > 4):

            code = transaction[0]
            to_account = transaction[1]
            amount = transaction[2]
            from_account = transaction[3]
            name = ''

            for i in range(4, length):
                  if (i == length-1):
                        name += transaction[i]
                  else:
                        name += transaction[i] + ' '
                        
            return ((code in transactions) and 
                  number_is_valid(to_account) and
                  number_is_valid(from_account) and
                  name_is_valid(name) and 
                  amount_is_valid(amount)) 
      return False