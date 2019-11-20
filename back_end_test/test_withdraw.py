from back_end_test.test_main import helper


def test_r1(capsys):
    """
    Test 1: When account is valid and account has sufficient funds to handle withdrawal
    """
    helper(
        capsys=capsys,
        input_master_accounts=[
            '1000327 10000 Spencer Venable'
        ],
        input_summary_one=[
            'EOS 0000000 000 0000000 ***'
        ], 
        input_summary_two=[
            'WDR 1000327 5000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ], 
        input_summary_three=[
            'EOS 0000000 000 0000000 ***'
        ],
        expected_merged_transactions=[
            'WDR 1000327 5000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ],
        expected_valid_accounts=[
            '1000327'
        ], 
        expected_master_accounts=[
            '1000327 5000 Spencer Venable'
        ],
        expected_tail_of_terminal_output=[
        ]
    )


def test_r2(capsys):
    """
    Test 2: When account is valid and account has insufficient funds to handle withdrawal
    """
    helper(
        capsys=capsys,
        input_master_accounts=[
            '1000327 2000 Spencer Venable',
            '1000326 10000 Ben Lammers'
        ],
        input_summary_one=[
            'EOS 0000000 000 0000000 ***'
        ], 
        input_summary_two=[
            'WDR 1000327 5000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ], 
        input_summary_three=[
            'EOS 0000000 000 0000000 ***'
        ],
        expected_merged_transactions=[
            'WDR 1000327 5000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ],
        expected_valid_accounts=[
            '1000326'
        ], 
        expected_master_accounts=[
            '1000326 10000 Ben Lammers'
        ],
        expected_tail_of_terminal_output=[
            "Withdraw Error: Account 1000327 has insufficient funds",
            "Transaction: WDR 1000327 5000 0000000 ***"
        ]
    )


def test_r3(capsys):
    """
    Test 3: Account does not exist in withdrawal transaction
    """
    helper(
        capsys=capsys,
        input_master_accounts=[
            '1000327 10000 Spencer Venable'
        ],
        input_summary_one=[
            'EOS 0000000 000 0000000 ***'
        ], 
        input_summary_two=[
            'WDR 1000326 5000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ], 
        input_summary_three=[
            'EOS 0000000 000 0000000 ***'
        ],
        expected_merged_transactions=[
            'WDR 1000326 5000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ],
        expected_valid_accounts=[
            '1000327'
        ], expected_master_accounts=[
            '1000327 10000 Spencer Venable'
        ],
        expected_tail_of_terminal_output=[
            "Withdraw Error: Account 1000326 does not exist",
            "Transaction: WDR 1000326 5000 0000000 ***"
        ]
    )
