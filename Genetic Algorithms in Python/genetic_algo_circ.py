import pygame
import random

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

# Define a class for circles
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self, surface, color):
        pygame.draw.circle(surface, color, (self.x, self.y), self.r)

# Create a population of random circles
population = []
for i in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.randint(10, 50)
    population.append(Circle(x, y, r))

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
    for circle in population:
        circle.draw(screen, (0, 0, 0))

    # Select the fittest circles
    fittest = []
    for i in range(10):
        fittest.append(random.choice(population))

    # Create a new generation of circles by mutating the fittest ones
    new_generation = []
    for circle in fittest:
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        r = random.randint(10, 50)
        new_generation.append(Circle(x, y, r))

    # Replace the current population with the new generation
    population = new_generation

    # Update the display
    pygame.display.update()
