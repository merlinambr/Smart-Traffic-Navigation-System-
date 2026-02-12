import heapq

# Graph representing the city (node: [(neighbor, travel_time)])
graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('D', 5), ('E', 12)],
    'C': [('F', 7)],
    'D': [('E', 2)],
    'E': [('G', 3)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic values (estimated time to reach G)
heuristic = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 4,
    'E': 2,
    'F': 3,
    'G': 0
}

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    
    parent = {}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]

        for neighbor, weight in graph[current]:
            new_cost = g_cost[current] + weight

            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = current

    return None, float('inf')


# ===== Main Program =====

print("Smart Traffic Navigation System (A*)")
print("Available Nodes:", list(graph.keys()))

start = input("Enter Start Node: ").upper()
goal = input("Enter Destination Node: ").upper()

path, cost = a_star(start, goal)

if path:
    print("\nOptimal Path:", " -> ".join(path))
    print("Total Travel Time:", cost)
else:
    print("No path found.")
