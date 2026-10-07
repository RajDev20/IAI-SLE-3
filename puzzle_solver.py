"""
SLE-3 / SLE-2: 8-Puzzle Solver (BFS vs DFS) with profiling.
Structure follows the C4 model in the report:

  Input Module      -> make_goal(), shuffle()
  Puzzle Model      -> class PuzzleProblem, get_successors(), is_goal()
  Search Engine     -> bfs(), dfs(), reconstruct_path()
  Visited Set       -> `visited` set inside bfs()/dfs()
  Profiler Module   -> profile_run()
  Output Module     -> print_results(), show_path()
"""
import random
import time
import cProfile
import pstats
import io
from collections import deque

# ---------------------------------------------------------------- Level 4: Node
class Node:
    """A search-tree node: a puzzle state, its parent node and the move that led to it."""
    def __init__(self, state, parent=None, move=None):
        self.state = state      # tuple of 9 ints, 0 = blank
        self.parent = parent
        self.move = move        # 'Up' / 'Down' / 'Left' / 'Right'

# ------------------------------------------------------------ Puzzle Model
class PuzzleProblem:
    """Holds the start and goal state of the 8-puzzle."""
    def __init__(self, start, goal):
        self.start = tuple(start)
        self.goal = tuple(goal)

MOVES = {"Up": -3, "Down": 3, "Left": -1, "Right": 1}

def get_successors(state):
    """Return [(move, new_state), ...] for every legal move of the blank tile."""
    blank = state.index(0)
    row, col = divmod(blank, 3)
    result = []
    for move, delta in MOVES.items():
        if move == "Up" and row == 0:    continue
        if move == "Down" and row == 2:  continue
        if move == "Left" and col == 0:  continue
        if move == "Right" and col == 2: continue
        new = list(state)
        new[blank], new[blank + delta] = new[blank + delta], new[blank]
        result.append((move, tuple(new)))
    return result

def is_goal(state, goal):
    """Goal test: is the current state equal to the goal arrangement?"""
    return state == goal

# ------------------------------------------------------------ Input Module
def make_goal():
    return (1, 2, 3, 4, 5, 6, 7, 8, 0)

def shuffle(goal, moves=25, seed=None):
    """Random walk from the goal, so the start state is always solvable."""
    rng = random.Random(seed)
    state, prev = goal, None
    for _ in range(moves):
        options = [s for _, s in get_successors(state) if s != prev]
        prev, state = state, rng.choice(options)
    return state

# ------------------------------------------------------------ Search Engine
def reconstruct_path(node):
    """Path Reconstructor: follow parent links from the goal node back to the start."""
    moves = []
    while node.parent is not None:
        moves.append(node.move)
        node = node.parent
    return moves[::-1]

def bfs(problem):
    """Breadth-First Search. Frontier = FIFO queue. Returns (moves, nodes_expanded)."""
    frontier = deque([Node(problem.start)])
    visited = {problem.start}
    expanded = 0
    while frontier:
        node = frontier.popleft()                       # pop (FIFO)
        expanded += 1                                   # Node Counter
        if is_goal(node.state, problem.goal):           # Goal Test
            return reconstruct_path(node), expanded
        for move, child in get_successors(node.state):  # Node Expander
            if child not in visited:                    # Explored / Visited Set
                visited.add(child)
                frontier.append(Node(child, node, move))
    return None, expanded

def dfs(problem):
    """Depth-First Search. Frontier = LIFO stack. Returns (moves, nodes_expanded)."""
    frontier = [Node(problem.start)]
    visited = set()
    expanded = 0
    while frontier:
        node = frontier.pop()                           # pop (LIFO)
        if node.state in visited:
            continue
        visited.add(node.state)
        expanded += 1
        if is_goal(node.state, problem.goal):
            return reconstruct_path(node), expanded
        for move, child in get_successors(node.state):
            if child not in visited:
                frontier.append(Node(child, node, move))
    return None, expanded

# ------------------------------------------------------------ Profiler Module
def profile_run(algo, problem, runs=5):
    """Time `algo` over several runs (perf_counter) and run cProfile once."""
    times = []
    for _ in range(runs):
        t0 = time.perf_counter()
        path, expanded = algo(problem)
        times.append((time.perf_counter() - t0) * 1000)  # ms
    pr = cProfile.Profile()
    pr.enable()
    algo(problem)
    pr.disable()
    stats = pstats.Stats(pr, stream=io.StringIO())
    return {
        "avg_ms": sum(times) / len(times),
        "expanded": expanded,
        "solution_len": len(path),
        "calls": stats.total_calls,
        "path": path,
    }

# ------------------------------------------------------------ Output Module
def show_board(state):
    for r in range(3):
        print(" ".join(str(x) if x else "_" for x in state[3*r:3*r+3]))

def print_results(results):
    print(f"\n{'Metric':<28}{'BFS':>14}{'DFS':>14}")
    print("-" * 56)
    rows = [("Avg. time (ms)", "avg_ms", "{:.2f}"),
            ("Nodes expanded", "expanded", "{:,}"),
            ("Solution length (moves)", "solution_len", "{:,}"),
            ("Function calls (cProfile)", "calls", "{:,}")]
    for label, key, fmt in rows:
        print(f"{label:<28}{fmt.format(results['BFS'][key]):>14}{fmt.format(results['DFS'][key]):>14}")

def main(seed=10):
    goal = make_goal()
    start = shuffle(goal, moves=25, seed=seed)
    problem = PuzzleProblem(start, goal)
    print("Start state:"); show_board(start)
    print("\nGoal state:"); show_board(goal)
    results = {"BFS": profile_run(bfs, problem), "DFS": profile_run(dfs, problem)}
    print_results(results)
    print("\nBFS solution (optimal):", " ".join(results["BFS"]["path"]))

if __name__ == "__main__":
    main()
