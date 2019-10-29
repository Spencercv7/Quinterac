from front_end_test.test_main import helper

def test_r1(capsys):
    """Testing r2. Self-contained (i.e. everything in the code approach)
    [my favorite - all in one place with the code]

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1000327',
            '1000',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
            '1000327',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Exiting System'
        ],
        expected_output_transactions=[
            'DEP 1000327 1000 0000000 ***',
            'EOS'
        ]
    )