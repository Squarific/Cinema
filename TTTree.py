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

	def is_full2(self):
		return len(self.values) >= 2 
		
		
	def is_root(self):
		return self.parent == None

			



	def split(self):
		"""Splits a node with 3 values into 3 nodes, with the middle value being the parent of the other two."""
		self.values.append(6)
		self.values.append(7)
		print(self.values)
		if self.is_root():
			lchild = Node(self, self.values[0])
			rchild = Node(self, self.values[2])
			lchild.children = []
			rchild.children = []

			for i in range(len(self.children)):
				if self.children[i] < self.values[1]:
					lchild.children.append(self.children[i])
				else:
					rchild.children.append(self.children[i])
			for i in range(len(lchild.children)):
				lchild.children[i].parent = lchild
			for j in range(len(rchild.children)):
				rchild.children[j].parent = rchild
			
			self.values = [self.values[1]]
			
			self.children = [lchild,rchild]
			
			return self
		else:
			self.mergesplit()
			
			return self.parent

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
			
			
	def add_value(self, value):
		if not self.is_full2():
			self.values.append(value)
			self.values.sort()
		else:
			print("ERROR: Node already has 2 values.\n(tried to insert " + str(value) + ")")

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

		
class TwoThreeTree:
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

	def insert(self, searchkey, value):
		if self.root == None: # Empty Tree
			self.root = Node(None, value)
			return
		else:
			self.insert_subtree(self.root, value) # Tree is not empty


	def insert_subtree(self, subtree, value):
		curnode = subtree

		if curnode.is_leaf(): # current node is a leaf
			if not curnode.is_full2(): # current node is not full
				curnode.add_value(value)
				return

			else:
				curnode.add_value(value)
				# # print("Splitting node: " + str(curnode))
				curnode = curnode.split()
				# # print("Current node is now: " + str(curnode))
				
				# Curnode is now the parent of a leaf

				if len(curnode.values) == 3:

					curnode = curnode.split()



		else:
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
			for i in range(3):
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
		
			
		else:
			return self.find_node(value, curnode.goto_subtree(value))

	def delete(self, value):
		to_delete = self.find_node(value, self.root)
		
		if to_delete == False:
			return False
		if to_delete.is_root():
			if len(to_delete.values == 1):
				to_delete.values.pop()
				return
		if to_delete.is_leaf():
			if len(to_delete.values) > 1:
				for i in range(len(to_delete.values)):
					if to_delete.values[i] == value:
						to_delete.values.pop(i)
						return
			else:
				self.d_rebuild(value)
				return
		else:
			takeClosest = lambda num, collection:min(collection,key=lambda x:abs(x-num))
			swap = takeClosest(value, to_delete.children)
			value1 = value
			value2 = swap
			to_delete.values.remove(value)
			to_delete.values.append(value2)
			to_delete.values.sort()
			to_delete.children.remove(swap)
			to_delete.children.append(value1)
			to_delete.children.sort()
			delete(self, value)
