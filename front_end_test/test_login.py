from front_end_test.test_main import helper

def test_r1(capsys):
    """Testing r1. Self-contained (i.e. everything in the code approach)

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
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
            'EOS'
        ]
    )

def test_r2(capsys):
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
            'EOS'
        ]
    )