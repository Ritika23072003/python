import pygame
import random
import time
from tkinter import *
pygame.init()
# colors
green = (255, 0, 0)
blue = (0, 0, 255)
red = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My First Game Ever')
pygame.display.update()
font = pygame.font.SysFont(None, 55)
def score(text, color, x, y):
    scroce = font.render(text, True, color)
    win.blit(scroce, (x, y))
def speeds(text, color, x, y):
    speed=font.render(text, True, color)
    win.blit(speed, (x, y))
clock = pygame.time.Clock()
def game():
    exitgame = False
    gameover = False
    snake_x = 140
    snake_y = 120
    snake_size = 20
    snake_vilocity_x = 0
    snake_vilocity_y = 0
    snake_list = []
    snake_length = 0
    food_x = random.randint(100, 500)
    food_y = random.randint(100, 500)

    cheat=False
    c = 0
    vx = 2
    vy = 2
    d = 10
    e = 0
    while not exitgame:
        win.fill(white)
        if gameover:
            win.fill(black)
            score('Game Over!',green,200,300)
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    exitgame = True
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_RETURN:
                        game()
        else:
            if e%10==0 and e!=0 and not(type(d)==type('max')) :
                e+=1
                if d==40:
                    d='max'
                else:
                    d+=10
                vx+=2
                vy+=2
##            if d==20:
##                for i in range(10,0,-1):
##                    score('Time:'+str(i),black,450,0)
##                    time.sleep(0.2)
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    exitgame = True
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_SPACE:
                        a = Tk()
                        Button(a, text='resume', command=a.destroy).grid()
                        a.mainloop()
                    if i.key==pygame.K_z:
                        cheat=True
                    if i.key==pygame.K_x:
                        cheat=False
                    if snake_vilocity_x>0 and vx!=0:
                        if i.key == pygame.K_RIGHT:
                            snake_vilocity_x = vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_UP:
                            snake_vilocity_y = -vy
                            snake_vilocity_x = 0
                        elif i.key == pygame.K_DOWN:
                            snake_vilocity_y = vy
                            snake_vilocity_x = 0
                    elif snake_vilocity_x<0 and vx!=0:
                        if i.key == pygame.K_LEFT:
                            snake_vilocity_x = -vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_UP:
                            snake_vilocity_y = -vy
                            snake_vilocity_x = 0
                        elif i.key == pygame.K_DOWN:
                            snake_vilocity_y = vy
                            snake_vilocity_x = 0
                    elif snake_vilocity_y>0 and vy!=0:
                        if i.key == pygame.K_RIGHT:
                            snake_vilocity_x = vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_LEFT:
                            snake_vilocity_x = -vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_DOWN:
                            snake_vilocity_y = vy
                            snake_vilocity_x = 0
                    elif snake_vilocity_y<0 and vy!=0:
                        if i.key == pygame.K_RIGHT:
                            snake_vilocity_x = vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_LEFT:
                            snake_vilocity_x = -vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_UP:
                            snake_vilocity_y = -vy
                            snake_vilocity_x = 0
                    else:
                        if i.key == pygame.K_RIGHT:
                            snake_vilocity_x = vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_LEFT:
                            snake_vilocity_x = -vx
                            snake_vilocity_y = 0
                        elif i.key == pygame.K_UP:
                            snake_vilocity_y = -vy
                            snake_vilocity_x = 0
                        elif i.key == pygame.K_DOWN:
                            snake_vilocity_y = vy
                            snake_vilocity_x = 0
            if abs(food_x-snake_x)<10 and abs(food_y-snake_y)<10:
                c+=1
                snake_length += 2
                if c%10!=0:
                    e+=1
                food_x = random.randint(100, 500)
                food_y = random.randint(100, 500)
            if abs(snake_y-600)<vx:
                snake_y=70
            elif abs(snake_y-70)<vx:
                snake_y=600
            elif abs(snake_x-800)<vx:
                snake_x=0
            elif abs(snake_x)<vx:
                snake_x=800

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            snake_x+=snake_vilocity_x
            snake_y+=snake_vilocity_y
            score('score :' + str(c * 10), black, 10, 0)
            speeds('speed :'+str(d),black,250,0)
            if head in snake_list[:-1] and not cheat:
                gameover=True
            for s_x,s_y in snake_list:
                pygame.draw.circle(win,black,[s_x,s_y],snake_size//2+1)
            pygame.draw.circle(win, blue, [snake_x, snake_y],snake_size//2+2)
            if len(snake_list)>= snake_length:
                del snake_list[0]
            pygame.draw.rect(win, red, [food_x, food_y , snake_size-2, snake_size-2])
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
game()
