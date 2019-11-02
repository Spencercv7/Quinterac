from front_end_test.test_main import helper

def test_r1(capsys):
    """
    T1 - ATM Case: Rejection of a transfer to or from an account that
        is not on the valid account list.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'transfer',
            '1000327',
            '0000000',
            '20000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T2 - ATM Case: Rejection of a transfer to or from an account that has a non-numeric character.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'transfer',
            '1000327',
            'ABC0001',
            '20000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T3 - ATM Case: Rejection of a transfer with an amount larger then $10000.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'transfer',
            '1000327',
            '3270000',
            '10000001',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T4 - ATM Case: Rejection of a transfer with an amount less than zero dollars.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'transfer',
            '1000327',
            '3270000',
            '-1',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T5 - ATM Case: Rejection of a transfer with an amount that contains non-numeric characters.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'transfer',
            '1000327',
            '3270000',
            '1asd12',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T6 - ATM Case: Rejection of a transfering more then 10000 dollars in one day.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'transfer',
            '1000327',
            '3270000',
            '550000',
            'logout',
            'login',
            'machine',
            'transfer',
            '1000327',
            '3270000',
            '550000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exceeded ATM Transfer Limit',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'XFR 1000327 550000 3270000 ***',
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r7(capsys):
    """
    T7 - ATM Case: Acceptance of a valid transfer.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'transfer',
            '1000327',
            '3270000',
            '550000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Transfer Completed',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'XFR 1000327 550000 3270000 ***',
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r8(capsys):
    """
    T8 - Agent Case: Reject transfer of an amount exceeding $999,999.99
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'transfer',
            '1000327',
            '3270000',
            '100000000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T9 - Agent Case: Reejct transfer amount that is less than 0.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'transfer',
            '1000327',
            '3270000',
            '-1',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T10 - Agent Case: Reject transfer amount that contains non-numeric characters.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'transfer',
            '1000327',
            '3270000',
            '1000asd',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid Account Number or Amount',
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
    T11 - Agent Case: Accept valid transfer amount.
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'transfer',
            '1000327',
            '3270000',
            '100000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '3271001',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Transfer Completed',
            'Command:',
            'Session Logged Out',
            'Type Login to login or Type Exit to End Program',
            'Command:',
            'Exiting System'
        ],
        expected_output_transactions=[
            'XFR 1000327 100000 3270000 ***'
            'EOS 0000000 000 0000000 ***'
        ]
    )
