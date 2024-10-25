import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up screen dimensions and create the game window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumping Game")

# Set up game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Set up player attributes
player_size = 50
player_x = 100
player_y = SCREEN_HEIGHT - player_size
player_velocity = 0
GRAVITY = 1
JUMP_FORCE = -15

# Set up obstacle attributes
obstacle_width = 50
obstacle_height = 50
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - obstacle_height

# Load fonts
font = pygame.font.Font(None, 36)

# Player score
score = 0

def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_size, player_size))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def display_text(text, x, y):
    screen_text = font.render(text, True, BLACK)
    screen.blit(screen_text, (x, y))

# Main game loop
running = True
game_over = False
while running:
    screen.fill(WHITE)
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Jump when spacebar or mouse button is pressed
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over and (event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN):
                if player_y == SCREEN_HEIGHT - player_size:
                    player_velocity = JUMP_FORCE
            elif game_over:
                # Restart the game after game over
                game_over = False
                obstacle_x = SCREEN_WIDTH
                player_y = SCREEN_HEIGHT - player_size
                player_velocity = 0
                score = 0
    
    if not game_over:
        # Update player position
        player_velocity += GRAVITY
        player_y += player_velocity
        if player_y >= SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size

        # Update obstacle position
        obstacle_x -= 10
        if obstacle_x < -obstacle_width:
            obstacle_x = SCREEN_WIDTH
            score += 1

        # Check for collisions
        if (player_x < obstacle_x + obstacle_width and player_x + player_size > obstacle_x and
            player_y + player_size > obstacle_y):
            game_over = True

        # Draw player and obstacle
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # Display score
        display_text(f"Score: {score}", 10, 10)
    
    else:
        # Display Game Over
        display_text("Game Over! Press space to restart.", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
