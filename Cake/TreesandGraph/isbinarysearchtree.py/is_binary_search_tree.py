  def is_binary_search_tree(root):
  	# Depth First Search

  	node_and_bounds_stack = [(root, -float('int'), float('inf'))]

  	while (len(node_and_bounds_stack)):
  		node, lower_bound, upper_bound = node_and_bounds_stack

  		if (node.value <= lower_bound) or (node.value >= upper_bound):
  			return False

  		if node.left:
  			node_and_bounds_stack.append((node.left, lower_bound, node.value))

  		if node.right:
  			node_and_bounds_stack.append((node.right, node.value, upper_bound))

  	return True

# Recursively
def is_binary_search_tree(root,
                      lower_bound=-float('inf'),
                      upper_bound=float('inf')):
if not root:
    return True

if (root.value >= upper_bound or root.value <= lower_bound):
    return False

return (is_binary_search_tree(root.left, lower_bound, root.value)
        and is_binary_search_tree(root.right, root.value, upper_bound))