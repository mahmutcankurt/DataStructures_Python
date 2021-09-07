class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def traversal(root):

	current = root

	while(current != None):

		if(current.left == None):
			yield current.data
			current = current.right

		else:
			pre = current.left
			while pre.right is not None and pre.right is not current:
				pre = pre.right

			if(pre.right == None):
				pre.right = current
				current = current.left

			else:
				pre.right = None
				yield current.data
				current = current.right

root = Node(1,
	right=Node(3),
	left=Node(2,
		left=Node(4),
		right=Node(5)
	)
)

for i in traversal(root):
	print(i, end=" ")

