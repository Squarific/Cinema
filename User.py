from Database import *

class User(Database):
	def __init__(self, id=None, fname=None, lname=None, email=None):
		self.set_searchkey_key("id")
		self.data = {}

		self.set("id", int(id))
		self.set("fname", fname)
		self.set("lname", lname)
		self.set("email", email)

	def __str__ (self):
		keys = ["id", "fname", "lname", "email"]
		string = "User: \n"

		for key in keys:
			string += "    " + key + ": " + str(self.get(key)) + "\n"

		return string

	def get_data (self):
		keys = ["id", "fname", "lname", "email"]
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