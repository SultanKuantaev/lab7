import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600  
BALL_RADIUS = 25  
BALL_SPEED = 20  
BALL_COLOR = (255, 0, 0)  
BG_COLOR = (255, 255, 255)  


screen = pygame.display.set_mode((WIDTH, HEIGHT))


ball_pos = [WIDTH // 2, HEIGHT // 2]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_pos[1] - BALL_SPEED > BALL_RADIUS:
        ball_pos[1] -= BALL_SPEED
    if keys[pygame.K_DOWN] and ball_pos[1] + BALL_SPEED < HEIGHT - BALL_RADIUS:
        ball_pos[1] += BALL_SPEED
    if keys[pygame.K_LEFT] and ball_pos[0] - BALL_SPEED > BALL_RADIUS:
        ball_pos[0] -= BALL_SPEED
    if keys[pygame.K_RIGHT] and ball_pos[0] + BALL_SPEED < WIDTH - BALL_RADIUS:
        ball_pos[0] += BALL_SPEED

    
    screen.fill(BG_COLOR)

    
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, BALL_RADIUS)

    
    pygame.display.flip()
