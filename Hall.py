from Database import *

class Hall(Database):
	def __init__(self, number=None, seats=None):
		self.set_searchkey_key("number")
		self.data = {}

		self.set("number", int(number))
		self.set("seats", int(seats))

	def __str__ (self):
		keys = ["number", "seats"]
		string = "Hall: \n"

		for key in keys:
			string += "    " + key + ": " + str(self.get(key)) + "\n"

		return string

	def get_data (self):
		keys = ["number", "seats"]
		datalist = []
		for key in keys:
			datalist.append(self.get(key))
		return datalist
		
	def __gt__(self, other):
		return self.get("number") > other.get("number")
		
	def __lt__(self, other):
		return self.get("number") < other.get("number")
		
	def __eq__(self, other):
		return self.get("number") == other.get("number")