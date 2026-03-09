import heapq

print("=" * 50)
print("         VIDEO GAME AI PATHFINDING (A*)")
print("=" * 50)

# Scenario
print("\nScenario:")
print("Enemy AI moves from Spawn Point to Player Base across Forest, River, Hill, and Bridge.\n")
print("-" * 50)

# Graph with unique movement costs
graph = {
    "Spawn Point": [("Forest", 3), ("River", 5), ("Hill", 4)],
    "Forest": [("Player Base", 7), ("Bridge", 3)],
    "River": [("Player Base", 6), ("Bridge", 2)],
    "Hill": [("Bridge", 4)],
    "Bridge": [("Player Base", 1)],
    "Player Base": []
}

heuristic = {
    "Spawn Point": 6,
    "Forest": 4,
    "River": 5,
    "Hill": 3,
    "Bridge": 1,
    "Player Base": 0
}


# Function to get all possible routes (DFS)
def get_routes(graph, start, goal, path=[], total_cost=0):
    path = path + [start]
    if start == goal:
        return [(path, total_cost)]
    routes = []
    for neighbor, cost in graph[start]:
        if neighbor not in path:
            routes += get_routes(graph, neighbor, goal, path, total_cost + cost)
    return routes


# Generate all routes
all_routes = get_routes(graph, "Spawn Point", "Player Base")

# Print available routes
print("Available Routes:")
for idx, (route, cost) in enumerate(all_routes, 1):
    route_str = " -> ".join(route)
    print(f"{idx}. {route_str} ({cost})")
print("\n" + "-" * 50)


# Correct A* algorithm
def astar(start, goal):
    queue = [(heuristic[start], 0, start, [])]  # (f=g+h, g, node, path)
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == goal:
            return path, g  # return real movement cost
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g_new = g + weight
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(queue, (f_new, g_new, neighbor, path))


# Run A* and print result
path, cost = astar("Spawn Point", "Player Base")
print("Shortest Path Selected by A*:")
print(" -> ".join(path))
print(f"Total Movement Cost: {cost}")
print("=" * 50)
