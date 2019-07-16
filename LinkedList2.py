class Node:
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

class LinkedList2:  
	def __init__(self):
		self.head = None
		self.tail = None

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
			item.prev = None
			item.next = None
		else:
			self.tail.next = item
			item.prev = self.tail
		self.tail = item

	def print_all_nodes(self):
		node = self.head
		while node != None:
			print(node.value)
			node = node.next

	def print_backwards(self):
		node = self.tail
		while node != None:
			print(node.value)
			node = node.prev

	def find(self, val):
		currentNode = self.head
		if self.head is None:
			return None
		while currentNode is not None:
			if currentNode.value == val:
				return currentNode
			else:
				currentNode = currentNode.next
		return None
		
	def find_all(self, val):
		currentNode = self.head
		listOfNodes = []
		if self.head is None:
			return None
		while currentNode is not None:
			if currentNode.value == val:
				listOfNodes.append(currentNode)
			currentNode = currentNode.next
		if len(listOfNodes) == 0:
			return None
		return listOfNodes

	def delete(self, val, all=False):
		currentNode = self.head
		previousNode = None
		if self.head is None:
			return
		else:
			if self.head.value == val:
				if self.len() == 1:
					self.head = None
					self.tail = None
					return
				else:
					currentNode = self.head.next
					self.head = currentNode
					currentNode.prev = None
					if all==False:
						return
		if all==False:
			while currentNode is not None:
				if currentNode.value == val:
					previousNode.next = currentNode.next
					if currentNode is self.tail:
						self.tail = previousNode
					else:
						currentNode.next.prev = previousNode
					return
				else:
					previousNode = currentNode
					currentNode = currentNode.next
			return
		else:
			while currentNode is not None:
				if currentNode.value == val:
					previousNode.next = currentNode.next
					if currentNode is self.tail:
						self.tail = previousNode
					else:
						currentNode.next.prev = previousNode
					currentNode = currentNode.next
				else:
					previousNode = currentNode
					currentNode = currentNode.next

	def clean(self):
		self.head = None
		self.tail = None
		
	def len(self):
		currentNode = self.head
		nodeCount = 0
		while currentNode is not None:
			nodeCount += 1
			currentNode = currentNode.next
		return nodeCount

	def insert(self, afterNode, newNode):
		if self.head is None:
			self.add_in_head(newNode)
		elif afterNode is None:
			self.add_in_tail(newNode)
		else:
			newNode.prev = afterNode
			if afterNode.next is None:
				self.tail = newNode
			else:
				newNode.next = afterNode.next
				newNode.next.prev = newNode
			afterNode.next = newNode
				

	def add_in_head(self, newNode):
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode

	def delete_head(self):
		if self.head is not None:
			if self.head is self.tail:
				self.clean()
			else:
				self.head.next.prev = None
				self.head = self.head.next

	def delete_tail(self):
		if self.tail is not None:
			if self.head is self.tail:
				self.clean()
			else:
				self.tail.prev.next = None
				self.tail = self.tail.prev    
