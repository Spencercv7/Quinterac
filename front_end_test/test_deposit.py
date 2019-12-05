from front_end_test.test_main import helper

def test_r1(capsys):
    """
    T1 - Reject account number that is not in valid account list
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1000001',
            '1000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
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

def test_r2(capsys):
    """
    T2 - Reject account number that have non-numerical characters
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            'basd142',
            '1000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T3 - Reject deposit amount exceeding $2000 in ATM mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1000000',
            '1000000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T4 - Reject deposit amount that is less than $0 in ATM mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1000000',
            '-1000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r5(capsys):
    """
    T5 - Reject amount that have non-numerical characters in ATM mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1000000',
            'adsf1234',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r6(capsys):
    """
    T6 - Reject deposit of more than $5000 in a day in ATM mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1000000',
            '200000',
            'deposit',
            '1000000',
            '200000',
            'deposit',
            '1000000',
            '200000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exceeded ATM Deposit Limit',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'DEP 1000000 200000 0000000 ***',
            'DEP 1000000 200000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r7(capsys):
    """
    T7 - Accept valid deposit in ATM mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1000000',
            '100000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'DEP 1000000 100000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r8(capsys):
    """
    T8 - Reject amount over $999,999.99 in agent mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deposit',
            '1000000',
            '100000000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r9(capsys):
    """
    T9 - Reject amount less than $0 in agent mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deposit',
            '1000000',
            '-1000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r10(capsys):
    """
    T10 - Reject amount that contains non-numerical characters in agent mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deposit',
            '1000000',
            'asdf324',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
            'Command:',
            'Session Logged Out',
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r11(capsys):
    """
    T11 - Accept valid deposit in agent mode
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deposit',
            '1000000',
            '10000',
            'logout'
        ],
        intput_valid_accounts=[
            '1000000',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exiting Front End'
        ],
        expected_output_transactions=[
            'DEP 1000000 10000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ]
    )