"""
Internal Data structure

Basically a tree.
"""

class DataNode:

	def __init__(self, value, tag=None, children=None, attribute=None):
		self.data = value
		# TODO: check for datatype of list of DataNode
		# TODO: add option to set children=DataNode(1)
		self.children = children

		self.tag = tag
		self.attribute = attribute


	def add(self, node):
		if self.children == None:
			self.children = []
		self.children += [node]


	def height(self):
		if self.children == None:
			return 1
		else:
			return 1 + max([x.height() for x in self.children])


class DataTree:

	def __init__(self, type):
		self.root = DataNode('File')
		self.type = type

	def height(self):
		return self.root.height()
