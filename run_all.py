from parse import *
import networkx as nx
import os
import solver_greedy as greedy
import solver_trimMST as trimMST
import glob
from utils import *

# only run on s/m/l inputs
if __name__ == "__main__":
	output_dir = "output_trimMST"
	cost_record = open("submission_meta/trimMST1_cost.txt", "a")

	for input_path in glob.glob('inputs/large*.in'):
		graph_name = input_path.split("/")[1] 
		graph_name = graph_name.split(".")[0]

		print("processing {}".format(graph_name))

		G = read_input_file(f"{input_path}")
		T = trimMST.solve(G)
		assert is_valid_network(G, T), "output for {} is invalid".format(graph_name)

		cost = average_pairwise_distance_fast(T)
		cost_record.write(graph_name + ": " + str(cost) + "\n")

		write_output_file(T, f"{output_dir}/{graph_name}.out")

	cost_record.close()

# run all inputs
# if __name__ == "__main__":
#     output_dir = "output"
#     input_dir = "inputs"
#     for input_path in os.listdir(input_dir):
#         graph_name = input_path.split(".")[0]
#         G = read_input_file(f"{input_dir}/{input_path}")
#         T = nx.maximum_spanning_tree(G)
#         write_output_file(T, f"{output_dir}/{graph_name}.out")