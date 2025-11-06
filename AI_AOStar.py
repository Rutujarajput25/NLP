# AO* (And-Or) Search Algorithm Implementation in Python

class Graph:
    def __init__(self, graph, heuristic, start):
        self.graph = graph                 # Adjacency list (with AND/OR structure)
        self.heuristic = heuristic         # Heuristic values for each node
        self.start = start                 # Start node
        self.status = {}                   # Stores status of nodes (-1 = solved)
        self.solution_graph = {}           # Final optimal solution graph

    # Function to get the minimum cost child nodes and cost for a given node
    def get_minimum_cost_child_nodes(self, node):
        min_cost = float('inf')
        best_child_nodes = []
        children = self.graph.get(node, [])

        for child_group in children:  # Each child_group can be OR or AND nodes
            cost = 0
            node_list = []
            for child in child_group:
                cost += self.heuristic[child] + 1  # edge cost = 1 (assumed)
                node_list.append(child)

            if cost < min_cost:
                min_cost = cost
                best_child_nodes = node_list

        return min_cost, best_child_nodes

    # Recursive function implementing AO* algorithm
    def ao_star(self, node):
        print(f"Processing Node: {node}")
        if node not in self.graph or not self.graph[node]:
            self.status[node] = -1  # Solved leaf node
            return

        min_cost, child_nodes = self.get_minimum_cost_child_nodes(node)
        self.heuristic[node] = min_cost
        self.solution_graph[node] = child_nodes
        print(f"Updated heuristic[{node}] = {min_cost}")

        solved = True
        for child in child_nodes:
            if self.status.get(child, 0) != -1:
                solved = False

        if solved:
            self.status[node] = -1
        else:
            for child in child_nodes:
                self.ao_star(child)

    # Function to start AO* search
    def apply_ao_star(self):
        print("\n--- AO* Search Started ---\n")
        self.ao_star(self.start)
        print("\n--- AO* Search Completed ---")
        print("\nSolution Graph:")
        for key, value in self.solution_graph.items():
            print(f"{key} -> {value}")


# Example Graph Representation
# Each key is a node, and its value is a list of possible child combinations.
# A combination may be an OR [A, B] or an AND [A, B] structure.
graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E', 'F']],
    'C': [['G', 'H']],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Heuristic values (initial estimates of cost-to-goal)
heuristic = {
    'A': 10, 'B': 4, 'C': 5, 'D': 2,
    'E': 3, 'F': 2, 'G': 4, 'H': 1
}

# Create AO* object and run algorithm
ao = Graph(graph, heuristic, 'A')
ao.apply_ao_star()
