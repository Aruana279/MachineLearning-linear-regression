# cs4341-a1
A* on a board with obstacles

To run the file, use: 
python astar.py [filename] [heuristic]

where heuristic is 1-6 corresponding to the instructions. 

running file:
- command line arguments for the file path and heuristic type

board class:
- reads the file and store the information in a 2d array
- get start and end positions
- track current position of robot (including heading)

robot class:
- generate_neighbors_with_cost()
    - calculated using the actions
    - return list of tuples (resulting board state, cost)

A* class:
- instantiated with which type of heuristic to use
- heuristic functions (one for each type)
- search()

tests: 
