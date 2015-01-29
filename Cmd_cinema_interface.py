from Movie import *
from Hall import *
from Showing import *
from User import *
from Reservation import *
from Stack import *

import time

class Cmd_cinema_interface:
	def __init__ (self, cinema):
		self.cinema = cinema

	def ask_movies (self):
		movies = input("How many movies would you like to add?\n")
		while not movies.isdigit():
			print("Wrong input. Please enter a whole number.\n")
			movies = input("How many movies would you like to add?\n")
		movies = int(movies)
		movie_id = 0
		offset = self.cinema.largest_searchkey("movie") + 1
		
		while movie_id < movies:
			movie_title = input("What is the title of the movie you would like to add.\n")
			movie_rating = input("What rating does the movie have?\n")
			loop = True
			while loop:
				try:
					float(movie_rating)
					loop = False
				except Exception:
					print("Wrong input. The movie rating has to be a number.\n")
					movie_rating = input("What rating does the movie have?\n")
					
			self.cinema.add("movie", Movie(movie_id + offset, movie_title, movie_rating))
			print("Movie has been added with id: ", movie_id + offset)
			movie_id += 1

	def ask_halls (self):
		halls = input("How many halls would you like to add?\n")
		while not halls.isdigit():
			print("Wrong input. Please enter a whole number.\n")
			halls = input("How many halls would you like to add?\n")
		halls = int(halls)
		hall_id = 0
		
		while hall_id < halls:
			hall_number = input("What is the hall number of the hall you would like to add?\n")
			loop = True
			while loop:
				try:
					int(hall_number)
					loop = False
				except Exception:
					print("Wrong input. The hall number has to be a whole number.")
					hall_number = input("What is the hall number of the hall you would like to add?\n")					
					
			hall_seats = input("How many seats are there in this hall?\n")
			loop = True
			while loop:
				try:
					int(hall_seats)
					loop = False
				except Exception:
					print("Wrong input. The amount of seats has to be a whole number.")
					hall_seats = input("How many seats are there in this hall?\n")
			
			self.cinema.add("hall", Hall(hall_number, hall_seats))
			hall_id += 1

	def ask_showings (self):
		showings = input("How many showings would you like to add?\n")
		while not showings.isdigit():
			print("Wrong input. Please enter a whole number.\n")
			showings = input("How many showings would you like to add?\n")
		showings = int(showings)
		showing_id = 0
		offset = self.cinema.largest_searchkey("showing") + 1
		while showing_id < showings:
			showing_hall = input("In which hall will this showing be?\n")
			loop = True
			while loop:
				try:
					int(showing_hall)
					loop = False
				except Exception:
					print("Wrong input. The hall number must be a whole number.\n")
					showing_hall = input("In which hall will this showing be?\n")			
				
			showing_time = input("When will this showing be? (Example: 14:30)\n")
			while not is_time(showing_time):
				print("Wrong input. Format: hh:mm\n")
				showing_time = input("When will this showing be? (Example: 14:30)\n")
				
			showing_date = input("At what date will the showing be? (Format: dd-mm-yyyy)\n")
			while not is_date(showing_date):
				print("Wrong input. Format: dd-mm-yyyy\n")
				showing_date = input("At what date will the showing be? (Format: dd-mm-yyyy)\n")
				
			showing_movie_id = input("What movie will be shown? Input the ID given when the movie was added.\n")
			loop = True
			while loop:
				try:
					int(showing_movie_id)
					loop = False
				except Exception:
					print("Wrong input. Movie ID has to be a whole number.\n")
					showing_movie_id = input("What movie will be shown? Input the ID given when the movie was added.\n")
					
			showing_free_seats = input("How many free seats are there?\n")
			loop = True
			while loop:
				try:
					int(showing_free_seats)
					loop = False
				except Exception:
					print("Wrong input. Amount of free seats should be a whole number.")
					showing_free_seats = input("How many free seats are there?\n")

			self.cinema.add("showing", Showing(showing_id + offset, showing_hall, showing_time, showing_date, showing_movie_id, showing_free_seats))
			showing_id += 1

	def display_all (self, category):
		print("All elements in category: " + category)
		elements = self.cinema.get_all(category)
		for element in elements:
			print(element)

	def display_item (self, category, searchKey):
		print("Element " + str(searchKey) + " in category: " + category)
		print(self.cinema.get(category, int(searchKey)))
		print("")
		
	def delete (self, category, searchKey):
		print("Deleting the following item: \n")
		self.display_item(category, int(searchKey))
		self.cinema.delete(category, int(searchKey))

	def new_reservation (self):
		answer = input("Would you like to create a new user? (Y/n): ")
		
		if answer == "n":
			user_id = input("What is the id of the user you are making a reservation for?: ")
		else:
			user_id = self.cinema.largest_searchkey("user") + 1
			self.cinema.add("user", User(user_id, input("What is your first name?: "), input("What is your last name?: "), input("What is your email?: ")))

		id = self.cinema.largest_searchkey("reservation")

		print("\n\n")
		print("Thesere are all the showings:\n")

		self.display_all("showing")

		print("\n\n")

		showing_id = input("What is the ID of the showing you want to go to?: ")
		while not showing_id.isdigit():
			print("Wrong input. The ID of the showing should be a whole number.")
			showing_id = input("What is the ID of the showing you want to go to?: ")
		showing_id = int(showing_id)
		
		seats = input("How many seats do you want to reserve?: ")
		while not seats.isdigit():
			print("Wrong input. The amount of seats has to be a whole number.")
			seats = input("How many seats do you want to reserve?: ")
		seats = int(seats)
			
		if self.cinema.add_reservation(Reservation(id, user_id, time.time(), showing_id, seats)):
			print("Succesfully added reservation.")
		else:
			print("There were not enough seats left for this showing.")

	def new_user (self):
		first_name = input("What is your first name?: ")
		last_name = input("What is your last name?: ")
		email = input("What is your email?: ")
		self.cinema.add("user", User(self.cinema.largest_searchkey("user") + 1, first_name, last_name, email))

	def can_movie_start (self):
		print("\n\n")
		print("Thesere are all the showings:\n")

		self.display_all("showing")

		print("\n\n")

		id = input("What is the id of the showing you'd like to start?")
		while not id.isdigit():
			print("Wrong input. The ID has to be a whole number.\n")
			id = input("What is the id of the showing you'd like to start?")
		id = int(id)

		stack = self.cinema.get("stack", id)
		if not stack:
			print("No stack present for this showing. Either noone bought tickets or something went wrong.")
			return

		if stack.is_empty():
			print("The movie can start.")
		else:
			print(str(stack.get_length()) + " people still have to arrive.")

	def user_arrived (self):
		print("\n\n")
		print("Thesere are all the showings:\n")

		self.display_all("showing")

		print("\n\n")

		id = input("What is the id of the showing the user came for?")
		while not id.isdigit():
			print("Wrong Input. The ID has to be a whole number.\n")
			id = input("What is the id of the showing the user came for?")
		id = int(id)

		stack = self.cinema.get("stack", id)
		if not stack:
			print("No stack present for this showing. Either noone bought tickets or something went wrong.")
			return

		stack.pop()
		print("One user has arrived. " + str(stack.get_length()) + " people still have to arrive.")


	def menu(self):
		quit = False
		
		print("")
		print("###########################################")
		print("#                  MENU                   #")
		print("###########################################")
		print("")
		
		while not quit:
			inputstr = input("What would you like to do?\n(type help if you need help)\n")
			inputarr = inputstr.split(" ")
			print("")
			
			if inputstr == "quit":
				quit = True
				
			elif inputstr == "help":
				print("You can enter the following commands:")
				print("- add movie")
				print("- add hall")
				print("- add showing")
				print("- add reservation")
				print("- add user")
				print("- user_arrived")
				print("- can_movie_start")
				print("- display all [category]")
				print("    [category] can be movie, hall, showing, reservation or user")
				print("- display [category] [searchkey]")
				print("    [category] can be movie, hall, showing, reservation or user")
				print("    [searchkey] is an integer, in most cases the id but for halls its the room number")
				print("- delete [category] [searchkey]")
				print("    [category] can be movie, hall, showing, reservation or user")
				print("    [searchkey] is an integer, in most cases the id but for halls its the room number")
				print("- save")
				print("    Save everything to the hard disk")
				print("- quit")
				print("    Quits the program and saves everything")
				
			elif inputstr == "add movie":
				self.ask_movies()
				
			elif inputstr == "add hall":
				self.ask_halls()
				
			elif inputstr == "add showing":
				self.ask_showings()
				
			elif inputstr == "add reservation":
				self.new_reservation()
				
			elif inputstr == "add user":
				self.new_user()

			elif inputstr == "user_arrived":
				self.user_arrived()

			elif inputstr == "can_movie_start":
				self.can_movie_start()

			elif inputstr == "save":
				print("")
				print("###########################################")
				print("#                 SAVING                  #")
				print("###########################################")
				print("")

				categorys = [("hall", Hall), ("movie", Movie), ("showing", Showing), ("user", User), ("reservation", Reservation)]
				for category in categorys:
					try:
						print("Opening 'data/" + category[0] + ".txt' with flag w ...")
						cat_file = open("data/" + category[0] + ".txt", "w")

					except:
						print("Could not open/create file '" + "data/" + category[0] + ".txt' with the w flag, try sudo?")

					else:
						elements = self.cinema.get_all(category[0])
						print(elements)
						element_file_string = ""
						for element in elements:
							datas = element.get_data()
							print(datas)
							for data in datas:
								element_file_string += str(data).replace(",", "").replace("\n", "") + ","
							element_file_string = element_file_string[:-1] + "\n" # Replace last space with a new line
						cat_file.write(element_file_string)
						print("Saved " + category[0] + "s")
				print("")


			elif inputarr[0] == "display":
				if inputarr[1] == "all":
					self.display_all(inputarr[2])
				elif len(inputarr) == 3:
					self.display_item(inputarr[1], inputarr[2])
				else:
					print("Command not found")
					print("You can only use 'display all [item]' OR 'display [category] [searchkey]'.")
					print("")
					
			elif inputarr[0] == "delete":
				if len(inputarr) == 3:
					self.delete(inputarr[1], inputarr[2])
				else:
					print("Command not found")
					print("You can only use 'delete [category] [searchkey]'.")
					print("")
					
			else:
				print("Command not found. Type help if you dont know what to do.")
				print("")
				

def is_date(str):
	if not len(str) == 10:
		return False
	if not (str[2] == "-" and str[5] == "-"):
		return False
	if not (str[0:1].isdigit() and str[3:4].isdigit() and str[6:9].isdigit()):
		return False
	return True
	
def is_time(str):
	if not len(str) == 5:
		return False
	if not str[2] == ":":
		return False
	if not (str[0:1].isdigit() and str[3:4].isdigit()):
		return False
	return True