import pygame
import os
pygame.init()
screen = pygame.display.set_mode((540, 720))
clock = pygame.time.Clock()
running = True
background = pygame.image.load(os.path.join("images","background.jpg"))

screen.blit(background,(0,0))
#박스 생성
main_box = pygame.Rect(90,200,360,360)
pygame.draw.rect(screen,"white",main_box,0,10)
#줄 구분
pygame.draw.line(screen,"black",pygame.Vector2(90,320),pygame.Vector2(450,320),width=3)#가로 1
pygame.draw.line(screen,"black",pygame.Vector2(90,440),pygame.Vector2(450,440),width=3)#가로 2
pygame.draw.line(screen,"black",pygame.Vector2(210,200),pygame.Vector2(210,560),width=3)#세로 3
pygame.draw.line(screen,"black",pygame.Vector2(330,200),pygame.Vector2(330,560),width=3)#세로 4
button1 = pygame.Rect(95,205,110,110)
button2 = pygame.Rect(215,205,110,110)
button3 = pygame.Rect(335,205,110,110)
button4 = pygame.Rect(95,325,110,110)
button5 = pygame.Rect(215,325,110,110)
button6 = pygame.Rect(335,325,110,110)
button7 = pygame.Rect(95,445,110,110)
button8 = pygame.Rect(215,445,110,110)
button9 = pygame.Rect(335,445,110,110)
pygame.draw.rect(screen,"black",button1,0,10)
pygame.draw.rect(screen,"black",button2,0,10)
pygame.draw.rect(screen,"black",button3,0,10)
pygame.draw.rect(screen,"black",button4,0,10)
pygame.draw.rect(screen,"black",button5,0,10)
pygame.draw.rect(screen,"black",button6,0,10)
pygame.draw.rect(screen,"black",button7,0,10)
pygame.draw.rect(screen,"black",button8,0,10)
pygame.draw.rect(screen,"black",button9,0,10)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button1.collidepoint(event.pos):
                    pass # 클릭시 작업
    pygame.display.flip()
    clock.tick(60)

pygame.quit()