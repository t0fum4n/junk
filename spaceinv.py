import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Space Invaders")

# Set the font for the score
font = pygame.font.Font(None, 36)

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set the player dimensions and position
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10

# Set the bullet dimensions and position
bullet_width = 5
bullet_height = 20
bullet_x = player_x + (player_width / 2) - (bullet_width / 2)
bullet_y = player_y - bullet_height

# Set the bullet speed
bullet_speed = 5

# Set the enemy speed
enemy_speed = 1

# Set the score to zero
score = 0

# Create a list of enemies and set their dimensions and position
enemies = []
enemy_width = 50
enemy_height = 50

for i in range(5):
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(50, 150)
    enemies.append([enemy_x, enemy_y])

# Set the clock for the game loop
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:
    # Handle events in the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player left or right with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += 5

    # Move the bullet up when space bar is pressed and reset when it goes off screen
    if bullet_y > -bullet_height:
        bullet_y -= bullet_speed
    else:
        bullet_x = player_x + (player_width / 2) - (bullet_width / 2)
        bullet_y = player_y - bullet_height

    # Move each enemy down and reset when it goes off screen or hits the bullet or player.
    for enemy in enemies:
        enemy[1] += enemy_speed

        if enemy[1] > screen_height:
            enemy[0] = random.randint(0, screen_width - enemy_width)
            enemy[1] = random.randint(50, 150)
            score -= 1

        if bullet_y < enemy[1] + enemy_height and \
                bullet_x + bullet_width > enemy[0] and \
                bullet_x < enemy[0] + enemy_width:
            enemy[0] = random.randint(0, screen_width - enemy_width)
            enemy[1] = random.randint(50, 150)
            score += 1

        if player_y < enemy[1] + enemy_height and \
                player_x + player_width > enemy[0] and \
                player_x < enemy[0] + enemy_width:
            running = False

    # Fill the background color of the screen with black.
    screen.fill(black)

    # Draw the player on the screen as a white rectangle.
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    # Draw each enemy on the screen as a white rectangle.
    for enemy in enemies:
        pygame.draw.rect(screen, white, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Draw the bullet on the screen as a white rectangle.
    pygame.draw.rect(screen, white, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Draw the score on the screen using a font object and set its position to top left corner of screen.

    # Draw the score on the screen using a font object and set its position to top left corner of screen.
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    # Update Pygame display surface.
    pygame.display.update()

    # Tick clock to control frame rate.
    clock.tick(60)

# Quit Pygame when game loop is exited.
pygame.quit()