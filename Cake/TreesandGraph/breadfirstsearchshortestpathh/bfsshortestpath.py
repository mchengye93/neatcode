from collections import deque

def bfs(graph, start_node, end_node):

	nodes_to_vist = deque()
	nodes_to_vist.append(start_node)

	how_we_reached_nodes = {start_node:None}

	while len(nodes_to_vist) > 0:
		current_node = nodes_to_vist.popleft()


		if current_node == end_node:
			return reconstruct_path(how_we_reached_nodes, start_node, end_node)

		for neighbor in graph[current_node]:
			nodes_to_vist.append(neighbor)
			how_we_reached_nodes[neighbor] = current_node
	return None


def reconstruct_path(previous_nodes, start_node, end_node):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current_node = end_node
    while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed