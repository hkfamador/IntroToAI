from itertools import combinations

# Example: Streaming Platform Recommendation
# A "session" represents one user's viewing activity.
# Each session contains shows watched during one visit.
# The Apriori algorithm will find shows frequently watched together.

print("="*50)
print("   APRIORI ALGORITHM - STREAMING PLATFORM")
print("="*50)

# Viewing session dataset
# Each list represents one session
sessions = [
    ["Stranger Things","The Witcher"],        # Session 1
    ["Stranger Things","Wednesday"],          # Session 2
    ["The Witcher","Wednesday"],              # Session 3
    ["Stranger Things","The Witcher","Wednesday"],  # Session 4
    ["Stranger Things","The Witcher"],        # Session 5
    ["Stranger Things","Loki"],               # Session 6
    ["Loki","The Witcher"],                   # Session 7
    ["Stranger Things","Loki","Wednesday"]    # Session 8
]

total_sessions = len(sessions)   # Total number of viewing sessions
min_support = 0.3                # Minimum support threshold

# Function to calculate support
# Support = number of sessions containing the itemset / total sessions
def calculate_support(itemset):

    count = 0

    for session in sessions:
        if set(itemset).issubset(session):
            count += 1

    support = count / total_sessions
    return count, support


# Get all unique shows from the dataset
shows = set()

for s in sessions:
    for show in s:
        shows.add(show)

shows = list(shows)

print("\nStep 1: 1-Show Itemsets")

for show in shows:

    count, support = calculate_support([show])

    print(f"{show}: appears {count} times → support = {count}/{total_sessions} = {support:.2f}")

print("-"*50)

print("\nStep 2: 2-Show Itemsets")

pairs = list(combinations(shows,2))   # Generate pairs of shows

for pair in pairs:

    count, support = calculate_support(pair)

    print(f"{pair}: appears {count} times → support = {count}/{total_sessions} = {support:.2f}")