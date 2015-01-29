from Movie import *
from Hall import *
from Showing import *
from User import *
from Reservation import *
from Stack import *

from Cinema import *
from Cmd_cinema_interface import *
from Cinema_save import *

import signal
import sys

def sigint_handler (signal, frame):
	""" What should be done if the program receives the sigint signal """
	print("")
	print("###########################################")
	print("#       TOLD TO SHUT DOWN (SIGINT)        #")
	print("###########################################")
	print("")

	# Closing down, save everything
	cinema_save.save(categories)
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)



# Data that needs to be saved
categories = [("hall", Hall), ("movie", Movie), ("showing", Showing), ("user", User), ("reservation", Reservation), ("stack", Stack)]

print("###########################################")
print("# Toepassingsopdract geg. abs. en struct. #")
print("# Bioscoop systeem                        #")
print("###########################################")
print("")
print("")
print("###########################################")
print("#                  SETUP                  #")
print("###########################################")
print("")

# Create the cinema to store the data and
# create an interface for the command line
cinema = Cinema("Kinepolis")
interface = Cmd_cinema_interface(cinema)
cinema_save = Cinema_save(cinema, interface)

# Read the data from the previous time
cinema_save.load(categories);

# Enter the menu
interface.menu()

print("")
print("###########################################")
print("#            QUITING & SAVING             #")
print("###########################################")
print("")

# Closing down, save everything
cinema_save.save(categories)