import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys


def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    # TODO: your code here!

    """
    1. find starting vertices set
    2. input each starting vertex into alg (list comprehension)
    3. return the minimum routing cost tree among all possible starting index
    """
    pass

def findMinTree(G, start_node):
    tree = nx.Graph()
    tree.add_node(start_node)
    tree_nodes = [start_node]
    reachable_nodes = {start_node}

    #until found the first dominating set

    while (not checkDominating(G, reachable_nodes)) :
        # update the min tree
        min_tree = tree
        min_cost = float('inf')
        min_node = None
        for node in tree_nodes:
            neighbors =  nx.neighbors(G, node)
            for neighbor_node in neighbors:
                if (neighbor_node not in tree_nodes) :
                    temp_tree = tree
                    edge_weight  = G[node][neighbor_node]['weight']
                    temp_tree.add_edge(node, neighbor_node)
                    temp_tree[node][neighbor_node]['weight'] = edge_weight
                    cost = average_pairwise_distance(temp_tree)
                    if (cost < min_cost):
                        min_cost = cost
                        min_tree = temp_tree
                        min_node = neighbor_node

        tree = min_tree
        tree_nodes.append(min_node)
        reachable_nodes = reachable_nodes | {min_node}

        #updating reachable nodes
        for node in tree_nodes:
            #reachable_nodes = reachable_nodes | {node}
            neighbors = set(nx.neighbors(G, node))
            reachable_nodes = reachable_nodes | neighbors



    #check if want to add edge to the dominating tree

def checkDominating(G, reachable_nodes):
    #check if size of reachable_nodes equal to the total number of vertices in G
    return nx.number_of_nodes(G) == len(reachable_nodes)

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G = read_input_file(path)
#     T = solve(G)
#     assert is_valid_network(G, T)
#     print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
#     write_output_file(T, 'out/test.out')
