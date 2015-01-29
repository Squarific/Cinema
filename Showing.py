from Database import *

class Showing(Database):
	def __init__(self, id=None, hall_number=None, slot=None, date=None, film_id=None, free_seats=None):
		self.set_searchkey_key("id")
		self.data = {}

		self.set("id", int(id))
		self.set("hall_number", int(hall_number))
		self.set("slot", slot)
		self.set("date", date)
		self.set("film_id", int(film_id))
		self.set("free_seats", int(free_seats))

	def __str__ (self):
		keys = ["id", "hall_number", "slot", "date", "film_id", "free_seats"]
		string = "Showing: \n"

		for key in keys:
			string += "    " + key + ": " + str(self.get(key)) + "\n"

		return string
		
	def is_full(self):
		return self.free_seats == 0

	def get_data (self):
		keys = ["id", "hall_number", "slot", "date", "film_id", "free_seats"]
		datalist = []
		for key in keys:
			datalist.append(self.get(key))
		return datalist
		
	def __gt__(self, other):
		return self.get("id") > other.get("id")
		
	def __lt__(self, other):
		return self.get("id") < other.get("id")
		
	def __eq__(self, other):
		return self.get("id") == other.get("id")