# Linked chain implementation made by Filip Smets
# License: MIT

class Node:
	def __init__ (self, searchKey, value, next):
		self.next = next
		self.searchKey = searchKey
		self.value = value

class LinkedChain:
	head = None

	def add (self, searchKey, value):
		if self.contains(searchKey):
			return False
			
		self.head = Node(searchKey, value, self.head or None)
		return True

	def get (self, searchKey):
		current_pointer = self.head
		while current_pointer:
			if current_pointer.searchKey == searchKey:
				return current_pointer.value
			current_pointer = current_pointer.next
		return False

	def get_all (self):
		elements = []
		current_pointer = self.head
		while current_pointer:
			elements.append(current_pointer.value)
			current_pointer = current_pointer.next
		return elements

	def delete (self, searchKey):
		current_pointer = self.head
		previous = None
		while current_pointer:
			if current_pointer.searchKey == searchKey:
				if not previous:
					self.head = None
				else:
					previous.next = current_pointer.next
				return current_pointer.value
			previous = current_pointer
			current_pointer = current_pointer.next
		return False


	def contains (self, searchKey):
		current_pointer = self.head
		while current_pointer:
			if current_pointer.searchKey == searchKey:
				return True
			current_pointer = current_pointer.next

		return False