import heapq

graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('E', 5), ('D', 1), ('B', 3)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('G', 3), ('H', 2), ('J', 3), ('E', 5)],
    'J': [('E', 5), ('I', 3)]
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, [start], start))
    visited = set()

    while pq:
        f, g, path, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            g_new = g + cost
            f_new = g_new + heuristic[neighbor]
            heapq.heappush(pq, (f_new, g_new, path + [neighbor], neighbor))

    return None, float('inf')

path, cost = a_star('A', 'J')
print("Most cost-effective path:", " → ".join(path))
print("Total cost:", cost)