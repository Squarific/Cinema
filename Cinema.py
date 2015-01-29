#Import containers
from HashMap import *
from TTFTree import *
from rbtree import *
from TTTree import *

from Stack import *
from User import *

class Cinema:
	def __init__(self, name):
		self.name = name
		self.categories = {}
		
	def rename(self, name):
		self.name = name

	def Container(self):
		#return HashMap("chaining", 11)
		return TTFTree()
		#return Tree()
		#return TwoThreeTree();
		
	def add(self, category, item):
		# Make sure the category exists, create if it does not yet exist
		cat_container = self.categories.get(category);
		if not cat_container:
			self.categories[category] = self.Container()

		# Add the item to the container
		return self.categories[category].add(item.get_searchkey(), item)
		
	def get(self, category, searchKey):
		# Make sure the category exists, create if it does not yet exist
		cat_container = self.categories.get(category);
		if not cat_container:
			self.categories[category] = self.Container()

		# Get the item from the container
		return self.categories[category].get(searchKey)
		
	def delete(self, category, searchKey):
		# Make sure the category exists, create if it does not yet exist
		cat_container = self.categories.get(category);
		if not cat_container:
			print("Category not found.")
			return

		# Get the item from the container
		self.categories[category].delete(searchKey)
		print("Item deleted.")
		return

	def largest_searchkey (self, category):
		items = self.get_all(category)
		biggest = 0
		for item in items:
			searchkey = item.get_searchkey()
			if searchkey > biggest:
				biggest = searchkey
		return biggest

	def get_all(self, category):
		# Make sure the category exists, create if it does not yet exist
		cat_container = self.categories.get(category);
		if not cat_container:
			self.categories[category] = self.Container()

		# Get all items from the container
		return self.categories[category].get_all()
		
	
	def add_reservation(self, reservation):
		# Get the showing of this reservation to check for free seats
		showing = self.get("showing", reservation.get("showing_id"))
		if not showing or showing.get("free_seats") < reservation.get("seats"):
			return False

		# Make sure the user exists, if he doesnt, create an empty user
		user_id = reservation.get("user_id")
		if not self.get("user", user_id):
			if not self.add("user", User(user_id)):
				return False

		# Add the reservation to the system
		self.add("reservation", reservation)

		# Reserve the seats
		showing.set("free_seats", showing.get("free_seats") - reservation.get("seats"))

		# Add the tickets to the stack
		stack = self.get("stack", showing.get("id"))
		if not stack:
			stack = Stack(showing.get("id"))
			self.add("stack", stack)

		# Add one ticket per seat
		for i in range(0, reservation.get("seats")):
			stack.push(showing.get("id"))

		return True