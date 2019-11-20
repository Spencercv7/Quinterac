
import tempfile as tempfile
import tempfile as tempfile1
import tempfile as tempfile2
import tempfile as temp_file3
import tempfile as temp_file

from importlib import reload
import os
import io
import sys
import back_end.run as app

path = os.path.dirname(os.path.abspath(__file__))

def helper(
        capsys,
        input_master_accounts,
        input_summary_one,
        input_summary_two,
        input_summary_three,
        expected_merged_transactions,
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
    temp_fd, temp_file = tempfile.mkstemp()
    new_merged_trans = temp_file

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
    transactions_file1 = temp_file4
    with open(transactions_file1, 'w') as wf:
        wf.write('\n'.join(input_summary_one))

    temp_fd5, temp_file5 = tempfile.mkstemp()
    transactions_file2 = temp_file5
    with open(transactions_file2, 'w') as wf:
        wf.write('\n'.join(input_summary_two))

    temp_fd6, temp_file6 = tempfile.mkstemp()
    transactions_file3 = temp_file6
    with open(transactions_file3, 'w') as wf:
        wf.write('\n'.join(input_summary_three))


    # prepare program parameters
    sys.argv = [
        'run.py',
        master_account_file,
        new_merged_trans,
        new_valid_account,
        new_master_accounts,
        transactions_file1,
        transactions_file2,
        transactions_file3]

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
    

    # compare merged transaction file:
    with open(new_merged_trans, 'r') as of:
        content = of.read().splitlines()
        
        # Change
        print('Merged output:', content)
        print('Merged output (expected):', expected_merged_transactions)
        
        for ind in range(len(content)):
            assert content[ind] == expected_merged_transactions[ind]
    

    # compare:
    with open(new_valid_account, 'r') as of:
        content = of.read().splitlines()
        
        # print out the testing information for debugging
        # the following print content will only display if a 
        # test case failed:
        print('Valid accounts output:', content)
        print('Valid Accounts output (expected):', expected_valid_accounts)
        
        for ind in range(len(content)):
            assert content[ind] == expected_valid_accounts[ind]
    
    with open(new_master_accounts, 'r') as of:
        content = of.read().splitlines()
        
        # Change
        print('Master output:', content)
        print('Master output (expected):', expected_master_accounts)
        
        for ind in range(len(content)):
            assert content[ind] == expected_master_accounts[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    os.close(temp_fd1)
    os.remove(temp_file1)
    os.close(temp_fd2)
    os.remove(temp_file2)
    os.close(temp_fd3)
    os.remove(temp_file3)
