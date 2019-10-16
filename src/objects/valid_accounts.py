class ValidAccounts():

# Take in text file, generate dictonary with valid accounts, functions that 
# add, remove and check for elementsof the dictonary

     def __init__(self, file_path):
          self.validAccountList = {}
          with open(file_path) as fp:
               line = fp.readline()
               cnt = 1
               while line:
                    accountNum = ("{}".format(line.strip()))
                    line = fp.readline()
                    cnt += 1
                    self.addValidAccount(accountNum)
          print("Valid Accounts")

     #assuming accountNum is a string
     def addValidAccount(self, accountNum):
          accountNum = int(accountNum)
          self.validAccountList[accountNum] = 1

     #assuming accountNum is a string
     def queryValidAccount(self, accountNum):
          accountNum = int(accountNum)
          if accountNum in self.validAccountList:
               return True
          else:
               return False
