class Color():
	"""makes a class color to specify the color of a node."""
	def __init__(self, bool):
		if bool == True:
			self.color = "black"
		else:
			self.color = "red"
	def __repr__(self):
		return self.color

class Node():
	"""A class for the nodes of the tree."""
	def __init__(self, searchKey, value, parent, color = True):
		self.searchKey = searchKey
		self.value = value
		self.color = Color(color)
		self.leftchild = None
		self.rightchild = None
		self.parent = parent
	def __repr__(self):
		return str(self.value)
	
class Tree():
	"""A class for the tree."""
	def __init__(self):
		self.root = None
	
	def __repr__(self):
		stringlist = []
		list = self.get_all()
		for i in list:
			stringlist.append(str(i))
		string = ", ".join(stringlist)
		return string
		
	def get(self, searchKey):
		"""searches for a node with a specific searchkey."""
		if type(self.inorder(searchKey)) == Node:
			return self.inorder(searchKey)
		else:
			return False
		
	def inorder(self, searchKey = None, node = None, traversal = None):
		"""Traverses the tree in inorder traversal."""
		if traversal == None:
			traversal = []
		if node == None:
			node = self.root
		if node.searchKey == searchKey:
			traversal = node.value
			
		if node.leftchild == None and node.rightchild == None:	
			#base case
			if type(traversal) == list:
				traversal.append(node)
			else:
				return traversal
				
		else:
			if node.leftchild != None:
				traversal = self.inorder(searchKey, node.leftchild, traversal)
				#inorder get with left child
			if type(traversal) == list:
				traversal.append(node)
			else:
				return traversal
			if node.rightchild != None:
				traversal = self.inorder(searchKey, node.rightchild, traversal)
				#inorder get wth right child
		return traversal

	def get_all(self, node = "base", traversal = None):
		"""Traverses the tree in get_all"""
		if traversal == None:
			traversal = []
		if node == "base":
			node = self.root
			
		if node == None:
			return
			#base case
			
		traversal.append(node.value)
		self.get_all(node.leftchild, traversal)
		self.get_all(node.rightchild, traversal)
		return traversal
	
	def repairtree(self):
		if self.root.color.color != "black":
			self.root.color = Color(True)
			self.repairtree()
			#the root of the tree is always black
			
		rootlist = self.inorder()
		
		for i in rootlist:
			if i != self.root:
				if i.parent.color.color == "red" and i.color.color == "red":
					i.color = Color(True)
					#A red node can only have black nodes as children.
					self.repairtree()
					
		for leaf_1 in rootlist:
			if leaf_1.leftchild == None and leaf_1.rightchild == None:
				for leaf_2 in rootlist:
					if leaf_2.leftchild == None and leaf_2.rightchild == None:
						if leaf_1.value == leaf_2.value or leaf_1.value > leaf_2.value:
							continue
						x = 0
						while x == 0:
							for i in self.get_parents(leaf_1):
								for j in self.get_parents(leaf_2):
									if i[0] == j[0]:
										if i[1] - 1 > j[1]:
											self.rotate_cw(i[0])
											self.repairtree()
										if j[1] - 1 > i[1]:
											self.rotate_ccw(i[0])
											self.repairtree()
										else:
											x = 1
										#every path from the root to a leaf must have the same amount of black nodes.

	def get_parents(self, leaf):
		"""Creates a list with the path from a leaf to the root"""
		parentlist = []
		j = 0
		while True:
			if leaf.parent != None:
				if leaf.parent.color.color == "black":
					j += 1
				parentlist.append((leaf.parent, j))
				leaf = leaf.parent
			else:
				return parentlist
			
			
	def add(self, searchKey, value):
		"""adds a new value in the tree"""
		if self.root == None:
			self.root = Node(searchKey, value, None, True)
			return
		
		for i in self.inorder():
			if i.searchKey == searchKey:
				return False
		node = self.root
		
		while True:
			# looks for his place in the tree: if less than node, go left, else, go right 
			if searchKey < node.searchKey:
				if node.leftchild != None:
					node = node.leftchild
					continue
				else:
					node.leftchild = Node(searchKey, value, node, False)
					break
					
			else:
				if node.rightchild != None:
					node = node.rightchild
					continue
				else:
					node.rightchild = Node(searchKey, value, node, False)
					break
					
		self.repairtree()
	
	def delete(self, searchKey):
		"""deletes a node from the tree"""
		delete = self.get(searchKey)
		if type(delete) == str:
			return
			
		if delete == self.root:
			#if the requested node is the root:
			if delete.leftchild != None:
				# node has an inorder successor
				node = delete.leftchild
				if node.rightchild == None:
					self.root = node
					node.rightchild = delete.rightchild
					if delete.rightchild != None:
						delete.rightchild.parent = node
					node.parent = None
					self.repairtree()
					return
				while node.rightchild != None:
					node = node.rightchild
				self.root = node
				node.rightchild = delete.rightchild
				if delete.rightchild != None:
					delete.rightchild.parent = node
				node.parent.rightchild = node.leftchild
				if node.leftchild != None:
					node.leftchild.parent = node.parent
				node.leftchild = delete.leftchild
				delete.leftchild.parent = node
				self.repairtree()
				return
				
			elif delete.rightchild != None:
			# node has an inorder predecessor
				node = delete.rightchild
				if node.leftchild == None:
					self.root = node
					node.leftchild = delete.leftchild
					if delete.leftchild != None:
						delete.leftchild.parent = node
					node.parent = None
				while node.leftchild != None:
					node = node.leftchild
				self.root = node
				node.leftchild = delete.leftchild
				if delete.leftchild != None:
					delete.leftchild.parent = node
				node.parent.leftchild = node.rightchild
				if node.rightchild != None:
					node.rightchild.parent = node.parent
				node.rightchild = delete.rightchild
				delete.rightchild.parent = node
				self.repairtree()
				return
				
			else:
				#deletes the node: the tree is empty
				self.root = None
				return
				
		else:
			# the node is not the root
			if delete.leftchild != None:
				# node has an inorder successor
				node = delete.leftchild
				if node.rightchild == None:
					node.parent = delete.parent
					if delete.parent.leftchild == delete:
						delete.parent.leftchild = node
					else:
						delete.parent.rightchild = node
					node.rightchild = delete.rightchild
					if delete.rightchild != None:
						delete.rightchild.parent = node
					self.repairtree()
					return
				while node.rightchild != None:
					node = node.rightchild
				node.parent = delete.parent
				if delete.parent.leftchild == delete:
					delete.parent.leftchild = node
				else:
					delete.parent.rightchild = node
				node.parent.rightchild = node.rightchild
				if node.leftchild != None:
					node.leftchild.parent = node.parent
				node.leftchild = delete.leftchild
				node.rightchild = delete.rightchild
				if delete.leftchild != None:
					delete.leftchild.parent = node
				if delete.rightchild != None:
					delete.rightchild.parent = node
				self.repairtree()
				return
				
			elif delete.rightchild != None:
				#node has an inorder predecessor 
				node = delete.rightchild
				if node.leftchild == None:
					node.parent = delete.parent
					if delete.parent.rightchild == delete:
						delete.parent.rightchild = node
					else:
						delete.parent.leftchild = node
					node.leftchild = delete.leftchild
					if delete.leftchild != None:
						delete.leftchild.parent = node
					self.repairtree()
					return
				while node.leftchild != None:
					node = node.leftchild
				node.parent = delete.parent
				if delete.parent.rightchild == delete:
					delete.parent.rightchild = node
				else:
					delete.parent.leftchild = node
				node.parent.leftchild = node.leftchild
				if node.rightchild != None:
					node.righthild.parent = node.parent
				node.rightchild = delete.rightchild
				node.leftchild = delete.leftchild
				if delete.rightchild != None:
					delete.rightchild.parent = node
				if delete.leftchild != None:
					delete.leftchild.parent = node
					
			else:
				# node is a leaf and can be deleted.
				if delete.parent.leftchild == delete:
					delete.parent.leftchild = None
				else:
					delete.parent.rightchild = None
				self.repairtree()
				return
	
	def rotate_cw(self, top):
		"""rotates the tree around a node clockwise"""
		if top.leftchild == None:
			return
		if top == self.root:
			#rotates around the root
			new_top = top.leftchild
			self.root = new_top
			new_top.parent = None
			top.leftchild = new_top.rightchild
			if top.leftchild != None:
				top.leftchild.parent = top
			top.parent = new_top
			new_top.rightchild = top
			
		else:
			# rotates around a node, not the root.
			new_top = top.leftchild
			if top.parent.leftchild == top:
				top.parent.leftchild = new_top
			else:
				top.parent.rightchild = new_top
			new_top.parent = top.parent
			top.leftchild = new_top.rightchild
			if top.leftchild != None:
				top.leftchild.parent = top
			top.parent = new_top
			new_top.rightchild = top
		return

		
	def rotate_ccw(self, top):
		"""rotates the tree around a node counter-clockwise"""
		if top.rightchild == None:
			return
		if top == self.root:
			#rotates around the root.
			new_top = top.rightchild
			self.root = new_top
			new_top.parent = None
			top.rightchild = new_top.leftchild
			if top.rightchild != None:
				top.rightchild.parent = top
			top.parent = new_top
			new_top.leftchild = top
			
		else:
			#rotates around a node, not the root.
			new_top = top.rightchild
			if top.parent.rightchild == top:
				top.parent.rightchild = new_top
			else:
				top.parent.leftchild = new_top
			new_top.parent = top.parent
			top.rightchild = new_top.leftchild
			if top.rightchild != None:
				top.rightchild.parent = top
			top.parent = new_top
			new_top.leftchild = top
		return