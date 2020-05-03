import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys
from collections import defaultdict

def solve(G):
	"""
	Args:
		G: networkx.Graph

	Returns:
		T: networkx.Graph
	"""
	min_tree = nx.Graph()
	min_cost = float('inf')

	# if by luck there's a node connecting to all other verts, return it 
	for node in G.nodes:
		if len(list(nx.neighbors(G, node))) == nx.number_of_nodes(G) - 1:
			min_tree.add_node(node)
			return min_tree

	start_vertices = starting_point(G)

	# run greedy alg on all starting vertex candidates
	for start_vertex in start_vertices:
		curr_tree = greedy_find_min_tree(G, start_vertex)
		curr_cost = average_pairwise_distance_fast(curr_tree)
		if curr_cost < min_cost:
			min_cost = curr_cost
			min_tree = curr_tree

	return min_tree

# vertices w more than n*DENSE_THRESHOLD neighbors is considered dense
DENSE_THRESHOLD = 0.75
SPARSE_THRESHOLD = 0.25

def starting_point(G):
	""" 
	picks starting point depending on sparcity of graph
	"""
	result = []
	# (node, degree) pairs
	all_degrees = G.degree(G.nodes)
	
	# maps from degree to list of nodes w that degree
	deg_to_nodes = defaultdict(list)
	for node, deg in all_degrees:
		deg_to_nodes[deg].append(node)
		
	max_deg = max(deg_to_nodes)
	min_deg = min(deg_to_nodes)

	# include sparse nodes
	if min_deg <= (len(G) * SPARSE_THRESHOLD):
		if min_deg == 1:
			leaf = deg_to_nodes[min_deg][0] # could optimize this more
			leaf_neighbor = list(G[leaf])[0] 
			result.append(leaf_neighbor)  
		else:
			result.append(deg_to_nodes[min_deg][0])

	# include dense nodes
	if max_deg >= (len(G) * DENSE_THRESHOLD):
		result.append(deg_to_nodes[max_deg][0])  # could optimize this more
	# if there's neither dense nor sparse nodes, default to starting at densest node
	else:
		result.append(deg_to_nodes[max_deg][0])

	return result


def greedy_find_min_tree(G, start_node):#n=2
	"""
	a greedy alg akin to prim's
	"""
	
	tree = nx.Graph()
	tree.add_node(start_node)
	tree_nodes = [start_node]
	reachable_nodes = {start_node}
	min_cost = float('inf')
	min_node = None
	min_node2 = None

	#until found the first dominating set
	while not nx.is_dominating_set(G, tree.nodes):
		# update the min tree
		min_tree = tree
		min_cost = float('inf')
		min_node = None
		for node in tree_nodes:
			neighbors =  nx.neighbors(G, node)
			for neighbor_node in neighbors:
				if (neighbor_node not in tree_nodes) :
					tree_nodes.append(neighbor_node)
					for node2 in tree_nodes:
						neighbors2 = nx.neighbors(G,node2)
						for neighbor_node_2 in neighbors2:
							if (neighbor_node_2 not in tree_nodes): # and (neighbor_node_2!=neighbor_node) and (neighbor_node_2 != node)
								temp_tree = tree.copy()
								edge_weight = G[node][neighbor_node]['weight']
								temp_tree.add_edge(node, neighbor_node)
								temp_tree[node][neighbor_node]['weight'] = edge_weight
								edge_weight2 = G[node2][neighbor_node_2]['weight']
								temp_tree.add_edge(node2, neighbor_node_2)
								temp_tree[node2][neighbor_node_2]['weight'] = edge_weight2
								cost = average_pairwise_distance_fast(temp_tree)
								if cost < min_cost:
									min_cost = cost
									min_tree = temp_tree
									min_node = neighbor_node
									min_node2 = neighbor_node_2
					tree_nodes.pop()

		tree = min_tree
		tree_nodes.append(min_node)
		tree_nodes.append(min_node2)
		reachable_nodes = reachable_nodes | {min_node}
		reachable_nodes = reachable_nodes | {min_node2}

		#updating reachable nodes
		for node in tree_nodes:
			neighbors = set(nx.neighbors(G, node))
			reachable_nodes = reachable_nodes | neighbors

	added = True
	while added:
		# min_tree = tree
		# min_cost = float('inf')
		# min_node = None
		added = False
		for node in tree_nodes:
			neighbors = nx.neighbors(G, node)
			for neighbor_node in neighbors:
				if (neighbor_node not in tree_nodes):
					temp_tree = tree.copy()
					edge_weight = G[node][neighbor_node]['weight']
					temp_tree.add_edge(node, neighbor_node)
					temp_tree[node][neighbor_node]['weight'] = edge_weight
					cost = average_pairwise_distance_fast(temp_tree)
					if (cost < min_cost):
						min_cost = cost
						min_tree = temp_tree
						min_node = neighbor_node
						added = True

		if added:
			tree = min_tree
			tree_nodes.append(min_node)
			reachable_nodes = reachable_nodes | {min_node}

			# updating reachable nodes
			for node in tree_nodes:
				neighbors = set(nx.neighbors(G, node))
				reachable_nodes = reachable_nodes | neighbors

	return tree


# def check_dominating(G, reachable_nodes):
# 	"""
# 	checks if all vertices in G are dominated
# 	"""
# 	return nx.number_of_nodes(G) == len(reachable_nodes)


def greedy_find_min_tree_n(G, start_node, n):
	"""
	a greedy alg akin to prim's
	"""
	tree = nx.Graph()
	tree.add_node(start_node)
	tree_nodes = [start_node]
	reachable_nodes = {start_node}
	min_cost = float('inf')
	min_node = None

	#until found the first dominating set
	while not nx.is_dominating_set(G, tree.nodes):
		# update the min tree
		min_tree = tree
		min_cost = float('inf')
		min_node = None

		#while n >= 0:
			#if n!=0:

			#else:


			#n = n - 1



		for node in tree_nodes:
			neighbors =  nx.neighbors(G, node)
			for neighbor_node in neighbors:
				if (neighbor_node not in tree_nodes) :
					tree_nodes.add(neighbor_node)
					for node2 in tree_nodes:
						neighbors2 = nx.neighbors(G,node2)
						for neighbor_node_2 in neighbors2:
							if (neighbor_node_2 not in tree_nodes): # and (neighbor_node_2!=neighbor_node) and (neighbor_node_2 != node)
								temp_tree = tree.copy()
								edge_weight = G[node][neighbor_node]['weight']
								temp_tree.add_edge(node, neighbor_node)
								temp_tree[node][neighbor_node]['weight'] = edge_weight
								edge_weight2 = temp_tree[node2][neighbor_node_2]['weight']
								temp_tree.add_edge(node2, neighbor_node_2)
								temp_tree[node2][neighbor_node_2]['weight'] = edge_weight2
								cost = average_pairwise_distance_fast(temp_tree)
								if (cost < min_cost):
									min_cost = cost
									min_tree = temp_tree
									min_node = neighbor_node

		tree = min_tree
		tree_nodes.append(min_node)
		reachable_nodes = reachable_nodes | {min_node}

		#updating reachable nodes
		for node in tree_nodes:
			neighbors = set(nx.neighbors(G, node))
			reachable_nodes = reachable_nodes | neighbors

	added = True
	while added:
		# min_tree = tree
		# min_cost = float('inf')
		# min_node = None
		added = False
		for node in tree_nodes:
			neighbors = nx.neighbors(G, node)
			for neighbor_node in neighbors:
				if (neighbor_node not in tree_nodes):
					temp_tree = tree.copy()
					edge_weight = G[node][neighbor_node]['weight']
					temp_tree.add_edge(node, neighbor_node)
					temp_tree[node][neighbor_node]['weight'] = edge_weight
					cost = average_pairwise_distance_fast(temp_tree)
					if (cost < min_cost):
						min_cost = cost
						min_tree = temp_tree
						min_node = neighbor_node
						added = True

		if added:
			tree = min_tree
			tree_nodes.append(min_node)
			reachable_nodes = reachable_nodes | {min_node}

			# updating reachable nodes
			for node in tree_nodes:
				neighbors = set(nx.neighbors(G, node))
				reachable_nodes = reachable_nodes | neighbors

	return tree


if __name__ == '__main__':
	assert len(sys.argv) == 2
	path = sys.argv[1]
	G = read_input_file(path)
	T = solve(G)
	assert is_valid_network(G, T)
	print("Average  pairwise distance: {}".format(average_pairwise_distance_fast(T)))
	write_output_file(T, 'output/test.out')