import pygame
import os
pygame.init()
screen = pygame.display.set_mode((540, 720))
clock = pygame.time.Clock()
running = True
background = pygame.image.load(os.path.join("images","background.jpg"))
o_img = pygame.image.load(os.path.join("images","O.png"))
x_img = pygame.image.load(os.path.join("images","X.png"))
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
pygame.draw.rect(screen,"white",button1,0,10)
pygame.draw.rect(screen,"white",button2,0,10)
pygame.draw.rect(screen,"white",button3,0,10)
pygame.draw.rect(screen,"white",button4,0,10)
pygame.draw.rect(screen,"white",button5,0,10)
pygame.draw.rect(screen,"white",button6,0,10)
pygame.draw.rect(screen,"white",button7,0,10)
pygame.draw.rect(screen,"white",button8,0,10)
pygame.draw.rect(screen,"white",button9,0,10)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button1.collidepoint(event.pos):
                    screen.blit(o_img,(95,205))
                if button2.collidepoint(event.pos):
                    screen.blit(o_img,(215,205))
                if button3.collidepoint(event.pos):
                    screen.blit(o_img,(335,205))
                if button4.collidepoint(event.pos):
                    screen.blit(o_img,(95,325))
                if button5.collidepoint(event.pos):
                    screen.blit(o_img,(215,325))
                if button6.collidepoint(event.pos):
                    screen.blit(o_img,(335,325))
                if button7.collidepoint(event.pos):
                    screen.blit(o_img,(95,445))
                if button8.collidepoint(event.pos):
                    screen.blit(o_img,(215,445))
                if button9.collidepoint(event.pos):
                    screen.blit(o_img,(335,445))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()