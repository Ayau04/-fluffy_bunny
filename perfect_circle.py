import pygame
import math

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Circle parameters
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = 200

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Variables for tracking mouse movement
prev_mouse_pos = None
distance_from_center = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Calculate distance from the center of the circle
            mouse_pos = pygame.mouse.get_pos()
            distance = math.sqrt((mouse_pos[0] - CENTER_X) ** 2 + (mouse_pos[1] - CENTER_Y) ** 2)
            distance_from_center.append(distance)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the perfect circle
    pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)

    # Check if the player draws too close to a point
    if distance_from_center and min(distance_from_center) < RADIUS - 5:
        pygame.draw.circle(screen, RED, (CENTER_X, CENTER_Y), RADIUS, 2)

    # Check if the player draws too slowly
    if distance_from_center and len(distance_from_center) >= 10:
        avg_distance = sum(distance_from_center[-10:]) / 10
        if avg_distance < 2:
            pygame.draw.circle(screen, RED, (CENTER_X, CENTER_Y), RADIUS, 2)

    # Calculate the percentage of how perfect the circle is
    if distance_from_center:
        avg_distance = sum(distance_from_center) / len(distance_from_center)
        percentage = max(0, int(((RADIUS - avg_distance) / RADIUS) * 100))
    else:
        percentage = 100

    # Display the percentage on the screen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Perfectness: {percentage}%", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()

