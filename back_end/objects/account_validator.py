class AccountValidator:

      def number_check(self):
            try:
                  accountNum = int(accountNum)
            except ValueError:
                  return False

            if accountNum > 9999999 or accountNum < 1000000:
                  return False 

            return True
            
      def balance_check(self, amount):
            try:
                  amount = int(amount)
            except ValueError:
                  return False
        
            if 0 > amount or amount > 99999999:
                  return False

            return True
      
      def name_check(self):
            accountName = str(accountName)

            if 3 >= len(accountName) or len(accountName) >= 30:
                  return False

            return True
