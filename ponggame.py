import pygame

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

# Set up the paddles
player_paddle = pygame.Rect(20, 250, 10, 100)
ai_paddle = pygame.Rect(770, 250, 10, 100)

# Set up the ball
ball = pygame.Rect(395, 295, 10, 10)
ball_speed_x = 5
ball_speed_y = 5

# Set up the score
player_score = 0
ai_score = 0

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles with the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.centery -= 5
    if keys[pygame.K_DOWN] and player_paddle.bottom < screen.get_height():
        player_paddle.centery += 5


    # Move the AI paddle towards the ball
    if ai_paddle.centery < ball.centery:
        ai_paddle.centery += 5
    elif ai_paddle.centery > ball.centery:
        ai_paddle.centery -= 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball off the top and bottom walls
    if ball.top <= 0 or ball.bottom >= screen.get_height():
        ball_speed_y *= -1

    # Bounce the ball off the paddles
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed_x *= -1

    # Score a point if the ball goes off the left or right side of the screen
    if ball.left <= 0:
        ai_score += 1
        ball.x = 395
        ball.y = 295
        ball_speed_x *= -1

    elif ball.right >= screen.get_width():
        player_score += 1
        ball.x = 395
        ball.y = 295
        ball_speed_x *= -1

    # Draw everything on the screen
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), player_paddle)
    pygame.draw.rect(screen, (0,0,0), ai_paddle)
    pygame.draw.ellipse(screen, (0,0,0), ball)
    score_text = font.render("Player: " + str(player_score) + "   AI: " + str(ai_score), True, (0,0,0))
    screen.blit(score_text,(300 - score_text.get_width() // 2 ,10))

    # Update the screen
    pygame.display.update()

    # Slow down gameplay by calling tick() on clock object at end of each iteration of game loop.
    clock.tick(55)