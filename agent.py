import timeit
import random
from collections import deque


# ============================================================
# SLE-1: STUDY ASSISTANT AI AGENT
# ============================================================

def calculate_percentage(marks):
    """Calculate percentage from marks."""
    total = sum(marks)
    percentage = total / len(marks)
    return percentage


def get_study_tip():
    """Return a random study tip."""
    tips = [
        "Study for 25-30 minutes and take a short break.",
        "Revise important concepts regularly.",
        "Practice programming by writing small programs.",
        "Make short notes for difficult topics.",
        "Solve previous questions for better preparation."
    ]

    return random.choice(tips)


def calculator():
    """Basic calculator."""

    print("\n======================================")
    print("              CALCULATOR")
    print("======================================")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":

            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return

            result = num1 / num2

        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")


def percentage_calculator():
    """Calculate percentage for multiple subjects."""

    print("\n======================================")
    print("        PERCENTAGE CALCULATOR")
    print("======================================")

    try:

        n = int(input("Enter number of subjects: "))

        if n <= 0:
            print("Number of subjects must be greater than 0.")
            return

        marks = []

        for i in range(n):

            mark = float(
                input(f"Enter marks for subject {i + 1}: ")
            )

            marks.append(mark)

        percentage = calculate_percentage(marks)

        print("\nMarks:", marks)

        print(
            "Percentage:",
            round(percentage, 2),
            "%"
        )

    except ValueError:

        print("Please enter valid numbers.")


# ============================================================
# SLE-2: BFS AND DFS
# ============================================================

# Graph used for both BFS and DFS.
# Both algorithms solve exactly the same problem.

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": ["K"],
    "H": [],
    "I": [],
    "J": [],
    "K": []
}

START_NODE = "A"
GOAL_NODE = "K"


# ============================================================
# BFS
# ============================================================

def bfs(graph, start, goal):
    """
    Breadth First Search.

    Returns:
        path
        number of nodes expanded
    """

    queue = deque([[start]])

    visited = set()

    nodes_expanded = 0

    while queue:

        path = queue.popleft()

        current = path[-1]

        if current in visited:
            continue

        visited.add(current)

        nodes_expanded += 1

        # Goal test
        if current == goal:
            return path, nodes_expanded

        for neighbour in graph[current]:

            if neighbour not in visited:

                new_path = path + [neighbour]

                queue.append(new_path)

    return [], nodes_expanded


# ============================================================
# DFS
# ============================================================

def dfs(graph, start, goal):
    """
    Depth First Search.

    Returns:
        path
        number of nodes expanded
    """

    stack = [[start]]

    visited = set()

    nodes_expanded = 0

    while stack:

        path = stack.pop()

        current = path[-1]

        if current in visited:
            continue

        visited.add(current)

        nodes_expanded += 1

        # Goal test
        if current == goal:
            return path, nodes_expanded

        # Reverse order is used so that the graph
        # is explored in a predictable manner.
        for neighbour in reversed(graph[current]):

            if neighbour not in visited:

                new_path = path + [neighbour]

                stack.append(new_path)

    return [], nodes_expanded


# ============================================================
# DISPLAY GRAPH
# ============================================================

def display_graph():

    print("\n======================================")
    print("          GRAPH USED IN SLE-2")
    print("======================================")

    for node in GRAPH:

        print(
            node,
            "->",
            GRAPH[node]
        )

    print("\nStart Node :", START_NODE)
    print("Goal Node  :", GOAL_NODE)


# ============================================================
# SLE-2 PROFILING
# ============================================================

def run_sle2_profiling():

    print("\n======================================")
    print("           SLE-2 PROFILING")
    print("             BFS vs DFS")
    print("======================================")

    display_graph()

    # --------------------------------------------------------
    # Run BFS
    # --------------------------------------------------------

    bfs_path, bfs_nodes = bfs(
        GRAPH,
        START_NODE,
        GOAL_NODE
    )

    # --------------------------------------------------------
    # Run DFS
    # --------------------------------------------------------

    dfs_path, dfs_nodes = dfs(
        GRAPH,
        START_NODE,
        GOAL_NODE
    )

    print("\n======================================")
    print("           SEARCH RESULTS")
    print("======================================")

    print("\nBFS")

    print("Path:",
          " -> ".join(bfs_path))

    print("Nodes Expanded:",
          bfs_nodes)

    print("\nDFS")

    print("Path:",
          " -> ".join(dfs_path))

    print("Nodes Expanded:",
          dfs_nodes)

    # --------------------------------------------------------
    # TIMEIT PROFILING
    # --------------------------------------------------------

    runs = 5
    iterations = 100000

    print("\n======================================")
    print("        PERFORMANCE PROFILING")
    print("======================================")

    print("Number of runs:", runs)

    print(
        "Iterations per run:",
        f"{iterations:,}"
    )

    # BFS timing
    bfs_times = timeit.repeat(
        stmt="bfs(GRAPH, START_NODE, GOAL_NODE)",
        globals={
            "bfs": bfs,
            "GRAPH": GRAPH,
            "START_NODE": START_NODE,
            "GOAL_NODE": GOAL_NODE
        },
        number=iterations,
        repeat=runs
    )

    # DFS timing
    dfs_times = timeit.repeat(
        stmt="dfs(GRAPH, START_NODE, GOAL_NODE)",
        globals={
            "dfs": dfs,
            "GRAPH": GRAPH,
            "START_NODE": START_NODE,
            "GOAL_NODE": GOAL_NODE
        },
        number=iterations,
        repeat=runs
    )

    # Average execution time
    bfs_average = sum(bfs_times) / runs
    dfs_average = sum(dfs_times) / runs

    # Convert to milliseconds
    bfs_ms = bfs_average * 1000
    dfs_ms = dfs_average * 1000

    # Time per single execution
    bfs_single_ms = (
        bfs_average / iterations
    ) * 1000

    dfs_single_ms = (
        dfs_average / iterations
    ) * 1000

    # --------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------

    print("\n======================================")
    print("          COMPARISON TABLE")
    print("======================================")

    print(
        "\nMetric                  BFS             DFS"
    )

    print(
        "------------------------------------------------"
    )

    print(
        f"Average Time (ms)       "
        f"{bfs_ms:.6f}       {dfs_ms:.6f}"
    )

    print(
        f"Time / Execution (ms)   "
        f"{bfs_single_ms:.9f}   {dfs_single_ms:.9f}"
    )

    print(
        f"Nodes Expanded          "
        f"{bfs_nodes:<14} {dfs_nodes}"
    )

    print(
        f"Path Length             "
        f"{len(bfs_path):<14} {len(dfs_path)}"
    )

    # --------------------------------------------------------
    # OBSERVATION
    # --------------------------------------------------------

    print("\n======================================")
    print("             OBSERVATION")
    print("======================================")

    if bfs_ms < dfs_ms:

        print(
            "BFS required less measured execution time "
            "in this experiment."
        )

    elif dfs_ms < bfs_ms:

        print(
            "DFS required less measured execution time "
            "in this experiment."
        )

    else:

        print(
            "Both algorithms had approximately the "
            "same measured execution time."
        )

    if bfs_nodes < dfs_nodes:

        print(
            "BFS expanded fewer nodes for this problem."
        )

    elif dfs_nodes < bfs_nodes:

        print(
            "DFS expanded fewer nodes for this problem."
        )

    else:

        print(
            "Both algorithms expanded the same number "
            "of nodes."
        )

    print(
        "\nBoth algorithms were tested on the same "
        "graph, start node and goal node."
    )

    print(
        "Therefore, the comparison is performed under "
        "the same problem conditions."
    )


# ============================================================
# PY-SPY COMMAND
# ============================================================

def show_pyspy_command():

    print("\n======================================")
    print("              PY-SPY")
    print("======================================")

    print("\nUse this command in the terminal:")

    print(
        "\npy-spy record -o sle2_pyspy.svg -- python agent.py"
    )

    print(
        "\nThis will generate:"
    )

    print(
        "sle2_pyspy.svg"
    )

    print(
        "\nThe SVG file contains the Py-Spy flame graph "
        "showing where Python spends its execution time."
    )


# ============================================================
# AGENT INFORMATION
# ============================================================

def show_agent_info():

    print("\n======================================")
    print("       STUDY ASSISTANT AI AGENT")
    print("======================================")

    print(
        "Course: 02AML204 - Introduction to Artificial Intelligence"
    )

    print(
        "Project: IAI SLE AI Agent"
    )

    print("\nSLE-1 Features:")

    print("1. Percentage Calculator")
    print("2. Study Tips")
    print("3. Basic Calculator")

    print("\nSLE-2 Features:")

    print("4. BFS vs DFS")
    print("5. Node Counting")
    print("6. Execution Time Profiling")
    print("7. Py-Spy Support")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    print("\n======================================")
    print("       IAI STUDY ASSISTANT")
    print("          AI AGENT")
    print("======================================")

    print(
        "Welcome to the Study Assistant AI Agent!"
    )

    while True:

        print("\n======================================")
        print("              MAIN MENU")
        print("======================================")

        print("1. Calculate Percentage")
        print("2. Get Study Tip")
        print("3. Use Calculator")
        print("4. Run SLE-2 BFS vs DFS Profiling")
        print("5. Show Py-Spy Command")
        print("6. Agent Information")
        print("7. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            percentage_calculator()

        elif choice == "2":

            print("\n======================================")
            print("              STUDY TIP")
            print("======================================")

            print(
                get_study_tip()
            )

        elif choice == "3":

            calculator()

        elif choice == "4":

            run_sle2_profiling()

        elif choice == "5":

            show_pyspy_command()

        elif choice == "6":

            show_agent_info()

        elif choice == "7":

            print(
                "\nThank you for using the "
                "Study Assistant AI Agent!"
            )

            print(
                "Good luck with your studies!"
            )

            break

        else:

            print(
                "\nInvalid choice. Please select 1-7."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()
