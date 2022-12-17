import pygame
import random
import sys

# Set the width and height of the window
WIDTH, HEIGHT = 800, 600

# Initialize Pygame
pygame.init()

# Set the window title
pygame.display.set_caption("Visual Genetic Algorithm")

# Set the window size and position
pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# Set the background color to white
screen = pygame.display.get_surface()
bg_color = pygame.Color('white')

# Create a population of random circles
population = []
for i in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.randint(10, 50)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), r)
    population.append(((x, y), r))

# Run the genetic algorithm
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(bg_color)

    # Draw the circles
    for center, radius in population:
        pygame.draw.circle(screen, (0, 0, 0), center, radius)

    # Select the fittest circles
    fittest = []
    for i in range(10):
        fittest.append(random.choice(population))

    # Create a new generation of circles by mutating the fittest ones
    new_generation = []
    for center, radius in fittest:
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        r = random.randint(10, 50)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), r)
        new_generation.append(((x, y), r))

    # Replace the current population with the new generation
    population = new_generation

    # Update the display
    pygame.display.update()
