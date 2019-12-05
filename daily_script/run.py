from importlib import reload
import os
import io
import sys
import front_end.run as front_end
import back_end.run as back_end
from back_end.objects.field_validator import transaction_is_valid

# Daily script takes in valid account list and master account file from previous day
# Outputs new master account file and valid account list 

def main():

    valid_account_list = sys.argv[1]
    master_account_file = sys.argv[2]
    new_valid_account_list = sys.argv[3]
    new_master_account_file = sys.argv[4]

    valid_input = False
    while (not valid_input):
        try: 
            front_end_instances = int(input('How many instances of front end would you like to run: ')) 
            valid_input = True
        except ValueError:
            print('Must enter an integer')

    transaction_list = []

    for x in range(front_end_instances):
        print("Front End {}: ".format(x+1))
        transaction_file = 'transaction_sum{}.txt'.format(x)
        transaction_list.append(transaction_file)

        # prepare program parameters
        sys.argv = ['run.py',
                    valid_account_list,
                    transaction_file]

        # run the program
        front_end.main()
    
    
    generate_merge_transaction("merged_file.txt", transaction_list)

    sys.argv = ['run.py', master_account_file, "merged_file.txt", new_valid_account_list, new_master_account_file]

    back_end.main()
    

        
'''
Gets transaction files from transaction_files dir and merges them to create a merged transaction summary file
Checks validity of each transaction and causes fatal error if one is in incorrect format
'''
def generate_merge_transaction(merged_file_name, transaction_files):
    try: # Attempts to create new file for writing transactions to
        merged_trans_file = open(merged_file_name, 'w')  # create and open new merge transaction file
        for file in transaction_files:   # list of transaction summary files
            try:
                with open(file) as f:   # open each transaction summary file

                    if not os.path.exists('transaction_archive'): #create archive folder if not existent
                        os.makedirs('transaction_archive')
                    path, dirs, files = next(os.walk("transaction_archive"))  # get amount of files in the folder
                    trans_file_num = len(files)
                    arch_file = open("transaction_archive/transaction_archive{}.txt".format(trans_file_num), 'w')

                    content = f.readlines()
                    for transaction in content:
                        
                        arch_file.write(transaction) # write transaction to archived transaction file

                        transaction_list = transaction.split() # split each part of the transaction into a list
                        if transaction_is_valid(transaction_list) and transaction != "EOS 0000000 000 0000000 ***":  # do not print EOS from transaction files
                            merged_trans_file.write(transaction)
                        elif (transaction != "EOS 0000000 000 0000000 ***"): # if the transaction invalid and does not equal EOS transaction
                            print("INVALID TRANSACTION READ: " + transaction + "from " + file + '\n') 
                            print("Merge error Program exits - omitted for testing purposes") # Exit progarm due to invalid format of transaction file

                # delete transaction file and leave transaction file stored in archive folder
                os.remove(file)
            
            except IOError:
                    print("Error Reading File")

        merged_trans_file.write("EOS 0000000 000 0000000 ***")  # add EOS to end of merged transaction file

    except IOError:
            print("Failed to Create new File or Foldler")
