import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys
from collections import defaultdict
import queue


def solve(G):
	tree = nx.minimum_spanning_tree(G)
	mst_cost = average_pairwise_distance_fast(G, tree)

	# max leaf heap containing (weight, leaf_node) tuples
	leaf_heap = queue.PrioirtyQueue()

	# keep pruning heaviest leaf from mst until the heaviest leaf becomes too light
	# or the tree is no longer dominating
	while True:
		if not nx.is_dominating_set(G, tree):
			break

		all_degrees = G.degree(G.nodes)
		
		# find all leaves
		deg_to_nodes = defaultdict(list)
		for node, deg in all_degrees:
			deg_to_nodes[deg].append(node)
		leaves = deg_to_nodes[1]

		# add leaves to PQ
		for leaf in leaves:
			leaf_neighbor = list(nx.neighbors(G, leaf))[0]
			leaf_weight = G[leaf][leaf_neighbor]['weight']
			leaf_heap.put((leaf_weight, (leaf, leaf_neighbor)))

		# prune heaviest leaf unless it's smaller than some threshold
		heaviest_leaf = leaf_heap.get()
		if heaviest_leaf[0] < mst_cost: # placeholder
			break
		else:
			leaf = heaviest_leaf[1]
			leaf_neighbor = list(nx.neighbors(G, leaf))[0]
			tree.remove_edge(leaf, leaf_neighbor)

	return tree