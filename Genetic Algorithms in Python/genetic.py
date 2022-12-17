import random
import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Genetic Algorithm")

# Set the background color to black
screen.fill((0, 0, 0))

# Set the target value that the genetic algorithm is trying to reach
target_value = 50

# Set the number of genes in each chromosome
num_genes = 10

# Set the size of the population
population_size = 100

# Set the probability of crossover
crossover_probability = 0.8

# Set the probability of mutation
mutation_probability = 0.1

# Set the font for displaying text
font = pygame.font.Font(None, 36)

# Set the color of the target line
target_color = (255, 255, 255)

# Set the color of the chromosomes
chromosome_color = (255, 255, 0)

# Set the maximum number of generations
max_generations = 1000

# Set the generation counter to 0
generation = 0

# Set the best fitness to 0
best_fitness = 0

# Set the best chromosome to None
best_chromosome = None

# Set the fitness function
def fitness(chromosome):
    return abs(sum(chromosome) - target_value)

# Set the initial population
population = [[random.randint(0, 1) for _ in range(num_genes)] for _ in range(population_size)]

# Run the genetic algorithm until the maximum number of generations is reached
while generation < max_generations:
    # Calculate the fitness of each chromosome
    fitnesses = [fitness(chromosome) for chromosome in population]

    # Get the index of the best chromosome
    best_index = fitnesses.index(min(fitnesses))

    # Get the best chromosome
    best_chromosome = population[best_index]

    # Update the best fitness
    best_fitness = min(fitnesses)

    # Stop the algorithm if the best fitness is 0 (i.e., the target value has been reached)
    if best_fitness == 0:
        break

    # Set the probability distribution for selecting chromosomes
    probability_distribution = [fitnesses[i] / sum(fitnesses) for i in range(population_size)]

    # Set the mating pool
    mating_pool = []
    for i in range(population_size):
        mating_pool += [i] * int(probability_distribution[i] * 100)

    # Set the new population
    new_population = []
    while len(new_population) < population_size:
        # Select two chromosomes from the mating pool
        chromosome1 = population[random.choice(mating_pool)]
        chromosome2 = population[random.choice(mating_pool)]

        # Crossover the chromosomes with a probability of crossover_probability
        offspring = chromosome1
        if random.random() < crossover_probability:
                    crossover_point = random.randint(1, num_genes - 1)
        offspring = chromosome1[:crossover_point] + chromosome2[crossover_point:]

        # Mutate the offspring with a probability of mutation_probability
        offspring = [gene if random.random() > mutation_probability else 1 - gene for gene in offspring]

        # Add the offspring to the new population
        new_population.append(offspring)

    # Set the population to the new population
    population = new_population

    # Increment the generation counter
    generation += 1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the target line
    pygame.draw.line(screen, target_color, (window_size[0]//2, 0), (window_size[0]//2, window_size[1]))

    # Draw the chromosomes
    for chromosome in population:
        x = window_size[0] // 2
        y = window_size[1] // 2
        pygame.draw.circle(screen, chromosome_color, (x, y), 5)

    # Display the generation number and best fitness
    text = font.render(f"Generation: {generation}   Best fitness: {best_fitness}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

