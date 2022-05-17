def find_largest(root_node):
	current = node
	while current:
		if not current.right:
			return current.value
		current = current.right

def find_second_largest(root_node):

	current = root_node

	while current:

		# Case 1: current is largest and has left subtree and not rigt subtree
		if current.left and not current.right:
			return find_largest(root_node)

		# Case 2: Current is parent of largest and largest has no children
		if current.right and not current.left and not current.right.right:
			return current.value

		current = current.right