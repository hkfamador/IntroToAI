import random
import math

def f(x):
    return x * math.sin(x)

population = [random.uniform(0,10) for _ in range(6)]
generations = 20
mutation_rate = 0.3

def fitness(x):
    return f(x)

def select(pop):
    # Tournament selection: pick 2 random and select the better
    a, b = random.sample(pop, 2)
    return a if fitness(a) > fitness(b) else b

def crossover(x1, x2):
    # Weighted average with randomness
    alpha = random.uniform(0,1)
    return x1*alpha + x2*(1-alpha)

def mutate(x):
    if random.random() < mutation_rate:
        x += random.uniform(-1.5,1.5)
        x = max(0,min(10,x))
    return x

# GA iterations
for g in range(generations):
    new_pop = []
    for _ in range(len(population)):
        p1 = select(population)
        p2 = select(population)
        child = crossover(p1,p2)
        child = mutate(child)
        new_pop.append(child)
    population = new_pop

best = max(population,key=fitness)

# Best candidate in understandable form
best = max(population, key=fitness)

print("="*60)
print("       GENETIC ALGORITHM: FUNCTION OPTIMIZATION")
print("="*60)
print("Objective: Find x in [0,10] that maximizes f(x) = x * sin(x)\n")

# Show best solution
print("➡ Best candidate found by GA:")
print(f"   x = {round(best,4)} → f(x) = {round(f(best),4)}\n")

# Show other candidates clearly
print("➡ Final population (other candidates and their fitness):")
for i, x in enumerate(population,1):
    print(f"   Candidate {i}: x = {round(x,4)}, f(x) = {round(f(x),4)}")

print("="*60)
print("Interpretation: The GA explored multiple x values and converged to a near-optimal solution.\n")