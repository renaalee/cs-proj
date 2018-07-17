#Combined Final Project
#Karin, Rena, & Emily

import pygame

pygame.init()

#Background code:
window_size = [1100, 800]
window_color = pygame.Color(255, 255, 255)
table_color = pygame.Color(214, 244, 255)
wood_color = pygame.Color(150, 150, 150)
pocket_color1 = pygame.Color(255, 0 ,0)
pocket_color2 = pygame.Color(255, 255, 255)

def draw_table():
   #Table
   pygame.draw.rect(window, table_color, [100, 100, 900, 600], 0) #draws the green of the table
  
   #Pocket 1, top left:
   pygame.draw.circle(window, pocket_color1, [120, 120], 20, 5)
   pygame.draw.circle(window, pocket_color2, [120, 120], 15, 5)
   pygame.draw.circle(window, pocket_color1, [120, 120], 10, 5)
   pygame.draw.circle(window, pocket_color2, [120, 120], 5, 5)

   #Pocket 2, top middle
   pygame.draw.circle(window, pocket_color1, [550, 115], 20, 5)
   pygame.draw.circle(window, pocket_color2, [550, 115], 15, 5)
   pygame.draw.circle(window, pocket_color1, [550, 115], 10, 5)
   pygame.draw.circle(window, pocket_color2, [550, 115], 5, 5)

   #Pocket 3, lower left
   pygame.draw.circle(window, pocket_color1, [120, 680], 20, 5)
   pygame.draw.circle(window, pocket_color2, [120, 680], 15, 5)
   pygame.draw.circle(window, pocket_color1, [120, 680], 10, 5)
   pygame.draw.circle(window, pocket_color2, [120, 680], 5, 5)

   # Pocket 4, top right
   pygame.draw.circle(window, pocket_color1, [980, 120], 20, 5)
   pygame.draw.circle(window, pocket_color2, [980, 120], 15, 5)
   pygame.draw.circle(window, pocket_color1, [980, 120], 10, 5)
   pygame.draw.circle(window, pocket_color2, [980, 120], 5, 5)

   # Pocket 5, lower middle
   pygame.draw.circle(window, pocket_color1, [550, 685], 20, 5)
   pygame.draw.circle(window, pocket_color2, [550, 685], 15, 5)
   pygame.draw.circle(window, pocket_color1, [550, 685], 10, 5)
   pygame.draw.circle(window, pocket_color2, [550, 685], 5, 5)

   # Pocket 6, lower right
   pygame.draw.circle(window, pocket_color1, [980, 680], 20, 5)
   pygame.draw.circle(window, pocket_color2, [980, 680], 15, 5)
   pygame.draw.circle(window, pocket_color1, [980, 680], 10, 5)
   pygame.draw.circle(window, pocket_color2, [980, 680], 5, 5)

   #Wooden border
   pygame.draw.rect(window, wood_color, [100, 100, 900, 600], 30) #draws the wooden edge of the table
  

table_dims = [115, 115, 985, 685]
ball_pos = (550, 400)
ball_vel = [0,0]
ball_radius = 10
ball_color = pygame.Color(127,127,255)

clock = pygame.time.Clock()

def update_control(surface_size, ball_pos, ball_vel, ball_radius):
    if ball_pos[0] + ball_radius >= table_dims[2] or ball_pos[0] - ball_radius <= table_dims[0]:
        ball_vel = (-ball_vel[0], ball_vel[1])
    if ball_pos[1] + ball_radius >= table_dims[3] or ball_pos[1] - ball_radius <= table_dims[1]:
        ball_vel = (ball_vel[0], -ball_vel[1])

    ball_pos = (ball_pos[0] + ball_vel[0], ball_pos[1]+ball_vel[1])

    return ball_pos, ball_vel

def draw_control(surface, ball_color, ball_pos, ball_radius):
    pygame.draw.circle(surface, ball_color, ball_pos, ball_radius)
  

def brake_control(ball_vel):
    """brakes control ball"""
    if ball_vel == (0,0):
        return
    elif ball_vel[0]==0:
        if ball_vel[1] < 0:
            ball_vel = (ball_vel[0], ball_vel[1]+1)
        elif ball_vel[1] > 0:
            ball_vel = (ball_vel[0], ball_vel[1]-1)
    elif ball_vel[1]==0:
        if ball_vel[0] <0:
            ball_vel = (ball_vel[0]+1, ball_vel[1])
        elif ball_vel[0]>0:
            ball_vel = (ball_vel[0]-1, ball_vel[1])
    else:
        if ball_vel[0] > 0 and ball_vel[1] > 0:
            ball_vel = (ball_vel[0]-1, ball_vel[1]-1)
        if ball_vel[0] < 0 and ball_vel[1] < 0:
            ball_vel = (ball_vel[0]+1, ball_vel[1]+1)
        if ball_vel[0] > 0 and ball_vel[1] < 0:
            ball_vel = (ball_vel[0]-1, ball_vel[1]+1)
        if ball_vel[0] < 0 and ball_vel[1] > 0:
            ball_vel = (ball_vel[0]+1, ball_vel[1]-1)
    return ball_vel

def shoot_control(ball_vel):
    """shoots control ball"""
    if ball_vel == (0,0):
        return ball_vel
    elif ball_vel[0]==0:
        if ball_vel[1] < 0:
            ball_vel = (ball_vel[0], ball_vel[1]-2)
        elif ball_vel[1] > 0:
            ball_vel = (ball_vel[0], ball_vel[1]+2)
    elif ball_vel[1]==0:
        if ball_vel[0] <0:
            ball_vel = (ball_vel[0]-2, ball_vel[1])
        elif ball_vel[0]>0:
            ball_vel = (ball_vel[0]+2, ball_vel[1])
    else:
        if ball_vel[0] > 0 and ball_vel[1] > 0:
            ball_vel = (ball_vel[0]+2, ball_vel[1]+2)
        if ball_vel[0] < 0 and ball_vel[1] < 0:
            ball_vel = (ball_vel[0]-2, ball_vel[1]-2)
        if ball_vel[0] > 0 and ball_vel[1] < 0:
            ball_vel = (ball_vel[0]+2, ball_vel[1]-2)
        if ball_vel[0] < 0 and ball_vel[1] > 0:
            ball_vel = (ball_vel[0]-2, ball_vel[1]+2)
    return ball_vel

def move_control(ball_vel):
    """Defines commands for moving control"""
    if event.key == pygame.K_UP:
        ball_vel = (ball_vel[0], ball_vel[1]-1)
    if event.key == pygame.K_DOWN:
        ball_vel = (ball_vel[0], ball_vel[1]+1)
    if event.key == pygame.K_RIGHT:
        ball_vel = (ball_vel[0]+1, ball_vel[1])
    if event.key == pygame.K_LEFT:
        ball_vel = (ball_vel[0]-1, ball_vel[1])
    if event.key == pygame.K_SPACE:
        ball_vel = shoot_control(ball_vel)
    if event.key == pygame.K_b:
        ball_vel = brake_control(ball_vel)
    return ball_vel


def ball(surface, ball_color, ball_pos, ball_radius):
    pygame.draw.circle(surface, ball_color, ball_pos, ball_radius)

def creating_balls():
    b1 = ball(window, pygame.Color(255, 153, 153), (800, 350), 10) #1
    b2 = ball(window, pygame.Color(255, 153, 153), (800, 375), 10) #2
    b3 = ball(window, pygame.Color(255, 255, 153), (800, 400), 10) #2
    b4 = ball(window, pygame.Color(204, 255, 153), (800, 425), 10) #4
    b5 = ball(window, pygame.Color(153, 255, 153), (800, 450), 10) #5
    b6 = ball(window, pygame.Color(153, 255, 204), (780, 437), 10) #6
    b7 = ball(window, pygame.Color(153, 255, 255), (780, 412), 10) #7
    b8 = ball(window, pygame.Color(153, 204, 255), (780, 387), 10) #8
    b9 = ball(window, pygame.Color(153, 153, 255), (780, 362), 10) #9
    b10 = ball(window, pygame.Color(204, 153, 255), (760, 375), 10) #10
    b11 = ball(window, pygame.Color(255, 153, 255), (760, 400), 10) #11
    b12 = ball(window, pygame.Color(255, 153, 204), (760, 425), 10) #12
    b13 = ball(window, pygame.Color(255, 204, 229), (740, 412), 10) #13
    b14 = ball(window, pygame.Color(229, 204, 255), (740, 387), 10) #14
    b15 = ball(window, pygame.Color(204, 229, 255), (720, 400), 10) #15

def in_pocket(ball_pos):  
    if ball_pos[0] <= 140 and ball_pos[1] <= 140:
        print("Goal!")
    elif ball_pos[0] >= 560 and ball_pos[0] <= 580 and ball_pos[1] <= 135:
        print("Goal!")
    elif ball_pos[0] >= 980 and ball_pos [1] <= 120:
        print("Goal!")
    elif ball_pos[0] <= 140 and ball_pos[1] >= 660:
        print("Goal!")
    elif ball_pos[0] >= 540 and ball_pos[0] <= 560 and ball_pos[1] >= 665:
        print("Goal!")
    elif ball_pos[0] >= 960 and ball_pos[1] >= 660:
        print("Goal!")

while True:
    window = pygame.display.set_mode(window_size)
    window.fill(window_color)
    table = draw_table()

    clock.tick(60)

    ball_pos, ball_vel = update_control(window_size, ball_pos, ball_vel, ball_radius)
    draw_control(window, ball_color, ball_pos, ball_radius)

    creating_balls()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ball_vel = move_control(ball_vel)        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    

    pygame.display.flip()
