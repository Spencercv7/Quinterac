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
            'EOS'
        ]
    )


def test_r2(capsys):
    """
    T2 - ATM Case: Rejection of a transfer to or from an account that has a non-numeric
    number.
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
            'EOS'
        ]
    )


def test_r3(capsys):
    """
    T3 - ATM Case: Rejection of a transfer with an ammount larger then 1000000.
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
            'EOS'
        ]
    )