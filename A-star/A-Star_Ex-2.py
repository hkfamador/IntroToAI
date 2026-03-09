import heapq


class StoreAisle:
    def __init__(self, aisle_number, category):
        self.aisle_number = aisle_number
        self.category = category
        self.connections = []  # (next_aisle, distance_in_seconds)
        self.congestion_level = 0


class GroceryStore:
    def __init__(self):
        self.aisles = {}
        self.entrance = None
        self.checkout = None

    def add_aisle(self, number, category):
        self.aisles[number] = StoreAisle(number, category)

    def connect_aisles(self, a1, a2, seconds):
        self.aisles[a1].connections.append((a2, seconds))
        self.aisles[a2].connections.append((a1, seconds))

    def set_entrance(self, aisle_number):
        self.entrance = aisle_number

    def set_checkout(self, aisle_number):
        self.checkout = aisle_number

    def update_congestion(self, aisle_number, level):
        if aisle_number in self.aisles:
            self.aisles[aisle_number].congestion_level = level

    def heuristic(self, current_aisle, target_aisle):
        return abs(current_aisle - target_aisle) * 5

    def find_shopping_route(self, shopping_list):

        current_location = self.entrance
        total_time = 0
        full_path = [f"Entrance (Aisle {current_location})"]

        needed_aisles = set()
        for item, aisle in shopping_list:
            needed_aisles.add(aisle)

        print(f"\n🛒 Shopping List:")
        for item, aisle in shopping_list:
            print(f"   • {item} (Aisle {aisle})")

        print(f"\n📍 Starting at Entrance (Aisle {self.entrance})")

        unvisited = list(needed_aisles)

        while unvisited:

            closest_aisle = None
            shortest_time = float('inf')
            best_path = None

            for target in unvisited:
                result = self.find_path(current_location, target)

                if result and result['total_time'] < shortest_time:
                    shortest_time = result['total_time']
                    closest_aisle = target
                    best_path = result['path']

            if closest_aisle:

                print(f"\n   Going to Aisle {closest_aisle} ({shortest_time} seconds)")
                print(f"   Path: {' → '.join([f'Aisle {a}' for a in best_path])}")

                total_time += shortest_time
                full_path.extend([f"Aisle {a}" for a in best_path[1:]])

                current_location = closest_aisle
                unvisited.remove(closest_aisle)

        print(f"\n   Going to Checkout (Aisle {self.checkout})")

        result = self.find_path(current_location, self.checkout)

        if result:
            total_time += result['total_time']
            full_path.extend([f"Aisle {a}" for a in result['path'][1:]])
            full_path.append(f"Checkout (Aisle {self.checkout})")

        return {
            'path': full_path,
            'total_time': total_time,
            'items_collected': len(shopping_list)
        }

    def find_path(self, start, goal):

        open_set = []
        counter = 0

        heapq.heappush(open_set, (0, counter, start, [start]))

        time_so_far = {start: 0}
        visited = set()

        while open_set:

            estimated, _, current, path = heapq.heappop(open_set)

            if current in visited:
                continue

            if current == goal:
                return {
                    'path': path,
                    'total_time': time_so_far[current]
                }

            visited.add(current)

            for next_aisle, base_time in self.aisles[current].connections:

                if next_aisle in visited:
                    continue

                congestion = self.aisles[next_aisle].congestion_level
                congestion_penalty = congestion * 3

                travel_time = base_time + congestion_penalty
                new_time = time_so_far[current] + travel_time

                if next_aisle not in time_so_far or new_time < time_so_far[next_aisle]:

                    time_so_far[next_aisle] = new_time

                    estimated = new_time + self.heuristic(next_aisle, goal)

                    new_path = path + [next_aisle]

                    counter += 1
                    heapq.heappush(open_set, (estimated, counter, next_aisle, new_path))

        return None


# Create store
store = GroceryStore()

store.add_aisle(1, "Produce")
store.add_aisle(2, "Dairy")
store.add_aisle(3, "Meat")
store.add_aisle(4, "Bakery")
store.add_aisle(5, "Canned Goods")
store.add_aisle(6, "Snacks")
store.add_aisle(7, "Frozen Foods")
store.add_aisle(8, "Beverages")
store.add_aisle(9, "Household Items")

store.connect_aisles(1, 2, 10)
store.connect_aisles(2, 3, 8)
store.connect_aisles(3, 4, 12)
store.connect_aisles(4, 5, 10)
store.connect_aisles(5, 6, 8)
store.connect_aisles(6, 7, 10)
store.connect_aisles(7, 8, 12)
store.connect_aisles(8, 9, 15)

store.connect_aisles(2, 5, 20)
store.connect_aisles(4, 7, 18)
store.connect_aisles(1, 9, 30)

store.set_entrance(1)
store.set_checkout(2)

print("\n" + "=" * 60)
print("🛒 GROCERY STORE ROUTE OPTIMIZER")
print("=" * 60)

shopping_list = [
    ("Apples", 1),
    ("Milk", 2),
    ("Chicken", 3),
    ("Bread", 4),
    ("Soda", 8)
]

print("\n📝 SCENARIO: Regular Shopping Trip")
print("-" * 40)

store.update_congestion(2, 2)
store.update_congestion(4, 1)

route = store.find_shopping_route(shopping_list)

if route:

    print(f"\n✅ Shopping complete!")
    print(f"   Total time: {route['total_time']} seconds ({route['total_time']/60:.1f} minutes)")
    print(f"   Items collected: {route['items_collected']}")

    print(f"\n   Complete route:")

    for i, step in enumerate(route['path']):
        print(f"     {i+1}. {step}")