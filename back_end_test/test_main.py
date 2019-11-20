
import tempfile
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
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    temp_fd1, temp_file1 = tempfile1.mkstemp()
    temp_fd2, temp_file2 = tempfile2.mkstemp()
    new_merged_trans = temp_file
    new_valid_account = temp_file1
    new_master_accounts = temp_file2

    

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(intput_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'run.py',
        input_master_accounts,
        new_merged_trans,
        new_valid_account,
        new_master_account,
        input_summary_one,
        input_summary_two,
        input_summary_three]

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()
    
    # print out the testing information for debugging
    # the following print content will only display if a 
    # test case failed:
    print('valid accounts:', intput_valid_accounts)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]
    
    # compare transactions:
    with open(new_merged_trans, 'r') as of:
        content = of.read().splitlines()
        
        # Change
        print('output transactions:', content)
        print('output transactions (expected):', expected_merged_transactions)
        
        for ind in range(len(content)):
            assert content[ind] == expected_merged_transactions[ind]
    
    # compare transactions:
    with open(new_valid_account, 'r') as of:
        content = of.read().splitlines()
        
        # print out the testing information for debugging
        # the following print content will only display if a 
        # test case failed:
        print('output transactions:', content)
        print('output transactions (expected):', expected_valid_accounts)
        
        for ind in range(len(content)):
            assert content[ind] == expected_valid_accounts[ind]
    
    with open(new_master_accounts, 'r') as of:
        content = of.read().splitlines()
        
        # Change
        print('output transactions:', content)
        print('output transactions (expected):', expected_master_accounts)
        
        for ind in range(len(content)):
            assert content[ind] == expected_master_accounts[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
