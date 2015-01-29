# HashMap implementation by Smets Filip
# License MIT

from LinkedChain import LinkedChain

class HashMapElement:
	def __init__ (self, searchKey, value):
		self.searchKey = searchKey
		self.value = value

class HashMap:
	_length = 0

	def __init__ (self, type, tableSize):
		self._type = type
		self._tableSize = tableSize
		self._table = [None] * tableSize

	def add (self, searchKey, value):
		""" Add an element """
		# Get the current algorythm, default to linear
		algo = getattr(self, "_algo_" + self._type + "_add", self._algo_linear_add)
		is_added = algo(searchKey, value) # Add the element

		if is_added:
			self._length += 1

		return is_added

	def get (self, searchKey):
		""" Get an element """
		# Get the current algorythm, default to linear
		algo = getattr(self, "_algo_" + self._type + "_get", self._algo_linear_get)
		return algo(searchKey) # Get the element

	def get_all (self):
		algo = getattr(self, "_algo_" + self._type + "_get_all", self._algo_linear_get)
		return algo() # Get the element

	def delete (self, searchKey):
		""" Delete an element """
		# Get the current algorythm, default to linear
		algo = getattr(self, "_algo_" + self._type + "_delete", self._algo_linear_delete)
		is_deleted = algo(searchKey) # Delete the element

		if is_deleted:
			self._length -= 1

		return is_deleted

	#######################
	# Linear hashing algo #
	#######################

	def _algo_linear_add (self, searchKey, value):
		relative_searchKey = searchKey % self._tableSize
		while isinstance(self._table[relative_searchKey], HashMapElement):
			relative_searchKey = (relative_searchKey + 1) % self._tableSize

			# If we are back where we started then there are no empty spaces left
			if relative_searchKey == searchKey % self._tableSize:
				return False
		
		self._table[relative_searchKey] = HashMapElement(searchKey, value)
		return True

	def _algo_linear_get (self, searchKey):
		relative_searchKey = searchKey % self._tableSize
		while isinstance(self._table[relative_searchKey], HashMapElement):
			if self._table[relative_searchKey].searchKey == searchKey:
				return self._table[relative_searchKey].value

			relative_searchKey = (relative_searchKey + 1) % self._tableSize

			# If we are back where we started then there are no empty spaces left
			if relative_searchKey == searchKey % self._tableSize:
				return False

		return False

	def _algo_linear_delete (self, searchKey):
		relative_searchKey = searchKey % self._tableSize
		while isinstance(self._table[relative_searchKey], HashMapElement):
			if self._table[relative_searchKey].searchKey == searchKey:
				value = self._table[relative_searchKey].value
				self._table[relative_searchKey] = None
				return value
			
			relative_searchKey = (relative_searchKey + 1) % self._tableSize

			# If we are back where we started then there are no empty spaces left
			if relative_searchKey == searchKey % self._tableSize:
				return False
		
		return False

	def _algo_linear_get_all (self):
		temp_list = []
		for el in self._table:
			if el:
				temp_list.append(el)
		return temp_list

	##########################
	# Quadratic hashing algo #
	##########################

	def _algo_quadratic_add (self, searchKey, value):
		modulo_searchKey = searchKey % self._tableSize
		relative_searchKey = modulo_searchKey
		counter = 1
		while isinstance(self._table[relative_searchKey], HashMapElement):
			relative_searchKey = (modulo_searchKey + counter ** 2) % self._tableSize

			counter += 1
			# If we are back where we started then there are no empty spaces left
			if relative_searchKey == searchKey % self._tableSize:
				return False
		
		self._table[relative_searchKey] = HashMapElement(searchKey, value)
		return True

	def _algo_quadratic_get (self, searchKey):
		modulo_searchKey = searchKey % self._tableSize
		relative_searchKey = modulo_searchKey
		counter = 1
		while isinstance(self._table[relative_searchKey], HashMapElement):
			if self._table[relative_searchKey].searchKey == searchKey:
				return self._table[relative_searchKey].value

			relative_searchKey = (modulo_searchKey + counter ** 2) % self._tableSize

			counter += 1
			# If we are back where we started then there are no empty spaces left
			if relative_searchKey == searchKey % self._tableSize:
				return False
		
		return False

	def _algo_quadratic_delete (self, searchKey):
		modulo_searchKey = searchKey % self._tableSize
		relative_searchKey = modulo_searchKey
		counter = 1
		while isinstance(self._table[relative_searchKey], HashMapElement):
			if self._table[relative_searchKey].searchKey == searchKey:
				value = self._table[relative_searchKey].value
				self._table[relative_searchKey] = None
				return value

			relative_searchKey = (modulo_searchKey + counter ** 2) % self._tableSize

			counter += 1
			# If we are back where we started then there are no empty spaces left
			if relative_searchKey == searchKey % self._tableSize:
				return False
		
		return False

	def _algo_quadratic_get_all (self):
		temp_list = []
		for el in self._table:
			if el:
				temp_list.append(el)
		return temp_list



	#########################
	# Chaining hashing algo #
	#########################

	def _algo_chaining_add (self, searchKey, value):
		relative_searchKey = searchKey % self._tableSize
		self._table[relative_searchKey] = self._table[relative_searchKey] or LinkedChain()
		return self._table[relative_searchKey].add(searchKey, value)


	def _algo_chaining_get (self, searchKey):
		relative_searchKey = searchKey % self._tableSize
		self._table[relative_searchKey] = self._table[relative_searchKey] or LinkedChain()
		return self._table[relative_searchKey].get(searchKey)

	def _algo_chaining_delete (self, searchKey):
		relative_searchKey = searchKey % self._tableSize
		self._table[relative_searchKey] = self._table[relative_searchKey] or LinkedChain()
		return self._table[relative_searchKey].delete(searchKey)

	def _algo_chaining_get_all (self):
		element_list = []
		for chain in self._table:
			if chain:
				element_list.extend(chain.get_all())
		return element_list


	def length (self):
		""" Returns the amount of added elements minus deleted elements """
		return self._length;

	def empty(self):
		""" Returns if there are currently 0 elements """
		return self._length == 0;