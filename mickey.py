import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800,800))

background = pygame.image.load(r"C:\Users\HUAWEI\Downloads\mainclock.png")
left_arm = pygame.image.load(r"C:\Users\HUAWEI\Downloads\leftarm.png")
right_arm = pygame.image.load(r"C:\Users\HUAWEI\Downloads\rightarm.png")
bg_rect = background.get_rect(center = (400, 400))


exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    current_time = datetime.now().time()  
    seconds_angle = -(current_time.second * 6)  
    minutes_angle = -(current_time.minute * 6)  

    rotated_leftarm = pygame.transform.rotate(left_arm, seconds_angle)  
    rotated_rightarm = pygame.transform.rotate(right_arm, minutes_angle)  

    leftarm_rect = rotated_leftarm.get_rect(center = bg_rect.center)  
    rightarm_rect = rotated_rightarm.get_rect(center = bg_rect.center)  

    screen.blit(background, bg_rect) 
    screen.blit(rotated_leftarm, leftarm_rect)  
    screen.blit(rotated_rightarm, rightarm_rect)  
    pygame.display.flip()  
    
