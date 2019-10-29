# Library Imports
import sys

# Object Imports
from front_end.objects.session_handler import SessionHandler

def main():
     account_list_file = sys.argv[1]
     trans_summary_file = sys.argv[2]

     # Starts the session handler and passes the path to the files
     sessionHandler = SessionHandler(account_list_file, trans_summary_file)

     print('Welcome to the Quinterac Banking System\n')
     running = True
     while (running):
          running = sessionHandler.get_command()
