import random

# Distance matrix for TSP
distance_matrix = [
    [0, 29, 20, 21, 16, 31],
    [29, 0, 15, 29, 28, 40],
    [20, 15, 0, 15, 14, 25],
    [21, 29, 15, 0, 22, 35],
    [16, 28, 14, 22, 0, 20],
    [31, 40, 25, 35, 20, 0]
]
cities = ["A", "B", "C", "D", "E", "F"]


'''

        A
       /|\
      / | \
  29 /  |  \ 20
    /   |   \
   B    |    C
   |\   |   /|
   | \  |  / |
   |  \ | /  |
  15   16   14
   |   / \   |
   |  /   \  |
   | /     \ |
   D----22----E
    \         /
     \       /
      \     /
       35  20
        \ /
         F

'''
# --- Genetic Algorithm Functions ---

# Calculate the total distance of a route
def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to starting point
    return total_distance

# Fitness function: higher fitness for shorter routes
def fitness(route):
    return 1 / calculate_distance(route)

# Generate a random route starting with A
def generate_route(num_cities):
    route = list(range(1, num_cities))  # Exclude A (index 0)
    random.shuffle(route)
    return [0] + route  # Ensure A is always the first city

# Generate an initial population of routes
def generate_population(pop_size, num_cities):
    return [generate_route(num_cities) for _ in range(pop_size)]

# Select a parent using roulette wheel selection
def select_parent(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, fitness_value in enumerate(fitnesses):
        current += fitness_value
        if current > pick:
            return population[i]

# Ordered Crossover (OX), preserving A as the starting point
def ordered_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(1, size), 2))  # Skip index 0 (A)
    child = [-1] * size
    child[0] = 0  # Fix A as the starting point
    child[start:end + 1] = parent1[start:end + 1]
    current_pos = (end + 1) % size
    for city in parent2:
        if city not in child:
            while child[current_pos] != -1:
                current_pos = (current_pos + 1) % size
            child[current_pos] = city
    return child

# Mutation: Swap two cities (excluding A)
def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(route)), 2)  # Skip index 0 (A)
        route[i], route[j] = route[j], route[i]

# --- Genetic Algorithm Implementation ---

def genetic_algorithm(
    pop_size=100, 
    generations=500, 
    mutation_rate=0.02, 
):
    num_cities = len(cities)
    population = generate_population(pop_size, num_cities)

    for generation in range(generations):
        # Calculate fitness for the current population
        fitnesses = [fitness(route) for route in population]

        # Create the next generation
        next_population = []
        for _ in range(pop_size // 2):
            # Select parents
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            # Generate offspring via crossover
            child1 = ordered_crossover(parent1, parent2)
            child2 = ordered_crossover(parent2, parent1)
            # Apply mutation
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_population.extend([child1, child2])

        population = next_population

        # Find the best route in the current generation
        best_route = min(population, key=calculate_distance)
        best_distance = calculate_distance(best_route)

        print(f"Generation {generation + 1}: Best Distance = {best_distance}, Best Route = {[cities[i] for i in best_route]}")

    # Return the best route and its distance
    best_route = min(population, key=calculate_distance)
    return best_route, calculate_distance(best_route)

# --- Run Genetic Algorithm ---

# Parameters
population_size = 100
num_generations = 500
mutation_rate = 0.02

best_route, best_distance = genetic_algorithm(
    pop_size=population_size, 
    generations=num_generations, 
    mutation_rate=mutation_rate
)

# Print the result
print(f"Optimal Route: {[cities[i] for i in best_route]}, Total Distance: {best_distance}")
