from Database import *

class Node:

	def __init__(self,value):
		self.next=None
		self.value=value
		
	def __str__(self):
		return self.value

class Stack_base (Database):
	"""The class stack uses the LIFO (Last in, first out) principle"""

	def __init__(self):
		self.first=None
		self.size=0
		
	def push(self,value):
		item=Node(value)
		
		if self.size!=0:
			item.next=self.first
			
		self.first=item
		self.size+=1
		
		return
		
	def pop(self):
		item=self.first

		if not item:
			return

		self.first=self.first.next
		self.size-=1
		
		return item.value
		
	def get_length(self):
		return self.size
		
	def is_empty(self):
		return self.size==0
		
	def get_top(self):
		return self.first.value
		
	def __str__(self):
		if self.size==0:
			return "Empty"
			
		returnstr=""
		current_item=self.first
		
		for i in range(self.size):
			returnstr+=str(current_item.value)+", "
			current_item=current_item.next
			
		return returnstr[:-2]

class Stack (Stack_base):
	def __init__ (self, showing_id=None, *elements):
		self.data = {}

		self.set_searchkey_key("showing_id")
		self.set("showing_id", int(showing_id))

		self.first=None
		self.size=0

		for element in elements:
			self.push(element)

	def get_data (self):
		""" Return a list with the current elements """
		elements = [self.get("showing_id")]

		while not self.is_empty():
			elements.append(self.pop())

		for element in elements:
			self.push(element)

		return elements

	def __gt__(self, other):
		return self.get("showing_id") > other.get("showing_id")
		
	def __lt__(self, other):
		return self.get("showing_id") < other.get("showing_id")
		
	def __eq__(self, other):
		return self.get("showing_id") == other.get("showing_id")