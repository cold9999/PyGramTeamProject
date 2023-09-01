import pygame
import os
pygame.init()
screen = pygame.display.set_mode((540, 720))
clock = pygame.time.Clock()
running = True
background = pygame.image.load(os.path.join("images","background.jpg"))
#box_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
class button():
    def __init__(self,width,height,x,y,action):
        pass
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    #박스 생성
    main_box = pygame.Rect(90,200,360,360)
    pygame.draw.rect(screen,"white",main_box,0,10)
    #줄 구분
    pygame.draw.line(screen,"black",pygame.Vector2(90,320),pygame.Vector2(450,320),width=3)#가로 1
    pygame.draw.line(screen,"black",pygame.Vector2(90,440),pygame.Vector2(450,440),width=3)#가로 2
    pygame.draw.line(screen,"black",pygame.Vector2(210,200),pygame.Vector2(210,560),width=3)#세로 3
    pygame.draw.line(screen,"black",pygame.Vector2(330,200),pygame.Vector2(330,560),width=3)#세로 4

    pygame.display.flip()   
    
    clock.tick(60)

pygame.quit()