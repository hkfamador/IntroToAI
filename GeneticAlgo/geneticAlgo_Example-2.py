import random

# ================================================
# GA Example: Employee Work Scheduling
# Goal: Assign employees to daily shifts while minimizing conflicts
# Each schedule is a chromosome. Each "shift" is now a real time slot.
# ================================================

employees = ['Alice', 'Bob', 'Charlie', 'Diana']
days = ['Mon', 'Tue', 'Wed', 'Thu']
time_slots = ['Morning', 'Late Morning', 'Afternoon', 'Evening']  # realistic shifts

# Fitness function: higher = fewer conflicts per day
def fitness(schedule):
    score = 0
    for day in days:
        assigned = schedule[day]
        # Count unique employees: fewer duplicates = higher fitness
        score += len(set(assigned)) - len(assigned)
    return score

# Mutation: randomly change a shift assignment
def mutate(schedule):
    day = random.choice(days)
    slot = random.randint(0, len(time_slots)-1)
    schedule[day][slot] = random.choice(employees)

# Crossover: mix shifts from two parents
def crossover(parent1, parent2):
    child = {}
    for day in days:
        child[day] = []
        for slot in range(len(time_slots)):
            if random.random() < 0.5:
                child[day].append(parent1[day][slot])
            else:
                child[day].append(parent2[day][slot])
    return child

# GA parameters
population_size = 6
generations = 10
mutation_rate = 0.3

# Initialize population randomly
population = []
for _ in range(population_size):
    schedule = {day: [random.choice(employees) for _ in time_slots] for day in days}
    population.append(schedule)

# GA iterations
for _ in range(generations):
    population = sorted(population, key=fitness, reverse=True)
    next_gen = population[:2]  # keep top 2
    while len(next_gen) < population_size:
        parents = random.sample(population[:4], 2)
        child = crossover(parents[0], parents[1])
        if random.random() < mutation_rate:
            mutate(child)
        next_gen.append(child)
    population = next_gen

# Best schedule
best_schedule = population[0]

# ------------------- OUTPUT -------------------
print("="*60)
print("      GA EMPLOYEE WORK SCHEDULING (REALISTIC SHIFTS)")
print("="*60)
print("Objective: Assign employees to 4 daily shifts while minimizing conflicts.\n")

for day in days:
    shifts = best_schedule[day]
    print(f"{day}:")
    for slot, emp in zip(time_slots, shifts):
        print(f"   {slot}: {emp}")
    print()

print("="*60)
print("Interpretation: Each employee is assigned to shifts with minimal conflicts per day.\n")