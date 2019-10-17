# Library Imports
import sys

# Object Imports
from objects.session_handler import SessionHandler

# Method to be run on start of the program
def frontend(account_list_file, trans_summary_file):

     # Starts the session handler and passes the path to the files
     sessionHandler = SessionHandler(account_list_file, trans_summary_file)

     print('Welcome to the Quinterac Banking System\n')
     running = True
     while (running):
          running = sessionHandler.get_command()

if __name__ == "__main__":
     accountFile = sys.argv[1]
     transFile = sys.argv[2]
     frontend(accountFile, transFile)