from collections import deque  # Import deque for efficient queue operations

def bfs(graph, start):
    visited = set()              # Set to keep track of visited nodes
    queue = deque([start])       # Initialize a queue with the starting node

    # Continue looping until the queue is empty
    while queue:
        node = queue.popleft()   # Remove the leftmost element from the queue

        # Process the node only if it hasn’t been visited yet
        if node not in visited:
            print(node, end=" ") # Print the current node (visit it)
            visited.add(node)    # Mark the node as visited

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Define a sample graph using an adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the BFS function starting from node 'A'
bfs(graph, 'A')
