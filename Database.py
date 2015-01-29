class Database:
	def __init__ (self):
		self.data = {}

	def get (self, key):
		return self.data.get(key)

	def set (self, key, value):
		self.data[key] = value
		return True

	def get_searchkey (self):
		return self.data.get(self.searchkey_key)

	def set_searchkey_key (self, searchkey_key):
		self.searchkey_key = searchkey_key