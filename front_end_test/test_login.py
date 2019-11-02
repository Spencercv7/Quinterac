from front_end_test.test_main import helper

def test_r1(capsys):
    """
    T1 - Checking if login accepted in ATM (machine) mode, no valid accounts
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r2(capsys):
    """
    T2 - Checking if login accepted in ATM (machine) mode and takes in valid accounts
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '1043565',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r3(capsys):
    """
    T2 - Checking if login accepted in agent mode, no valid accounts
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r4(capsys):
    """
    T4 - Checking if login accepted in agent mode and takes in valid accounts
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '1043565',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exiting System'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r5(capsys):
    """
    T5 - Checking that invalid input for session type is rejected
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'a23bd',
            'agent',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Machine or Agent:',
            'Invalid Input',
            'Machine or Agent:',
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
    T6 - Checking that alternative command before login rejected
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Must login before doing an alternative command',
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
    T7 - Checking that subsequent logins are rejected after logged in
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'login',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Session already logged in',
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
