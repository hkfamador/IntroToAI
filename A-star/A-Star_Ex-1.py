import heapq


class Location:
    def __init__(self, name):
        self.name = name
        self.connections = []  # (neighbor, distance_in_minutes)

    def add_path(self, neighbor, minutes):
        self.connections.append((neighbor, minutes))


class SchoolRouter:
    def __init__(self):
        self.locations = {}

    def add_location(self, name):
        self.locations[name] = Location(name)

    def add_road(self, loc1, loc2, minutes):
        """Add a walking path between two locations"""
        self.locations[loc1].add_path(self.locations[loc2], minutes)
        self.locations[loc2].add_path(self.locations[loc1], minutes)

    def heuristic(self, current, goal):
        """Simple straight-line estimate"""
        if current.name == goal.name:
            return 0
        elif "Park" in current.name:
            return 5
        elif "Store" in current.name:
            return 3
        else:
            return 2

    def find_shortest_route(self, start_name, goal_name):
        """A* search to find shortest walking route"""

        start = self.locations[start_name]
        goal = self.locations[goal_name]

        open_set = []
        counter = 0

        heapq.heappush(open_set, (0, counter, start, [start.name]))

        time_so_far = {start.name: 0}
        visited = set()

        print(f"\n📍 Finding route from {start_name} to {goal_name}")
        print("-" * 40)

        while open_set:
            estimated_total, _, current, path = heapq.heappop(open_set)

            if current.name in visited:
                continue

            print(f"   Checking: {current.name}")

            if current.name == goal_name:
                return {
                    "path": path,
                    "total_time": time_so_far[current.name],
                    "locations_checked": len(visited),
                }

            visited.add(current.name)

            for neighbor, travel_time in current.connections:

                if neighbor.name in visited:
                    continue

                new_time = time_so_far[current.name] + travel_time

                if neighbor.name not in time_so_far or new_time < time_so_far[neighbor.name]:
                    time_so_far[neighbor.name] = new_time

                    estimated = new_time + self.heuristic(neighbor, goal)
                    new_path = path + [neighbor.name]

                    counter += 1
                    heapq.heappush(open_set, (estimated, counter, neighbor, new_path))

        return None


# Create router
router = SchoolRouter()

# Add locations
locations = [
    "Home",
    "School",
    "Park",
    "Store",
    "Library",
    "Bus Stop",
    "Friend's House",
    "Bakery",
]

for loc in locations:
    router.add_location(loc)

# Add roads

router.add_road("Home", "Store", 5)
router.add_road("Home", "Park", 8)
router.add_road("Home", "Friend's House", 4)

router.add_road("Store", "Bakery", 3)
router.add_road("Store", "Bus Stop", 6)

router.add_road("Park", "Library", 4)
router.add_road("Park", "School", 7)

router.add_road("Library", "Bus Stop", 5)
router.add_road("Library", "School", 3)

router.add_road("Friend's House", "Bakery", 4)
router.add_road("Friend's House", "Bus Stop", 7)

router.add_road("Bakery", "Bus Stop", 4)

router.add_road("Bus Stop", "School", 8)


print("\n" + "=" * 50)
print("🚶 STUDENT'S WALKING ROUTE PLANNER")
print("=" * 50)

# Only Scenario: Home to School
route = router.find_shortest_route("Home", "School")

if route:
    print("\n✅ Best route found!")
    print(f"   Path: {' → '.join(route['path'])}")
    print(f"   Total walking time: {route['total_time']} minutes")
    print(f"   Locations checked: {route['locations_checked']}")