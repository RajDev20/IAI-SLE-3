# IAI-SLE-3
8-Puzzle Solver – BFS vs DFS

1. Project Overview

This project implements an 8-Puzzle Solver using two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

The system takes a solvable start state and a goal state, searches for a solution, and compares the performance of BFS and DFS.

The project is based on the same 8-Puzzle system used in SLE-2 and is extended in SLE-3 with a C4 architectural design and performance profiling.

2. Problem Description

The 8-Puzzle is a 3×3 sliding-tile puzzle containing eight numbered tiles and one blank space. The blank tile can move up, down, left, or right when the corresponding position is available.

The objective is to move the tiles from the given start state to the required goal state.

The system uses BFS and DFS to find a solution and records performance information such as:

- Solution path
- Solution length
- Nodes expanded
- Execution time

3. Algorithms Used

Breadth-First Search (BFS)

BFS explores states level by level using a FIFO queue. It is capable of finding the shortest solution path when all moves have equal cost.

Depth-First Search (DFS)

DFS explores one branch deeply before backtracking using a LIFO stack. A visited set is used to prevent repeated states and infinite loops.

4. System Architecture

The system is divided into the following major containers:

1. Input Module – Creates or accepts the start and goal states.
2. Puzzle Model – Generates legal successor states and performs the goal test.
3. Search Engine – Executes BFS and DFS.
4. Visited Set (Memory) – Stores already explored states.
5. Profiler Module – Measures execution time and collects profiling information.
6. Output Module – Displays the solution and performance comparison.

5. Main Classes and Functions

- "Node" – Stores a puzzle state, parent node, and move.
- "PuzzleProblem" – Stores the start and goal states and provides puzzle operations.
- "get_successors(state)" – Generates all legal successor states.
- "is_goal(state)" – Checks whether the current state is the goal.
- "bfs(problem)" – Solves the puzzle using Breadth-First Search.
- "dfs(problem)" – Solves the puzzle using Depth-First Search.
- "reconstruct_path(node)" – Reconstructs the solution path.
- "profile_run(algo, problem)" – Measures algorithm execution time and profiling information.

6. Performance Profiling

The system compares BFS and DFS using:

- Execution time
- Number of nodes expanded
- Solution length
- Function-call profiling using "cProfile"

Each algorithm is run multiple times to obtain performance measurements.

7. Requirements

- Python 3.x
- Python standard libraries
- "matplotlib" for generating comparison charts

8. How to Run

1. Install Python 3.x.
2. Install the required library:

pip install matplotlib

3. Run the Python program:

python main.py

4. The program generates the BFS and DFS results and displays the performance comparison.

9. Expected Output

The program provides:

- Starting puzzle state
- Goal state
- BFS solution path and number of moves
- DFS solution path and number of moves
- Nodes expanded by each algorithm
- Execution time
- BFS vs DFS comparison chart

10. Project Structure

8-Puzzle-Solver/
│
├── main.py
├── README.md
├── contribution_log.md
└── output/
    └── comparison_chart.png

11. SLE-3 Objective

The main objective of SLE-3 is to represent the 8-Puzzle Solver using the C4 Model at four levels:

- Level 1 – Context Diagram
- Level 2 – Container Diagram
- Level 3 – Component Diagram
- Level 4 – Code Level Overview

This architecture shows how the different parts of the system interact and how BFS and DFS are implemented within the Search Engine.

12. Conclusion

The project demonstrates how BFS and DFS can be applied to the 8-Puzzle problem and compared using measured performance data. The C4 architecture provides a clear view of the system from its overall context down to its important classes and functions.
