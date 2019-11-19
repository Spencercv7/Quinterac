# Library Imports
import sys
import os
from objects.field_validator import transaction_is_valid


def main():
      generate_merge_transaction()  #create merged transaction summary file
      # create the master account dictionary





'''
Gets transaction files from transaction_files dir and merges them to create a merged transaction summary file
'''
def generate_merge_transaction():
      transaction_dir = 'transaction_files'
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
main()


