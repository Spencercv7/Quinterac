
import tempfile as tempfile

from importlib import reload
import os
import io
import sys
import back_end.run as app

path = os.path.dirname(os.path.abspath(__file__))

def helper(
        capsys,
        input_master_accounts,
        input_merged_transactions,
        expected_valid_accounts,
        expected_master_accounts,
        expected_tail_of_terminal_output
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output

    temp_fd1, temp_file1 = tempfile.mkstemp()
    new_valid_account = temp_file1

    temp_fd2, temp_file2 = tempfile.mkstemp()
    new_master_accounts = temp_file2

    # create a temporary files:
    temp_fd3, temp_file3 = tempfile.mkstemp()
    master_account_file = temp_file3
    with open(master_account_file, 'w') as wf:
        wf.write('\n'.join(input_master_accounts))

    temp_fd4, temp_file4 = tempfile.mkstemp()
    merged_transactions = temp_file4
    with open(merged_transactions, 'w') as wf:
        wf.write('\n'.join(input_merged_transactions))


    # prepare program parameters
    sys.argv = [
        'run.py',
        master_account_file,
        merged_transactions,
        new_valid_account,
        new_master_accounts]

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs at the end.
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]
    

    # compare new valid account file
    with open(new_valid_account, 'r') as of:
        content = of.read().splitlines()
        
        # print out the testing information for debugging
        # the following print content will only display if a 
        # test case failed:
        print('Valid accounts output:', content)
        print('Valid Accounts output (expected):', expected_valid_accounts)
        
        for ind in range(len(content)):
            assert content[ind] == expected_valid_accounts[ind]
    
    # compare new master account
    with open(new_master_accounts, 'r') as of:
        content = of.read().splitlines()
        
        print('Master output:', content)
        print('Master output (expected):', expected_master_accounts)
        
        for ind in range(len(content)):
            assert content[ind] == expected_master_accounts[ind]

    # clean up
    os.close(temp_fd1)
    os.remove(temp_file1)
    os.close(temp_fd2)
    os.remove(temp_file2)
    os.close(temp_fd3)
    os.remove(temp_file3)
    os.close(temp_fd4)
    os.remove(temp_file4)
