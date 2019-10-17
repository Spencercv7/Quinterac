
class TransactionSummary:

# Functions to read and wrtie to transaction summary file.
    def __init__(self, file_path):
        self.transaction_summary = open(file_path,"w+")

    # Formats and writes transaction to transaction summary.
    # Utalizes default perameter values for unsupplied feilds.
    def add_transaction(self, transaction_type, to_account="0000000", amount="000", from_account="0000000", name='***'):
        transaction_string = "{} {} {} {} {}\n".format(transaction_type, to_account, amount, from_account, name)
        self.transaction_summary.write(transaction_string)
    
    # Must be called at end of session to save transaction summary.
    def transaction_close(self):
        self.transaction_summary.write("EOS")
        self.transaction_summary.close()