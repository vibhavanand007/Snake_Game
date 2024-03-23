# This code is a simple Snake Game implemented using Pygame in Python.
# It includes functions to draw the snake, handle game events, display score, and run the game loop.

# Required Libraries
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

# Set the game display dimensions
width, height = 600, 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vibhav Snake Game")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Snake properties
snake_size = 10
# snake_speed = 5

# Fonts for messages and score
message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

# Function to display the score
def print_score(score):
    text = score_font.render("Score/Level >>  " + str(score), True, black)
    game_display.blit(text, [0, 0])

# Function to draw the snake
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, orange, [pixel[0], pixel[1], snake_size, snake_size])

# Main game loop
def run_game():
    # Game variables
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_speed = 0
    y_speed = 0
    snake_pixels = []
    snake_length = 1
    snake_speed = 5

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        # Game Over Screen
        while game_close:

            # Display Game Over message and score
            game_display.fill(white)
            game_over_message = message_font.render("Game Over...", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            # Event handling for Game Over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # Event handling for main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        # Check for boundaries collision
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Update snake position
        x += x_speed
        y += y_speed

        # Refresh the game display
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        # Adjust snake length
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        # Check for self-collision
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        # Draw the snake and display score
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        # Check if snake has eaten the target
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1
            snake_speed += 1

        # Control game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
run_game()