import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys
from collections import defaultdict
import queue


def solve(G):
	tree = nx.minimum_spanning_tree(G)
	cost = average_pairwise_distance_fast(G, tree)

	# max leaf heap containing (weight, leaf_edge) tuples
	leaf_heap = queue.PriorityQueue()
	# keep track of leaves in the heap
	leaves_in_heap = set()

	# keep pruning heaviest leaf from mst until the heaviest leaf becomes too light
	# or the tree is no longer dominating
	while True:
		# (node, degree) pairs
		all_degrees = G.degree(G.nodes)
		
		# find all leaves
		leaves = []
		for node, deg in all_degrees:
			if deg == 1:
				leaves.append(node)

		# add leaves to PQ
		for leaf in leaves:
			leaf_neighbor = list(nx.neighbors(G, leaf))[0]
			leaf_weight = G[leaf][leaf_neighbor]['weight']
			# negate weight to use minPQ as maxPQ
			entry = (-leaf_weight, (leaf, leaf_neighbor))
			if entry not in leaves_in_heap:
				leaf_heap.put(entry)

		
		heaviest = leaf_heap.get()
		edge = heaviest[1]
		tree.remove_edge(edge[0], edge[1])
		# if removing the edge makes the tree non-dominating, put it back
		if not nx.is_dominating_set(G, tree):
			tree.add_edge(edge[0], edge[1])
			break

		# if removing the edge results in greater cost, put it back
		temp_cost = average_pairwise_distance_fast(tree)
		if temp_cost > cost:
			tree.add_edge(edge[0], edge[1])
			break

		# the leaf is officially removed; update leaves set and cost
		leaves_in_heap.remove(heaviest)
		cost = temp_cost

	return tree

