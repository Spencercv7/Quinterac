class TransactionSummary:

# Takes in blank text file, write to it and export it

    def __init__(self, file_path):
        self.transaction_summary = open(file_path,"w+")
    
    def transaction_write(self, to_write):
        self.transaction_summary.write(to_write)

    def get_transaction_summary():
        return self.transaction_summary

    def transaction_string(transaction_type, to_account=0000000, amount=000, from_account=0000000, name='***'):
        self.transaction_summary.write("%s %d %d %d %s", transaction_type, to_account, amount, from_account, name )
    
    # Must be called at end of session.
    def transaction_close():
        self.transaction_summary.close()