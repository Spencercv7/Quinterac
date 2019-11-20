from back_end_test.test_main import helper


def test_r1(capsys):
    """
    Test test
    """
    helper(
        capsys=capsys,
        input_master_accounts=[
            '1000327 10000 Spencer Venable',
            '2222333 2000 Ben Lammers',
            '2323453 23231 Jolene Lammers'
        ],
        input_summary_one=[
            'WDR 1000327 3000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ], input_summary_two=[
            'EOS 0000000 000 0000000 ***'
        ], input_summary_three=[
            'EOS 0000000 000 0000000 ***'
        ],
        expected_merged_transactions=[
            'WDR 1000327 3000 0000000 ***',
            'EOS 0000000 000 0000000 ***'
        ],
        expected_valid_accounts=[
            '1000327',
            '2222333',
            '2323453'
        ], expected_master_accounts=[
            '1000327 7000 Spencer Venable',
            '2222333 2000 Ben Lammers',
            '2323453 23231 Jolene Lammers'
        ],
        expected_tail_of_terminal_output=[]
    )
