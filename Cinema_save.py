class Cinema_save:
	def __init__ (self, cinema, interface):
		self.cinema = cinema
		self.interface = interface

	def load (self, categories):
		""" Read data from the given categories from file, if no file exists ask user for input """
		for category in categories:
			try:
				print("Loading data from file 'data/" + category[0] + ".txt' ...")
				cat_file = open("data/" + category[0] + ".txt")

			except FileNotFoundError:
				# File doesnt exist, ask user
				print("File not found.")
				ask_func = getattr(self.interface, "ask_" + category[0] + "s", None)
				if ask_func:
					print("Manually adding data.")
					ask_func()

			else:
				for line in cat_file:
					data = line.replace("\n", "").split(",")
					self.cinema.add(category[0], category[1](*data))
				cat_file.close()

	def save (self, categories):
		""" Save data for the given categories """
		for category in categories:
			try:
				print("Opening 'data/" + category[0] + ".txt' with flag w ...")
				cat_file = open("data/" + category[0] + ".txt", "w")

			except:
				print("Could not open/create file '" + "data/" + category[0] + ".txt' with the w flag, try sudo?")

			else:
				elements = self.cinema.get_all(category[0])
				element_file_string = ""
				for element in elements:
					for data in element.get_data():
						element_file_string += str(data).replace(",", "").replace("\n", "") + ","
					element_file_string = element_file_string[:-1] + "\n" # Replace last space with a new line
				cat_file.write(element_file_string)
				print("Saved " + category[0] + "s")