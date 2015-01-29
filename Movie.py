from Database import *

class Movie(Database):
	def __init__ (self, id=None, title=None, rating=None):
		self.set_searchkey_key("id")
		self.data = {}
		
		self.set("id", int(id))
		self.set("title", title)
		self.set("rating", float(rating))

	def __str__ (self):
		keys = ["id", "title", "rating"]
		string = "Movie: \n"

		for key in keys:
			string += "    " + key + ": " + str(self.get(key)) + "\n"

		return string

	def get_data (self):
		keys = ["id", "title", "rating"]
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