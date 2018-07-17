#Combined Final Project
#Karin, Rena, & Emily

import pygame
import math
import time

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
  

table_dims = [110, 110, 990, 690]
ball_pos = [550, 400]
ball_vel = [0,0]
ball_radius = 10
ball_color = pygame.Color(127,127,255)

clock = pygame.time.Clock()

def update_control(surface_size, ball_pos, ball_vel, ball_radius):
    if ball_pos[0] + ball_radius >= table_dims[2] or ball_pos[0] - ball_radius <= table_dims[0]:
        ball_vel = [-ball_vel[0], ball_vel[1]]
    if ball_pos[1] + ball_radius >= table_dims[3] or ball_pos[1] - ball_radius <= table_dims[1]:
        ball_vel = [ball_vel[0], -ball_vel[1]]

    ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1]+ball_vel[1]]

    return ball_pos, ball_vel


def draw_control(surface, ball_color, ball_pos, ball_radius):
    pygame.draw.circle(surface, ball_color, ball_pos, ball_radius)
  

def brake_control(ball_vel):
    """brakes control ball"""
    if ball_vel == [0,0]:
        return ball_vel
    elif ball_vel[0]==0:
        if ball_vel[1] < 0:
            ball_vel = [ball_vel[0], ball_vel[1]+1]
        elif ball_vel[1] > 0:
            ball_vel = [ball_vel[0], ball_vel[1]-1]
    elif ball_vel[1]==0:
        if ball_vel[0] <0:
            ball_vel = [ball_vel[0]+1, ball_vel[1]]
        elif ball_vel[0]>0:
            ball_vel = [ball_vel[0]-1, ball_vel[1]]
    else:
        if ball_vel[0] > 0 and ball_vel[1] > 0:
            ball_vel = [ball_vel[0]-1, ball_vel[1]-1]
        if ball_vel[0] < 0 and ball_vel[1] < 0:
            ball_vel = [ball_vel[0]+1, ball_vel[1]+1]
        if ball_vel[0] > 0 and ball_vel[1] < 0:
            ball_vel = [ball_vel[0]-1, ball_vel[1]+1]
        if ball_vel[0] < 0 and ball_vel[1] > 0:
            ball_vel = [ball_vel[0]+1, ball_vel[1]-1]
    return ball_vel

def shoot_control(ball_vel):
    """shoots control ball"""
    if ball_vel == [0,0]:
        return ball_vel
    elif ball_vel[0]==0:
        if ball_vel[1] < 0:
            ball_vel = [ball_vel[0], ball_vel[1]-2]
        elif ball_vel[1] > 0:
            ball_vel = [ball_vel[0], ball_vel[1]+2]
    elif ball_vel[1]==0:
        if ball_vel[0] <0:
            ball_vel = [ball_vel[0]-2, ball_vel[1]]
        elif ball_vel[0]>0:
            ball_vel = [ball_vel[0]+2, ball_vel[1]]
    else:
        if ball_vel[0] > 0 and ball_vel[1] > 0:
            ball_vel = [ball_vel[0]+2, ball_vel[1]+2]
        if ball_vel[0] < 0 and ball_vel[1] < 0:
            ball_vel = [ball_vel[0]-2, ball_vel[1]-2]
        if ball_vel[0] > 0 and ball_vel[1] < 0:
            ball_vel = [ball_vel[0]+2, ball_vel[1]-2]
        if ball_vel[0] < 0 and ball_vel[1] > 0:
            ball_vel = [ball_vel[0]-2, ball_vel[1]+2]
    return ball_vel

def move_control(ball_vel):
    """Defines commands for moving control"""
    if event.key == pygame.K_UP:
        ball_vel = [ball_vel[0], ball_vel[1]-1]
    if event.key == pygame.K_DOWN:
        ball_vel = [ball_vel[0], ball_vel[1]+1]
    if event.key == pygame.K_RIGHT:
        ball_vel = [ball_vel[0]+1, ball_vel[1]]
    if event.key == pygame.K_LEFT:
        ball_vel = [ball_vel[0]-1, ball_vel[1]]
    if event.key == pygame.K_SPACE:
        ball_vel = shoot_control(ball_vel)
    if event.key == pygame.K_b:
        ball_vel = brake_control(ball_vel)
    return ball_vel


def ball(surface, ball_color, ball_pos, ball_radius):
    pygame.draw.circle(surface, ball_color, ball_pos, ball_radius)

b1_pos = [800, 350]
b2_pos = [800, 375]
b3_pos = [800, 400]
b4_pos = [800, 425]
b5_pos = [800, 450]
b6_pos = [780, 437]
b7_pos = [780, 412]
b8_pos = [780, 387]
b9_pos = [780, 362]
b10_pos = [760, 375]
b11_pos = [760, 400]
b12_pos = [760, 425]
b13_pos = [740, 412]
b14_pos = [740, 387]
b15_pos = [720, 400]

b1_vel = [0,0]
b2_vel = [0,0]
b3_vel = [0,0]
b4_vel = [0,0]
b5_vel = [0,0]
b6_vel = [0,0]
b7_vel = [0,0]
b8_vel = [0,0]
b9_vel = [0,0]
b10_vel = [0,0]
b11_vel = [0,0]
b12_vel = [0,0]
b13_vel = [0,0]
b14_vel = [0,0]
b15_vel = [0,0]

rad = 10

def creating_balls():
    b1 = ball(window, pygame.Color(255, 153, 153), b1_pos, 10) #1
    b2 = ball(window, pygame.Color(255, 153, 153), b2_pos, 10) #2
    b3 = ball(window, pygame.Color(255, 255, 153), b3_pos, 10) #2
    b4 = ball(window, pygame.Color(204, 255, 153), b4_pos, 10) #4
    b5 = ball(window, pygame.Color(153, 255, 153), b5_pos, 10) #5
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
    return b1, b2, b3, b4, b5, #b6, b7, b8, b9, b10, b11, b12, b13, b14, b15


def creating_balls():
    b1 = ball(window, pygame.Color(255, 153, 153), b1_pos, rad) #1
    b2 = ball(window, pygame.Color(255, 153, 153), b2_pos, rad) #2
    b3 = ball(window, pygame.Color(255, 255, 153), b3_pos, rad) #2
    b4 = ball(window, pygame.Color(204, 255, 153), b4_pos, rad) #4
    b5 = ball(window, pygame.Color(153, 255, 153), b5_pos, rad) #5
    #b6 = ball(window, pygame.Color(153, 255, 204), b6_pos, rad) #6
    #b7 = ball(window, pygame.Color(153, 255, 255), b7_pos, rad) #7
    #b8 = ball(window, pygame.Color(153, 204, 255), b8_pos, rad) #8
    #b9 = ball(window, pygame.Color(153, 153, 255), b9_pos, rad) #9
    #b10 = ball(window, pygame.Color(204, 153, 255), b10_pos, rad) #10
    #b11 = ball(window, pygame.Color(255, 153, 255), b11_pos, rad) #11
    #b12 = ball(window, pygame.Color(255, 153, 204), b12_pos, rad) #12
    #b13 = ball(window, pygame.Color(255, 204, 229), b13_pos, rad) #13
    #b14 = ball(window, pygame.Color(229, 204, 255), b14_pos, rad) #14
    #b15 = ball(window, pygame.Color(204, 229, 255), b15_pos, rad) #15
    return b1, b2, b3, b4, b5

def one_collision(a, b):
    """checks if there is a collision between two balls"""
    ans = math.hypot(a[0]-b[0], a[1]-b[1])
    if ans <= 20:
        print('COLLISION')      
        return True
    else:
        print('no collision')
        return False

def checking_collisions():
    """checks collisions between all objects
    takes no input, returns list of velocities of balls that have been involved in a collision"""
    
    C = []
    L = [ball_pos, b1_pos, b2_pos, b3_pos, b4_pos, b5_pos]

    for b in L[0:(len(L)-1)]:
        indexCount = 1
        bCount = 0
        for r in L[1:]:
            L = L[2:]
            check = one_collision(b, r)
            #print(check)
            if check == True:
                    C += [bCount] + [indexCount]
                    #print(C)
                    return C
            indexCount += 1
        bCount += 1

def update_balls():
    pass
          


def in_pocket(a):
    """Checks if a ball is in any of the 6 pockets. Returns a boolean. """  
    if a[0] <= 140 and a[1] <= 140:
        return True
    elif a[0] <= 560 and a[0] >= 540 and a[1] <= 135:
        return True
    elif a[0] >= 960 and a[1] <= 140:
        return True
    elif a[0] <= 140 and a[1] >= 660:
        return True
    elif a[0] >= 540 and a[0] <= 560 and a[1] >= 665:
        return True
    elif a[0] >= 960 and a[1] >= 660:
        return True
    else:
        return False

def all_pockets():
    """Takes a list of all the balls and checks to see if any are in a pocket.
    If they are in a pocket, excluding the control ball, they are removed from the list. """
    L = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
    b = [x for x in L if in_pocket(x) == False]

def timer():
    """Creates a timer that runs throughout the game. """
    clock = pygame.time.Clock()
    return clock


while True:
    window = pygame.display.set_mode(window_size)
    window.fill(window_color)
    table = draw_table()

    clock.tick(60)

    ball_pos, ball_vel = update_control(window_size, ball_pos, ball_vel, ball_radius)
    control = draw_control(window, ball_color, ball_pos, ball_radius)

    b1, b2, b3, b4, b5 = creating_balls()

    all_pockets()
    
    #one_collision(ball_pos, b1_pos)
    checking_collisions()
    timer()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ball_vel = move_control(ball_vel)        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    

    pygame.display.flip()
