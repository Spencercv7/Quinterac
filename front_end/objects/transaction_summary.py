import sys
import os

class TransactionSummary:

# Functions to read and wrtie to transaction summary file.
    def __init__(self, file_path):
        self.transaction_summary = file_path

    # Formats and writes transaction to transaction summary.
    # Utalizes default perameter values for unsupplied feilds.
    def add_transaction(self, transaction_type, to_account="0000000", amount="000", from_account="0000000", name='***'):
        transaction_string = "{} {} {} {} {}\n".format(transaction_type, to_account, amount, from_account, name)
        with open(self.transaction_summary, 'a') as ts:
            ts.write(transaction_string)
    
    # Must be called at end of session to save transaction summary.
    def transaction_close(self):
        with open(self.transaction_summary, 'a') as ts:
            ts.write("EOS 0000000 000 0000000 ***")
