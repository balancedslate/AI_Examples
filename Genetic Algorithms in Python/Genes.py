import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (640, 480)
window_title = "Genetic Algorithm"

# Create the window and set the caption
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption(window_title)

# Set the target color
target_color = (255, 0, 0)

# Set the population size and mutation rate
population_size = 100
mutation_rate = 0.01

# Create the initial population
population = []
for i in range(population_size):
    # Generate a random color for each member of the population
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    population.append(color)

# Define the main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update the window size when the window is resized
            window_size = event.size
            screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the target color
    pygame.draw.rect(screen, target_color, (0, 0, 100, 100))

    # Calculate the number of rows and columns needed to display the population
    rows = int(window_size[1] / 100)
    columns = int(window_size[0] / 100)

    # Draw the current population
    for i, color in enumerate(population):
        # Calculate the fitness of each member of the population
        fitness = sum([abs(c - t) for c, t in zip(color, target_color)])
        # Calculate the row and column for each member of the population
        row = int(i / columns)
        column = i % columns
        # Draw the color on the screen
        pygame.draw.rect(screen, color, (column * 100, row * 100, 100, 100))
        # Draw the fitness value on the screen
        font = pygame.font.Font(None, 36)
        text = font.render(str(fitness), True, (0, 0, 0))
        screen.blit(text, (column * 100, row * 100))

    # Update the display
    pygame.display.flip()

    # Add a delay to the game loop
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
