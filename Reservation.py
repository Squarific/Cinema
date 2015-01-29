from Database import *

class Reservation(Database):
	def __init__(self, id=None, user_id=None, timestamp=None, showing_id=None, seats=None):
		self.set_searchkey_key("id")
		self.data = {}
		
		self.set("id", int(id))
		self.set("user_id", int(user_id))
		self.set("timestamp", float(timestamp))
		self.set("showing_id", int(showing_id))
		self.set("seats", int(seats))

	def __str__ (self):
		keys = ["id", "user_id", "timestamp", "showing_id", "seats"]
		string = "Reservation: \n"

		for key in keys:
			string += "    " + key + ": " + str(self.get(key)) + "\n"

		return string

	def get_data (self):
		keys = ["id", "user_id", "timestamp", "showing_id", "seats"]
		datalist = []
		for key in keys:
			datalist.append(self.get(key))
		return datalist
		
	def __gt__(self, other):
		return self.id > other.id
		
	def __lt__(self, other):
		return self.id < other.id
		
	def __eq__(self, other):
		return self.id == other.id