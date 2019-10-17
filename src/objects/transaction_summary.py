class TransactionSummary:

# Functions to read and wrtie to transaction summary file.
    def __init__(self, file_path):
        self.transaction_summary = open(file_path,"w+")

    # Getter for transcation summary.
    def get_transaction_summary(self):
        return self.transaction_summary

    # Formats and writes transaction to transaction summary.
    # Utalizes default perameter values for unsupplied feilds.
    def transaction_string(self, transaction_type, to_account=0000000, amount=000, from_account=0000000, name='***'):
        self.transaction_summary.write("%s %d %d %d %s", transaction_type, to_account, amount, from_account, name )
    
    # Must be called at end of session to save transaction summary.
    def transaction_close(self):
        self.transaction_summary.close()