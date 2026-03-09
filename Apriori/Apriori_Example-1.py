from itertools import combinations

# Example: Coffee Shop Order Analysis
# Each order represents what a customer bought in one purchase.
# The Apriori algorithm finds menu items that are frequently bought together.

print("="*50)
print("     APRIORI ALGORITHM - COFFEE SHOP")
print("="*50)

# Orders dataset
# Each list represents one customer's order
orders = [
    ["Coffee","Donut"],           # Order 1
    ["Coffee","Sandwich"],        # Order 2
    ["Coffee","Donut","Muffin"],  # Order 3
    ["Tea","Donut"],              # Order 4
    ["Coffee","Muffin"],          # Order 5
    ["Coffee","Donut"],           # Order 6
    ["Tea","Muffin"],             # Order 7
    ["Coffee","Sandwich","Muffin"] # Order 8
]

total_orders = len(orders)   # Total number of orders
min_support = 0.3            # Minimum support threshold


# Function to calculate support
# Support = number of orders containing the itemset / total orders
def calculate_support(itemset):

    count = 0

    for order in orders:
        if set(itemset).issubset(order):
            count += 1

    support = count / total_orders
    return count, support


# Get all unique menu items
items = set()

for order in orders:
    for item in order:
        items.add(item)

items = list(items)

print("\nStep 1: 1-Itemsets")

for item in items:

    count, support = calculate_support([item])

    print(f"{item}: appears {count} times → support = {count}/{total_orders} = {support:.2f}")

print("-"*50)

print("\nStep 2: 2-Itemsets")

pairs = list(combinations(items,2))   # Generate item pairs

for pair in pairs:

    count, support = calculate_support(pair)

    print(f"{pair}: appears {count} times → support = {count}/{total_orders} = {support:.2f}")