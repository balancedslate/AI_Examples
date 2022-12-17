#Basic predator versus prey simulation

import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Simulation parameters
NUM_PREY = 50  # Initial number of prey
NUM_PREDATORS = 10  # Initial number of predators
PREY_SPEED = 5  # Speed of the prey (in pixels per timestep)
PREDATOR_SPEED = 3  # Speed of the predators (in pixels per timestep)
TIMESTEP = 0.1  # Timestep for the simulation (in seconds)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the prey
prey = []
for i in range(NUM_PREY):
    x = random.uniform(0, WIDTH)
    y = random.uniform(0, HEIGHT)
    prey.append(pygame.draw.circle(screen, GREEN, (int(x), int(y)), 5))

# Create the predators
predators = []
for i in range(NUM_PREDATORS):
    x = random.uniform(0, WIDTH)
    y = random.uniform(0, HEIGHT)
    predators.append(pygame.draw.circle(screen, RED, (int(x), int(y)), 5))

# Main loop
running = True
while running:
    # Update the positions of the prey and predators
    for p in prey:
        x, y = p.center
        x += random.uniform(-PREY_SPEED, PREY_SPEED) * TIMESTEP
        y += random.uniform(-PREY_SPEED, PREY_SPEED) * TIMESTEP
        # Keep the prey within the boundaries of the screen
        x = min(max(x, 0), WIDTH)
        y = min(max(y, 0), HEIGHT)
        p.center = (x, y)
    for p in predators:
        x, y = p.center
        closest_prey = None
        closest_distance = float("inf")
        for q in prey:
            x2, y2 = q.center
            distance = ((x - x2)**2 + (y - y2)**2)**0.5
            if distance < closest_distance:
                closest_prey = q
                closest_distance = distance
        if closest_prey:
            # Move towards the closest prey
            x2, y2 = closest_prey.center
            x += (x2 - x) * PREDATOR_SPEED * TIMESTEP / closest_distance
            y += (y2 - y) * PREDATOR_SPEED * TIMESTEP / closest_distance
            # Check if the predator caught the prey
            if closest_distance < 5:
                # Remove the caught prey from the list
                prey.remove(closest_prey)
                # Keep the predators within the boundaries of the screen
            x = min(max(x, 0), WIDTH)
            y = min(max(y, 0), HEIGHT)
            p.center = (x, y)
    # Render the prey and predators
    screen.fill(BLACK)
    for p in prey:
        pygame.draw.circle(screen, GREEN, p.center, 5)
    for p in predators:
        pygame.draw.circle(screen, RED, p.center, 5)
    pygame.display.flip()
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()


