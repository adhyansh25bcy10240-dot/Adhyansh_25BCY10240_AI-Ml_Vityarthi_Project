# PROJECT DESCRIPTION

This project involves exploring all unique nodes by going into depth of the nodes first, i.e,
depth first search. DFS explores as far as possible along each branch before backtracking.
The function used for traversing uses a recursive approach. This program is capable of traversing 
various graph representations. The visited nodes are written in a set to avoid redudancy of nodes and
to avoid infinite looping and accurately track path of exploration.


# ALGORITHM

STEP 1: Starts the DFS process with two important inputs: the Graph (containing nodes and edges) and the Starting Node(root).

STEP 2: Create a 'visited' data structure ( preferably set to avoid repetition) to keep track of all nodes that have been processed to prevent infinite loops.

STEP 3: Mark the Starting Node as 'visited' immediately upon entry and add it to the output list or print it.

STEP 4: Identify all adjacent neighbors of the current node.

STEP 5: Iterate through the list of neighbors one by one.

STEP 6: For each neighbor, check if it is present in the 'visited' set.

STEP 7: If the neighbor has NOT been visited, pause the processing of the current node and recursively call the DFS function for this new neighbor (or push it to the Stack).

STEP 8: Continue this process until a node is reached with no unvisited neighbors nodes.

STEP 9: The process terminates when all reachable nodes from the start have been visited and the recursion stack is empty.

# SOFTWARE USED

Programming Language: Python was used.

Version Control: Git and GitHub were utilized.

Code Editor: VS Code (Visual Studio Code) was the code editor

# Made by- (Adhyansh Raina,25BCY10240)
