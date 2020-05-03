# CS 170 Project Spring 2020

Requirements:

You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: calls all other solvers and return the optimal output
  - `solver_greedy2.py`: a solver created using greedy algorithm
  - `solver_greedy2_more_edges.py`: a solver created by modifiying solver_greedy2 to explore more edges in each iteration
  - `solver_trimMST.py`: a solver created by trimming minimum spanning trees
  - `solver_ds_spt.py`: a solver created by shortest paths tree
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

Instructions to run the solver:
1. `cd` into this project directory `network-alg-proj`
2. Create a directory named `output` in the project directory using `mkdir output`.
3. Type `python3 run_all.py` to the command line. 
  - This command will run all inputs stored in the `inputs` directory using our solver in solver.py and write all output .out       files into `output` directory.
