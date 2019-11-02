from front_end_test.test_main import helper

def test_r1(capsys):
    """
    T1 - ATM case: Rejects the creation of an account in ATM -> Machine mode.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'createacct',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Cannot perform command in ATM mode',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r2(capsys):
    """
    T2 - Agent Case: Rejection of account creation with an account number that already exisits.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '3270000',
            'Ben Lammers',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '3270000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Account Number Already in Use',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r3(capsys):
    """
    T3 - Agent Case: Reject creation of an account which has an account number begining with a zero.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '0327000',
            'Ben Lammers',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r4(capsys):
    """
    T4 - Agent Case: Rejection of the creation of an account which has a number longer then 7 numbers.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '10327000',
            'Ben Lammers',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r5(capsys):
    """
    T5 - Agent Case: Rejection of the creation of an account which has a number shorter then 7 digits.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '327000',
            'Spencer Venable',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r6(capsys):
    """
    T6 - Agent Case: Rejection of the creation of an account which has an account number which dEOS 0000000 000 0000000 *** not have 7 numerical digits.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            'yeetest',
            'Spencer Venable',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r7(capsys):
    """
    T7 - Agent Case: Rejection of the creation of an account with a name shorter then 3 letters.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '3270000',
            'Sp',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r8(capsys):
    """
    T8 - Agent Case: Rejection of an account created with a name longer then 30 letters.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '3270000',
            'Spener Cory Park Venable Long Name Ya Yeet',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r9(capsys):
    """
    T9 - Agent Case: Rejection of the creation of an account with a name that starts with a ' '
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '3270000',
            ' Spencer Venable',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r10(capsys):
    """
    T10 - Agent Case: Rejection of the creation of an account with a name that ends with a space.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '3270000',
            'Spencer Venable ',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Name',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r11(capsys):
    """
    T11 - Agent Case: Create a valid account.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1000000',
            'Spencer Venable',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Account Created',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'NEW 1000000 000 0000000 Spencer Venable',
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r12(capsys):
    """
    T12 - Agent Case: Reject transaction on newly created account.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '3271001',
            'Spencer Venable',
            'deposit',
            '3271001',
            '1000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Account Number Not In Use',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )