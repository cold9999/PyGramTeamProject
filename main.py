import pygame
import os
import random
pygame.init()
screen = pygame.display.set_mode((540, 720))
clock = pygame.time.Clock()
running = True
background = pygame.image.load(os.path.join("images","background.jpg"))
o_img = pygame.image.load(os.path.join("images","O.png"))
x_img = pygame.image.load(os.path.join("images","X.png"))
screen.blit(background,(0,0))
#게임 플레이 변수
#0이 지정 X, False가 컴터, True가 플레이어
pressed_list = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
button_sizes = {"1":(95,205),"2":(215,205),"3":(335,205),"4":(95,325),"5":(215,325),"6":(335,325),"7":(95,445),"8":(215,445),"9":(335,445)}
#박스 생성
button1 = pygame.Rect(95,205,110,110)
button2 = pygame.Rect(215,205,110,110)
button3 = pygame.Rect(335,205,110,110)
button4 = pygame.Rect(95,325,110,110)
button5 = pygame.Rect(215,325,110,110)
button6 = pygame.Rect(335,325,110,110)
button7 = pygame.Rect(95,445,110,110)
button8 = pygame.Rect(215,445,110,110)
button9 = pygame.Rect(335,445,110,110)
button_reset = pygame.Rect(50,50,60,60)
pygame.draw.rect(screen,"white",button_reset,0,10)
def reset():
    global pressed_list, turn_num
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
    pressed_list = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
def get_danger():
    print(list(pressed_list.items()))
    player_list = []
    for val in list(pressed_list.items()):
        if val[1] == True:
            player_list.append(val[0])
get_danger()
def com_play(arg:str):
    global turn_num
    if arg == "5":
        while True:
            ran_sel = random.choice(["2","4","6","8"])
            if pressed_list[ran_sel] == 0:
                screen.blit(x_img,button_sizes[ran_sel])
                pressed_list[ran_sel] = False
                break
            else:
                continue
    else:
        #앞에 위험 체크해야됨
        if pressed_list["5"] == 0:
            screen.blit(x_img,button_sizes["5"])
            pressed_list["5"] = False
        else:
            pass
reset()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button1.collidepoint(event.pos):
                    if pressed_list["1"] == 0:
                        screen.blit(o_img,button_sizes["1"])
                        pressed_list["1"] = True
                        com_play("1")
                if button2.collidepoint(event.pos):
                    if pressed_list["2"] == 0:
                        screen.blit(o_img,button_sizes["2"])
                        pressed_list["2"] = True
                        com_play("2")
                if button3.collidepoint(event.pos):
                    if pressed_list["3"] == 0:
                        screen.blit(o_img,button_sizes["3"])
                        pressed_list["3"] = True
                        com_play("3")
                if button4.collidepoint(event.pos):
                    if pressed_list["4"] == 0:
                        screen.blit(o_img,button_sizes["4"])
                        pressed_list["4"] = True
                        com_play("4")
                if button5.collidepoint(event.pos):
                    if pressed_list["5"] == 0:
                        screen.blit(o_img,button_sizes["5"])
                        pressed_list["5"] = True
                        com_play("5")
                if button6.collidepoint(event.pos):
                    if pressed_list["6"] == 0:
                        screen.blit(o_img,button_sizes["6"])
                        pressed_list["6"] = True
                        com_play("6")
                if button7.collidepoint(event.pos):
                    if pressed_list["7"] == 0:
                        screen.blit(o_img,button_sizes["7"])
                        pressed_list["7"] = True
                        com_play("7")
                if button8.collidepoint(event.pos):
                    if pressed_list["8"] == 0:
                        screen.blit(o_img,button_sizes["8"])
                        pressed_list["8"] = True
                        com_play("8")
                if button9.collidepoint(event.pos):
                    if pressed_list["9"] == 0:
                        screen.blit(o_img,button_sizes["9"])
                        pressed_list["9"] = True
                        com_play("9")
                if button_reset.collidepoint(event.pos):
                    reset()
                print(pressed_list)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()