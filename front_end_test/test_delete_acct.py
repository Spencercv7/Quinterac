from front_end_test.test_main import helper

def test_r1(capsys):
    """
    T1 - ATM Case: Reject attempt to delet an account in ATM mode.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deleteacct',
            'logout'
        ],
        intput_valid_accounts=[
            '1000327',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Cannot perform command in ATM mode',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r2(capsys):
    """
    T2 - Agent Case: Reject attempt to delete an account which is not in the valid account list.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1000327',
            'Spencer Venable',
            'logout'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Account Number Not In Use',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r3(capsys):
    """
    T3 - Agent Case: Reject attempt to delete an account which is not in the valid account list.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            'aaa1010',
            'Spencer Venable',
            'logout'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r4(capsys):
    """
    T4 - Agent Case: Delete a valid account.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '3271001',
            'Spencer Venable',
            'logout'
        ],
        intput_valid_accounts=[
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Account Deleted',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'DEL 3271001 000 0000000 Spencer Venable',
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r5(capsys):
    """
    T5 - Agent Case: Reject transaction on deleted account.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '3271001',
            'Spencer Venable',
            'deposit',
            '3271001',
            '1000',
            'logout'
        ],
        intput_valid_accounts=[
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Account Number Not In Use',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'DEL 3271001 000 0000000 Spencer Venable',
            'EOS 0000000 000 0000000 ***'
        ]
    )