from back_end_test.test_main import helper


'''
White Box Testing: Statement Coverage
'''

def test_r1(capsys):
    """
    Account creation with valid account information. New account successfully created. 
    """
    helper(
        capsys=capsys,
        input_master_accounts=[
            '1000327 10000 Spencer Venable',
            '2222333 2000 Ben Lammers',
            '2323453 23231 Jolene Lammers'
        ],
        input_merged_transactions=[
            'NEW 1010101 000 0000000 Jon Snow',
            'EOS 0000000 000 0000000 ***'
        ],
        expected_valid_accounts=[
            '1000327',
            '1010101',
            '2222333',
            '2323453'
        ], expected_master_accounts=[
            '1000327 10000 Spencer Venable',
            '1010101 0 Jon Snow',
            '2222333 2000 Ben Lammers',
            '2323453 23231 Jolene Lammers'
        ],
        expected_tail_of_terminal_output=[
        ]
    )

def test_r2(capsys):
    """
    Test statements which notify the user when an account is created which already exists in the system.
    """
    helper(
        capsys=capsys,
        input_master_accounts=[
            '1000327 10000 Spencer Venable',
            '2222333 2000 Ben Lammers',
            '2323453 23231 Jolene Lammers'
        ],
        input_merged_transactions=[
            'NEW 1000327 000 0000000 Jon Snow',
            'EOS 0000000 000 0000000 ***'
        ],
        expected_valid_accounts=[
            '1000327',
            '2222333',
            '2323453'
        ], expected_master_accounts=[
            '1000327 10000 Spencer Venable',
            '2222333 2000 Ben Lammers',
            '2323453 23231 Jolene Lammers'
        ],
        expected_tail_of_terminal_output=[
              "Error: Duplicate account creation attempt 1000327",
              "Transaction: NEW 1000327 000 0000000 Jon Snow"
        ]
    )