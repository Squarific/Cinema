class Node:
	def __init__(self, parent, value):
		self.values = [value]
		self.parent = parent
		self.children = []
		
		
	def __repr__(self):
		returnstr = "Node:  "
		
		for i in range(len(self.values)):
			returnstr += str(self.values[i]) + "  "
			
		returnstr += "    (has " + str(len(self.children)) + " children)"
			
		return returnstr
		
		
	def is_leaf(self):
		return len(self.children) == 0
		
		
	def is_full(self):
		return len(self.values) >= 3
		
		
	def is_root(self):
		return self.parent == None
		
		
	def mergesplit(self):
		""""Splits a node with 3 by merging the middle value to the parent, and having the two outer values become children of said parent."""
		
		# Parent has one value
		if len(self.parent.values) == 1:
			if self.values[1] < self.parent.values[0]: # Node is left child
				self.parent.values.insert(0, self.values[1])
					
				# New node
				newnode = Node(self.parent, self.values[2])
				self.parent.children.insert(1, newnode)
				
				if not self.is_leaf():
					newnode.children = [self.children[2], self.children[3]]
					newnode.children[0].parent = newnode
					newnode.children[1].parent = newnode
				
				# Old (reused) node
					self.children = [self.children[0], self.children[1]]
				self.values = [self.values[0]]
				
				return
			else: # Node is right child
				self.parent.values.insert(1, self.values[1])
					
				# New node
				newnode = Node(self.parent, self.values[0])
				self.parent.children.insert(1, newnode)
				
				if not self.is_leaf():
					newnode.children = [self.children[0], self.children[1]]
					newnode.children[0].parent = newnode
					newnode.children[1].parent = newnode
				
				# Old (reused) node
					self.children = [self.children[2], self.children[3]]
				self.values = [self.values[2]]
				
				return
			
		# Parent has two values
		if len(self.parent.values) == 2:
			if self.values[1] < self.parent.values[0]: # Node is left child
				self.parent.values.insert(0, self.values[1])
				
				# New node
				newnode = Node(self.parent, self.values[2])
				self.parent.children.insert(1, newnode)
				
				if not self.is_leaf():
					newnode.children = [self.children[2], self.children[3]]
					newnode.children[0].parent = newnode
					newnode.children[1].parent = newnode
				
				# Old (reused) node
					self.children = [self.children[0], self.children[1]]
				self.values = [self.values[0]]

				return
			elif self.values[1] < self.parent.values[1]: # Node is middle child
				self.parent.values.insert(1, self.values[1])
				
				# New node
				newnode = Node(self.parent, self.values[2])
				self.parent.children.insert(2, newnode)
				
				if not self.is_leaf():
					newnode.children = [self.children[2], self.children[3]]
					newnode.children[0].parent = newnode
					newnode.children[1].parent = newnode
				
				# Old (reused) node
					self.children = [self.children[0], self.children[1]]
				self.values = [self.values[0]]

				return
			else:
				self.parent.values.insert(2, self.values[1])
				
				# New node
				newnode = Node(self.parent, self.values[0])
				self.parent.children.insert(2, newnode)
				
				if not self.is_leaf():
					newnode.children = [self.children[0], self.children[1]]
					newnode.children[0].parent = newnode
					newnode.children[1].parent = newnode
				
				# Old (reused) node
					self.children = [self.children[2], self.children[3]]
				self.values = [self.values[2]]

				return
		
		
	def split(self):
		"""Splits a node with 3 values into 3 nodes, with the middle value being the parent of the other two."""
		
		if self.is_root():
			lchild = Node(self, self.values[0])
			rchild = Node(self, self.values[2])
			
			if len(self.children) == 4:
				lchild.children = [self.children[0],self.children[1]]
				rchild.children = [self.children[2],self.children[3]]
				lchild.children[0].parent = lchild
				lchild.children[1].parent = lchild
				rchild.children[0].parent = rchild
				rchild.children[1].parent = rchild
			
			self.values = [self.values[1]]
			
			self.children = [lchild,rchild]
			
			return self
		else:
			self.mergesplit()
			
			return self.parent
		
		
	def add_value(self, value):
		if not self.is_full():
			self.values.append(value)
			self.values.sort()
		else:
			print("ERROR: Node already has 3 values.\n(tried to insert " + str(value) + ")")
			
			
	def goto_subtree(self, value):
		"""Returns the subtree/child where the value needs to be inserted"""
		if self.is_leaf():
			print("ERROR: This node is a leaf.\n(tried to insert " + str(value) + ")")
			return
			
		for i in range(len(self.values)):
			if self.values[i] > value:
				return self.children[i]
			
		return self.children[-1]
		
	
	def child_index(self):
		# Returns which location the Node has in its parent's children list.
		if self.is_root():
			print("The root has no parent!")
			return False
		
		for i in range(len(self.parent.children)):
			if self.parent.children[i] == self:
				return i

				
		
class TTFTree:
	def __init__(self):
		self.root = None
		self.traverselist = []
		
		
	def inorder(self, subtree):
		curnode = subtree

		if curnode.is_leaf():
			for i in range(len(curnode.values)):
				self.traverselist.append(curnode.values[i])
			return
		
		self.inorder(curnode.children[0])
		for i in range(len(curnode.values)):
			self.traverselist.append(curnode.values[i])
			self.inorder(curnode.children[i+1])
		
		
	def d_rebuild(self, value):
		self.traverselist = []
		self.inorder(self.root)
		self.traverselist.remove(value)
		self.root = None
		for i in range(len(self.traverselist)):
			self.insert("", self.traverselist[i])
	
	def add(self, searchkey, value):
		self.insert(searchkey, value)
		
	def insert(self, searchkey, value):
		if self.root == None: # Empty Tree
			self.root = Node(None, value)
			return
		else:
			self.insert_subtree(self.root, value) # Tree is not empty
		
		
	def insert_subtree(self, subtree, value):
		curnode = subtree
			
		if curnode.is_leaf(): # current node is a leaf
			if not curnode.is_full(): # current node is not full
				curnode.add_value(value)
				return
			else:
				# # print("Splitting node: " + str(curnode))
				curnode = curnode.split()
				# # print("Current node is now: " + str(curnode))
				
				# Curnode is now the parent of a leaf
				
				if len(curnode.values) == 1: # Current node has 1 value
					if value < curnode.values[0]:
						curnode.children[0].add_value(value)
						return
					else:
						curnode.children[1].add_value(value)
						return
						
				elif len(curnode.values) == 2: # Current node has 2 values
					if value < curnode.values[0]:
						curnode.children[0].add_value(value)
						return
					elif value < curnode.values[1]:
						curnode.children[1].add_value(value)
						return
					else:
						curnode.children[2].add_value(value)
						return
						
				else: # Current node has 3 values
					if value < curnode.values[0]:
						curnode.children[0].add_value(value)
						return
					elif value < curnode.values[1]:
						curnode.children[1].add_value(value)
						return
					elif value < curnode.values[2]:
						curnode.children[2].add_value(value)
						return
					else:
						curnode.children[3].add_value(value)
						return
				
		else:
			if curnode.is_full():
				# # print("Pre-emptive split: " + str(curnode))
				curnode = curnode.split()
				
			# # print("Going to node: "	+ str(curnode.goto_subtree(value)))
			self.insert_subtree(curnode.goto_subtree(value), value)
			
			
	def __repr__(self):
		returnstr = "\nTTFTree:\n\nRoot: " + str(self.root)
		
		return returnstr
		
	
	def get(self, value):
		if self.root != None:
			node = self.find_node(value, self.root)
		else:
			return False

		if node != False:
			for i in range(4):
				if node.values[i] == value:
					return node.values[i]
		else:
			return False
	
	def get_all(self):
		self.traverselist = []
		self.inorder(self.root)
		
		return self.traverselist
	
	
	def find_node(self, value, subtree):
		curnode = subtree
		
		if value in curnode.values:
			return curnode
		
		elif curnode.is_leaf():
			print("Tried to find "+str(value)+", but could not find it.")
			return False
			
		else:
			return self.find_node(value, curnode.goto_subtree(value))
			
			
	def delete(self, value):
		to_delete = self.find_node(value, self.root)
		
		if to_delete == False:
			return
		
		if to_delete.is_leaf() and len(to_delete.values) > 1:
			for i in range(len(to_delete.values)):
				if to_delete.values[i] == value:
					to_delete.values.pop(i)
					return
		else:
			self.d_rebuild(value)
			return