import random
import matplotlib.pyplot as plt

def fitness_function(x, y):
    # Simple 2D function with a global maximum at x=0.5, y=0.5
    return -((x - 0.5)**2 + (y - 0.5)**2)

def generate_random_point():
    # Generate a random point within the range (-1, 1)
    return (random.uniform(-1, 1), random.uniform(-1, 1))

def generate_initial_population(size):
    # Generate a list of 'size' random points
    return [generate_random_point() for _ in range(size)]

def select_fittest_points(population, num_to_select):
    # Sort the population by fitness
    sorted_population = sorted(population, key=lambda point: fitness_function(*point))
    # Select the top 'num_to_select' points
    return sorted_population[-num_to_select:]

def crossover(point1, point2):
    # Crossover two points by averaging their coordinates
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def mutate(point, mutation_rate):
    # Introduce a random mutation to a point with probability 'mutation_rate'
    x, y = point
    if random.uniform(0, 1) < mutation_rate:
        x += random.uniform(-0.1, 0.1)
        y += random.uniform(-0.1, 0.1)
    return (x, y)

def generate_next_generation(previous_generation, num_to_select, mutation_rate):
    # Select the fittest points from the previous generation
    fittest_points = select_fittest_points(previous_generation, num_to_select)
    # Crossover the fittest points to generate offspring
    offspring = [crossover(fittest_points[i], fittest_points[i + 1]) for i in range(0, len(fittest_points), 2)]
    # Mutate the offspring
    offspring = [mutate(point, mutation_rate) for point in offspring]
    # Combine the fittest points and the offspring to form the next generation
    next_generation = fittest_points + offspring
    return next_generation

def run_genetic_algorithm(num_generations, population_size, num_to_select, mutation_rate):
    # Generate the initial population
    population = generate_initial_population(population_size)

    # Run the genetic algorithm for the specified number of generations
    for i in range(num_generations):
        population = generate_next_generation(population, num_to_select, mutation_rate)

    # Extract the x and y coordinates of the points in the population
    x, y = zip(*population)
    # Plot the points
    plt.scatter(x, y)
    plt.title("Generation {}".format(i))
    plt.show()

# Run the genetic algorithm with the specified parameters
run_genetic_algorithm(num_generations=10, population_size=100, num_to_select=20, mutation_rate=0.1)
