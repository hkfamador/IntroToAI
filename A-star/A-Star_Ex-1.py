import heapq
from itertools import product

print("=" * 50)
print("           ROBOT PATH PLANNING (A*)")
print("=" * 50)

# Scenario
print("\nScenario:")
print("Warehouse robot moves from Charging Station to Storage Area.")
print("It can travel through Packing Area, Inspection Area, Quality Check, or Loading Bay.\n")
print("-" * 50)

# Warehouse graph with unique distances
graph = {
    "Charging Station": [("Packing Area", 2), ("Inspection Area", 5), ("Loading Bay", 8)],
    "Packing Area": [("Storage Area", 6), ("Quality Check", 3)],
    "Inspection Area": [("Storage Area", 7), ("Quality Check", 4)],
    "Loading Bay": [("Storage Area", 10)],
    "Quality Check": [("Storage Area", 2)],
    "Storage Area": []
}

heuristic = {
    "Charging Station": 6,
    "Packing Area": 4,
    "Inspection Area": 5,
    "Loading Bay": 7,
    "Quality Check": 1,
    "Storage Area": 0
}


# Function to get all possible routes (DFS)
def get_routes(graph, start, goal, path=[], total_cost=0):
    path = path + [start]
    if start == goal:
        return [(path, total_cost)]
    routes = []
    for neighbor, cost in graph[start]:
        if neighbor not in path:  # avoid cycles
            routes += get_routes(graph, neighbor, goal, path, total_cost + cost)
    return routes


# Generate all routes
all_routes = get_routes(graph, "Charging Station", "Storage Area")

# Print available routes
print("Available Routes:")
for idx, (route, cost) in enumerate(all_routes, 1):
    route_str = " -> ".join(route)
    print(f"{idx}. {route_str} ({cost})")
print("\n" + "-" * 50)


# Correct A* Implementation
def astar(start, goal):
    queue = [(heuristic[start], 0, start, [])]  # (f = g+h, g, node, path)
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == goal:
            return path, g
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g_new = g + weight
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(queue, (f_new, g_new, neighbor, path))


# Run A* and print the result
path, cost = astar("Charging Station", "Storage Area")
print("Shortest Path Selected by A*:")
print(" -> ".join(path))
print(f"Total Distance: {cost} meters")
print("=" * 50)