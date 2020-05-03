import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys
#import solver_naive as solver_naive
import solver_greedy2 as solver_greedy1
import solver_greedy2_more_edges as solver_greedy2
import solver_trimMST as solver_mst
import solver_ds_spt as solver_spt


def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    # TODO: your code here!
    #hard code methods
    #greedy2
    #greedy2_more_edges (only small and median)
    #trimMST
    #ds_spt

    #compute the cost only if not none

    min_cost = float('inf')
    min_tree = None

    #if val is not None:

    """
    tree_naive = solver_naive.solve(G)
    if (tree_naive is not None):
        if average_pairwise_distance_fast(tree_naive) < min_cost:
            min_cost = average_pairwise_distance_fast(tree_naive)
            min_tree = tree_naive
    """

    tree_greedy1 = solver_greedy1.solve(G)
    if average_pairwise_distance_fast(tree_greedy1) < min_cost:
        min_cost = average_pairwise_distance_fast(tree_greedy1)
        min_tree = tree_greedy1

    if (nx.number_of_nodes(G) == 25 or nx.number_of_nodes(G) == 50):
        tree_greedy2 = solver_greedy2.solve(G)
        if average_pairwise_distance_fast(tree_greedy2) < min_cost:
            min_cost = average_pairwise_distance_fast(tree_greedy2)
            min_tree = tree_greedy2


    tree_mst = solver_mst.solve(G)
    if average_pairwise_distance_fast(tree_mst) < min_cost:
        min_cost = average_pairwise_distance_fast(tree_mst)
        min_tree = tree_mst

    tree_spt = solver_spt.solve(G)
    if average_pairwise_distance_fast(tree_spt) < min_cost:
        min_cost = average_pairwise_distance_fast(tree_spt)
        min_tree = tree_spt

    return min_tree


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
