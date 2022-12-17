import random

# The genetic algorithm will try to optimize this function
def fitness_function(x):
  return x**2 + x + 1

# Generate a population of individuals with random values for the input of the fitness function
def generate_population(pop_size, num_genes):
  population = []
  for i in range(pop_size):
    individual = []
    for j in range(num_genes):
      individual.append(random.randint(-10, 10))
    population.append(individual)
  return population

# Calculate the fitness of each individual in the population
def calculate_fitness(population):
  fitness = []
  for individual in population:
    fit = fitness_function(individual[0])
    fitness.append(fit)
  return fitness

# Select the fittest individuals for reproduction
def selection(population, fitness):
  # Select the fittest individuals
  fittest_individuals = []
  for i in range(len(fitness)):
    max_fitness = max(fitness)
    index = fitness.index(max_fitness)
    fittest_individuals.append(population[index])
    # Remove the individual from the population and the fitness list
    del population[index]
    del fitness[index]
  return fittest_individuals

# Reproduce the fittest individuals to create the next generation
def reproduction(fittest_individuals, num_children):
  next_generation = []
  for i in range(int(num_children/2)):
    parent1 = random.choice(fittest_individuals)
    parent2 = random.choice(fittest_individuals)
    # Select a random crossover point
    crossover_point = random.randint(0, len(parent1)-1)
    # Create the children by combining the genes from each parent
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    next_generation.append(child1)
    next_generation.append(child2)
  return next_generation

# Mutate the genes of some individuals in the population
def mutation(population, mutation_rate):
  for i in range(len(population)):
    if random.uniform(0, 1) < mutation_rate:
      population[i][0] = random.randint(-10, 10)

# Run the genetic algorithm
def genetic_algorithm(pop_size, num_genes, num_children, mutation_rate, num_generations):
  population = generate_population(pop_size, num_genes)
  for i in range(num_generations):
    fitness = calculate_fitness(population)
    fittest_individuals = selection(population, fitness)
    population = reproduction(fittest_individuals, num_children)
    mutation(population, mutation_rate)
  return population

# Test the genetic algorithm
print(genetic_algorithm(pop_size=10, num_genes=1, num_children=10, mutation_rate=0.1, num_generations=10))
