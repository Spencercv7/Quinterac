from importlib import reload
import os
import io
import sys
import daily_script.run as daily_script


def main():

    valid_account_list = sys.argv[1]
    master_account_file = sys.argv[2]

    valid_input = False
    while (not valid_input):
        try: 
            num_of_days = int(input('How many days would you like to simulate: ')) 
            valid_input = True
        except ValueError:
            print('Must enter an integer')


    for day in range(1, num_of_days+1):
        print("\nDay {}:".format(day))
        new_master_account = "master_account{}".format(day)
        new_valid_account_list = "valid_account_list{}".format(day)

        if (day == 1):
            # prepare program parameters
            sys.argv = ['run.py',
                        valid_account_list,
                        master_account_file,
                        new_valid_account_list,
                        new_master_account]
                        
        else:
            valid_account_list = "valid_account_list{}".format(day-1)
            master_account_file = "master_account{}".format(day-1)
            # prepare program parameters
            sys.argv = ['run.py',
                        valid_account_list,
                        master_account_file,
                        new_valid_account_list,
                        new_master_account]

        # run the program
        daily_script.main()
