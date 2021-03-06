#Combined Final Project
#Karin, Rena, & Emily

import pygame
import math
import time
import random

pygame.init()

#Background code:
window_size = [1100, 800]
window_color = pygame.Color(255, 255, 255)
table_color = pygame.Color(222, 231, 247)
wood_color = pygame.Color(150, 150, 150)
pocket_color1 = pygame.Color(255, 0 ,0)
pocket_color2 = pygame.Color(255, 255, 255)

# +++++++++++++++++++++++++++++ TABLE SETUP ++++++++++++++++++++++++++++++

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
ball_radius = 12
ball_color = pygame.Color(127,127,255)
clock = pygame.time.Clock()

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
    elif a[1] == 750:
        return True
    else:
        return False

def all_pockets():
    """Takes a list of all the balls and checks to see if any are in a pocket.
    If they are in a pocket, excluding the control ball, they are removed from the list. 
    Returns a list of all the balls left on the table. """
    global b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    L = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
    #b = [x for x in L if in_pocket(x) == False]

    w = []
    for b in range(len(L)):
        if in_pocket(L[b]) == False:
            w += [b]
    #print(w)
    return w

# ++++++++++++++++++++++++++ CONTROL BALL STUFF ++++++++++++++++++++++++++++

def update_control():#ball_pos, ball_vel, ball_radius):
    global ball_pos, ball_vel, ball_radius, table_dims

    if ball_pos[0] + ball_radius >= table_dims[2] or ball_pos[0] - ball_radius <= table_dims[0]:
        ball_vel = [-ball_vel[0], ball_vel[1]]
    if ball_pos[1] + ball_radius >= table_dims[3] or ball_pos[1] - ball_radius <= table_dims[1]:
        ball_vel = [ball_vel[0], -ball_vel[1]]

    if len(all_pockets()) == 0:
        ball_pos = [ball_pos[0], ball_pos[1]]
    if len(all_pockets()) != 0:
        ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1]+ball_vel[1]]

    #return ball_pos, ball_vel


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

# ++++++++++++++++++++++ CHEAT FUNCTION +++++++++++++++++++++++++++

def auto_win():
    global b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    """Pressing the w key will automatically win the game; meant for testing. """
    if event.key == pygame.K_w:
        b1_pos = [130, 130]
        b2_pos = [130, 130]
        b3_pos = [130, 130]
        b4_pos = [130, 130]
        b5_pos = [130, 130]
        b6_pos = [130, 670]
        b7_pos = [130, 670]
        b8_pos = [130, 670]
        b9_pos = [130, 670]
        b10_pos = [130, 670]
        b11_pos = [970, 130]
        b12_pos = [970, 130]
        b13_pos = [970, 130]
        b14_pos = [970, 130]
        b15_pos = [970, 130]
    #return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o

# ++++++++++++++++++++++++++ GAME BALLS ++++++++++++++++++++++++++

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
    b1 = ball(window, pygame.Color(255, 153, 153), b1_pos, rad) #1
    b2 = ball(window, pygame.Color(255, 195, 90), b2_pos, rad) #2
    b3 = ball(window, pygame.Color(255, 255, 0), b3_pos, rad) #2
    b4 = ball(window, pygame.Color(178, 255, 102), b4_pos, rad) #4
    b5 = ball(window, pygame.Color(153, 255, 153), b5_pos, rad) #5
    b6 = ball(window, pygame.Color(153, 255, 204), b6_pos, rad) #6
    b7 = ball(window, pygame.Color(153, 255, 255), b7_pos, rad) #7
    b8 = ball(window, pygame.Color(153, 204, 255), b8_pos, rad) #8
    b9 = ball(window, pygame.Color(153, 153, 255), b9_pos, rad) #9
    b10 = ball(window, pygame.Color(204, 153, 255), b10_pos, rad) #10
    b11 = ball(window, pygame.Color(255, 153, 255), b11_pos, rad) #11
    b12 = ball(window, pygame.Color(255, 153, 204), b12_pos, rad) #12
    b13 = ball(window, pygame.Color(255, 204, 229), b13_pos, rad) #13
    b14 = ball(window, pygame.Color(229, 204, 255), b14_pos, rad) #14
    b15 = ball(window, pygame.Color(204, 204, 255), b15_pos, rad) #15,  (178, 229, 255)
    
    return b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15

# ++++++++++++++++++++++ COLLISIONS & REACTIONS +++++++++++++++++++++++++++

def one_collision(a, b):
    """checks if there is a collision between two balls"""
    ans = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
    if ans <= 20:
        #print('COLLISION')      
        return True
    else:
        #print('no collision')
        return False

def checking_collisions():
    """checks collisions between all objects
    takes no input, returns list of indices of balls that have been involved in a collision"""
    
    C = []
    L = [ball_pos, b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]

    for b in range(len(L)):
        for r in range(len(L)):
            if b == r:
                continue
            #print(b, ' , ', r)
            check = one_collision(L[b], L[r])
            #print(check)
            if check == True:
                C += [b] + [r]
                #print(C)
    return C

def update_all():
    global ball_pos, ball_vel, b1_pos, b1_vel, b2_pos, b2_vel, b3_pos, b3_vel, b4_pos, b4_vel, b5_pos, b5_vel, b6_pos, b6_vel, b7_pos, b7_vel, b8_pos, b8_vel, b9_pos, b9_vel, b10_pos, b10_vel, b11_pos, b11_vel, b12_pos, b12_vel, b13_pos, b13_vel, b14_pos, b14_vel, b15_pos, b15_vel

    lst = checking_collisions()
    #print('collisions:', lst)
    for x in lst:
        if x == 0:
            #print(x, 'collided')
            ball_pos, ball_vel = stopc(ball_pos, ball_vel)
        elif x == 1:
           # print(x, 'collided')
            b1_pos, b1_vel = rxn1(b1_pos, b1_vel)
        elif x==2:
           # print(x, 'collided')
            b2_pos, b2_vel = rxn2(b2_pos, b2_vel)
        elif x == 3:
           # print(x, 'collided')
            b3_pos, b3_vel = rxn3(b3_pos, b3_vel)
        elif x ==4:
            #print(x, 'collided')
            b4_pos, b4_vel = rxn4(b4_pos, b4_vel)
        elif x==5:               
           # print(x, 'collided')
            b5_pos, b5_vel = rxn5(b5_pos, b5_vel)
        elif x == 6:
            b6_pos, b6_vel = rxn6(b6_pos, b6_vel)
        elif x == 7:
            b7_pos, b7_vel = rxn7(b7_pos, b7_vel)
        elif x == 8:
            b8_pos, b8_vel = rxn8(b8_pos, b8_vel)
        elif x == 9:
            b9_pos, b9_vel = rxn9(b9_pos, b9_vel)
        elif x == 10:
            b10_pos, b10_vel = rxn10(b10_pos, b10_vel)
        elif x == 11:
            b11_pos, b11_vel = rxn11(b11_pos, b11_vel)
        elif x == 12:
            b12_pos, b12_vel = rxn12(b12_pos, b12_vel)
        elif x == 13:
            b13_pos, b13_vel = rxn13(b13_pos, b13_vel)
        elif x == 14:
            b14_pos, b14_vel = rxn14(b14_pos, b14_vel)
        elif x == 15:
            b15_pos, b15_vel = rxn15(b15_pos, b15_vel)

def stopc(ball_pos, ball_vel):
    ball_vel = [0,0]
    ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1]]
    return ball_pos, ball_vel

def rxn1(b1_pos, b1_vel):
    b1_vel = [1, 1]
    b1_pos = [b1_pos[0] + b1_vel[0], b1_pos[1] + b1_vel[1]]
    return b1_pos, b1_vel

def rxn2(b2_pos, b2_vel):
    b2_vel = [2, 2]
    b2_pos = [b2_pos[0] + b2_vel[0], b2_pos[1] + b2_vel[1]]
    return b2_pos, b2_vel

def rxn3(b3_pos, b3_vel):
    b3_vel = [1, -1]
    b3_pos = [b3_pos[0] + b3_vel[0], b3_pos[1] + b3_vel[1]]
    return b3_pos, b3_vel

def rxn4(b4_pos, b4_vel):
    b4_vel = [2, -2]
    b4_pos = [b4_pos[0] + b4_vel[0], b4_pos[1] + b4_vel[1]]
    return b4_pos, b4_vel

def rxn5(b5_pos, b5_vel):
    b5_vel = [1, 2]
    b5_pos = [b5_pos[0] + b5_vel[0], b5_pos[1] + b5_vel[1]]
    return b5_pos, b5_vel

def rxn6(b6_pos, b6_vel):
    b6_vel = [-1, -1]
    b6_pos = [b6_pos[0] + b6_vel[0], b6_pos[1] + b6_vel[1]]
    return b6_pos, b6_vel

def rxn7(b7_pos, b7_vel):
    b7_vel = [-1, 1]
    b7_pos = [b7_pos[0] + b7_vel[0], b7_pos[1] + b7_vel[1]]
    return b7_pos, b7_vel

def rxn8(b8_pos, b8_vel):
    b8_vel = [-2, -1]
    b8_pos = [b8_pos[0] + b8_vel[0], b8_pos[1] + b8_vel[1]]
    return b8_pos, b8_vel

def rxn9(b9_pos, b9_vel):
    b9_vel = [2, -1]
    b9_pos = [b9_pos[0] + b9_vel[0], b9_pos[1] + b9_vel[1]]
    return b9_pos, b9_vel
    
def rxn10(b10_pos, b10_vel):
    b10_vel = [1, -2]
    b10_pos = [b10_pos[0] + b10_vel[0], b10_pos[1] + b10_vel[1]]
    return b10_pos, b10_vel

def rxn11(b11_pos, b11_vel):
    b11_vel = [-1, -2]
    b11_pos = [b11_pos[0] + b11_vel[0], b11_pos[1] + b11_vel[1]]
    return b11_pos, b11_vel

def rxn12(b12_pos, b12_vel):
    b12_vel = [1, 3]
    b12_pos = [b12_pos[0] + b12_vel[0], b12_pos[1] + b12_vel[1]]
    return b12_pos, b12_vel

def rxn13(b13_pos, b13_vel):
    b13_vel = [-2, 2]
    b13_pos = [b13_pos[0] + b13_vel[0], b13_pos[1] + b13_vel[1]]
    return b13_pos, b13_vel

def rxn14(b14_pos, b14_vel):
    b14_vel = [3, 1]
    b14_pos = [b14_pos[0] + b14_vel[0], b14_pos[1] + b14_vel[1]]
    return b14_pos, b14_vel

def rxn15(b15_pos, b15_vel):
    b15_vel = [1, -3]
    b15_pos = [b15_pos[0] + b15_vel[0], b15_pos[1] + b15_vel[1]]
    return b15_pos, b15_vel

# ++++++++++++++++++++++ BOUNCE OFF BOUNDARY ++++++++++++++++++++++++++++++

def bound_and_roll():
    global b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_pos, b6_vel, b7_pos, b7_vel, b8_pos, b8_vel, b9_pos, b9_vel, b10_pos, b10_vel, b11_pos, b11_vel, b12_pos, b12_vel, b13_pos, b13_vel, b14_pos, b14_vel, b15_pos, b15_vel
    P = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
    V = [b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel]

    w = all_pockets()
    for x in w:
        if P[x][0] + rad >= table_dims[2]: 
            P[x] = [table_dims[2]-10, P[x][1]]
            V[x] = [-V[x][0], V[x][1]]
        if P[x][0] - rad <= table_dims[0]:
            P[x] = [table_dims[0]+10, P[x][1]]
            V[x] = [-V[x][0], V[x][1]]
        if P[x][1] + rad >= table_dims[3]:
            P[x] = [P[x][0], table_dims[3]-10]
            V[x] = [V[x][0], - V[x][1]]
        if P[x][1] - rad <= table_dims[1]:
            P[x] = [P[x][0], table_dims[1]+10]
            V[x] = [V[x][0], - V[x][1]]
    
    for x in range(len(P)):
        P[x] = [P[x][0] + V[x][0], P[x][1] + V[x][1]]
        #print(V[x][0], V[x][1])

    b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos = P[0], P[1], P[2], P[3], P[4], P[5], P[6], P[7], P[8], P[9], P[10], P[11], P[12], P[13], P[14]
    b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel = V[0], V[1], V[2], V[3], V[4], V[5], V[6], V[7], V[8], V[9], V[10], V[11], V[12], V[13], V[14]

def off_table():
    """Takes the balls that have been scored and places them somewhere off the table. """
    global b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    global b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel
    L = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
    g = [x for x in L if in_pocket(x) == True]
    for x in g:
        if b1_pos == x:
            b1_pos = [130, 750]
            b1_vel = [0, 0]
        if b2_pos == x:
            b2_pos = [190, 750]
            b2_vel = [0, 0]
        if b3_pos == x:
            b3_pos = [250, 750]
            b3_vel = [0, 0]
        if b4_pos == x:
            b4_pos = [310, 750]
            b4_vel = [0, 0]
        if b5_pos == x:
            b5_pos = [370, 750]
            b5_vel = [0, 0]
        if b6_pos == x:
            b6_pos = [430, 750]
            b6_vel = [0, 0]
        if b7_pos == x:
            b7_pos = [490, 750]
            b7_vel = [0, 0]
        if b8_pos == x:
            b8_pos = [550, 750]
            b8_vel = [0, 0]
        if b9_pos == x:
            b9_pos = [610, 750]
            b9_vel = [0, 0]
        if b10_pos == x:
            b10_pos = [670, 750]
            b10_vel = [0, 0]
        if b11_pos == x:
            b11_pos = [730, 750]
            b11_vel = [0, 0]
        if b12_pos == x:
            b12_pos = [790, 750]
            b12_vel = [0, 0]
        if b13_pos == x:
            b13_pos = [850, 750]
            b13_vel = [0, 0]
        if b14_pos == x:
            b14_pos = [910, 750]
            b14_vel = [0, 0]
        if b15_pos == x:
            b15_pos = [970, 750]
            b15_vel = [0, 0]

# ++++++++++++++++++++++++++++ SCORING +++++++++++++++++++++++++++++++

def timer(add_time, end_time):
    """Creates a timer that runs throughout the game. Should also add time when the control ball is in a pocket. """
    m = len(all_pockets())
    frame_count = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    frame_rate = 1000
    if m != 0:
        #Frame count
        total_seconds  = frame_count // frame_rate + add_time - end_sec

        if in_pocket(ball_pos) == True:
            add_time += 1

        seconds = total_seconds % 60
        minutes = total_seconds // 60
    
        output_string = "Timer: {0:02}:{1:02}".format(minutes, seconds)
        text = font.render(output_string, True, [0, 0, 0])
        window.blit(text, [300, 50])

        end_time = output_string
    
    else:
        #make the timer freeze at the time it was at when all the balls were collected
        #print("Display?")
        text = font.render(end_time, True, [0, 0, 0])
        window.blit(text, [300, 50])
    
    return add_time, end_time
    
def score():
    """Displays the number of balls left to get in the pockets. """
    font = pygame.font.Font(None, 30)
    left = len(all_pockets())
    output_string = "Left To Go: {0:02}".format(left)
    text = font.render(output_string, True, [0, 0, 0])
    window.blit(text, [700, 50])

# +++++++++++++++++++++++++++++ SLOW BALLS DOWN ++++++++++++++++++++++++++

collsec = 0
def stopballs():
    global collsec, b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel
    V = [b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel]
    collcheck = checking_collisions()
    
    frame_count = pygame.time.get_ticks()
    frame_rate = 1000
    totsec = frame_count  // frame_rate

    if collcheck != []:
        collsec = frame_count  // frame_rate
        #print('collsec')
    
    elif totsec - collsec == 2:
        for x in range(len(V)):
            if V[x][0] > 0 and V[x][1] > 0:
                V[x] = [V[x][0]-1,V[x][1]-1]
            elif V[x][0] > 0 and V[x][1] < 0:
                V[x] = [V[x][0]-1,V[x][1]+1]
            elif V[x][0] < 0 and V[x][1] > 0:
                V[x] = [V[x][0]+1,V[x][1]-1]
            elif V[x][0] < 0 and V[x][1] < 0:
                V[x] = [V[x][0]+1,V[x][1]+1]
    elif totsec - collsec == 3:
        for x in range(len(V)):
            V[x] = [0,0]

    b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel = V[0], V[1], V[2], V[3], V[4], V[5], V[6], V[7], V[8], V[9], V[10], V[11], V[12], V[13], V[14]
    bound_and_roll()

def play_question():
    """Asks the user if they want to play again. """
    #user = input("Play again? [y/n]")
    font = pygame.font.Font(None, 30)
    text = font.render('Play again?', True, [244, 66, 104])
    text2 = font.render('R to restart, Q to quit.', True, [244, 66, 104])
    window.blit(text, [490, 500])
    window.blit(text2, [450, 530])


# +++++++++++++++++++++++++++ FIREWORK CODE ++++++++++++++++++++++++++++++

class Pellet(object):
    """flying pellets from explosion"""

    def __init__(self, radius, xposx, yposy, xvelx, yvely, color):
        self.radius = radius
        self.xposx = xposx
        self.yposy = yposy
        self.xvelx = xvelx
        self.yvely = yvely 
        self.color = color
    
    def create_pellets(self):
        """creates exploding pellets at point of height"""
        pygame.draw.circle(window, self.color, [self.xposx, self.yposy], self.radius)

    def move(self):
        """guides motion"""
        self.yposy = self.yposy + self.yvely
        self.xposx = self.xposx + self.xvelx
        #print('this is them all moving')

    def explode(self):
        self.create_pellets()
        #print(self.xposx, self.yposy)
        self.move()
        #print(self.xposx, self.yposy)

class Firework(object):

    def __init__(self, radius, height, posx, posy, velx, vely, color, P):
        self.radius = radius
        self.height = height
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely 
        self.color = color
        self.P = P


    def create_base(self):
        """creates base at bottom with positions x, and y"""
        pygame.draw.circle(window, self.color, [self.posx, self.posy], self.radius)


    def roll_and_stop(self):
        """ rolls up and stops at given height"""
        #global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12
        
        if self.posy <= self.height:
            #print('im at height')
            self.velx = 0
            self.vely = 0
            X = self.posx
            Y = self.posy

            #print('this is', X,Y)
            
            if self.P == []:
                D = [[2,0], [0,2], [-2,0], [0,-2], [1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
                #print(P)
                for p in range(12):
                    self.P.append(Pellet(self.radius, X, Y, D[p][0], D[p][1],self.color))
    
            return explosion(self.P)
            #explosion(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12) #why doesn't this work??? they form but don't move
            #print('they have exploded')
           
        self.posy = self.posy - self.vely
        self.posx = self.posx 
        #print('roll pls')

def explosion(P):
    for p in P:
        p.explode()


def generate_fireworks():
    rad = random.randint(1,8)
    height = random.randint(100, 700)
    posx = random.randint(100, 1000)
    vely = random.randint(1,3)
    color = random.choice([(255,153,153), (255,204,153), (255,255,153), (178,255,102), (153,255,204), (153,255,255), (153,204,255), (153,153,255), (204,153,255), (255,153,255), (255,204,229), (229,204,255), (178,229,255)])

    d = Firework(rad, height, posx, 780, 0, vely, color, [])
    return d

def generate_list_fireworks():
    A = []
    for x in range(15):
        a = generate_fireworks()
        A += [a]
    return A

def text_conclusion(text, font):
    textSurface = font.render(text, True, [244, 66,104])
    return textSurface, textSurface.get_rect()

A = generate_list_fireworks()
def cue_fireworks():
    if len(all_pockets()) == 0:
        tfont = pygame.font.Font(None, 50)
        TextSurf, TextRect = text_conclusion('YOU WIN!', tfont)
        TextRect.center = (550, 400)
        window.blit(TextSurf, TextRect)
        play_question()
        
        for d in A:
            d.create_base()
            d.roll_and_stop()

#END FIREWORK CODE

# +++++++++++++++++++++++++++++++++ INTRO SCREEN ++++++++++++++++++++++

def text_objects(text, font):
    textSurface = font.render(text, True, [255,255,255])
    return textSurface, textSurface.get_rect()

beg_sec = 0
end_sec = 0
def intro():
    global beg_sec, end_sec
    window = pygame.display.set_mode(window_size)
    while True:
        frame_count = pygame.time.get_ticks()
        frame_rate = 1000
        beg_sec = frame_count // frame_rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        window.fill([255, 204, 229])
        bfont = pygame.font.Font(None, 100)
        lfont = pygame.font.Font(None, 40)
        TextSurf, TextRect = text_objects('ABSURDIST POOL', bfont)
        TextSurf2, TextRect2 = text_objects('Use ARROW KEYS to control ball.', lfont)
        TextSurf3, TextRect3 = text_objects('SPACE shoots ball. B brakes.', lfont)
        TextSurf4, TextRect4 = text_objects('Press SPACE to begin!', lfont)
        TextRect.center = (550, 300)
        TextRect2.center = (550, 400)
        TextRect3.center = (550, 450)
        TextRect4.center = (550, 550)
        window.blit(TextSurf, TextRect)
        window.blit(TextSurf2, TextRect2)
        window.blit(TextSurf3, TextRect3)
        window.blit(TextSurf4, TextRect4)
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                end_sec = frame_count // frame_rate
                break

L = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
end_time = 0
add_time = 0  


def play_again():
    global ball_pos, b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    global ball_vel, b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel
    global collsec, add_time
    if event.key == pygame.K_r:
        clock = pygame.time.Clock()
        whileCount = 0
        collsec = 0
        totsec = 0
        beg_sec = 0
        end_sec = 0 
        end_time = 0
        add_time = 0
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
        ball_pos = [550, 400]
        ball_vel = [0,0]

        for d in range(len(A)):
            A[d] = generate_fireworks()

        #print(b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel)
        main()





# +++++++++++++++++++++ BEGIN WHILE LOOP AND MAIN FUNCTION ++++++++++++++++++++++


def main():
    global window, window_color, window_size, ball_color, ball_radius, ball_pos, b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    global ball_vel, b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel
    global add_time, end_time, control, event
    whileCount = 0
    while True:

        if whileCount == 0:
            intro()

        window = pygame.display.set_mode(window_size)
        window.fill(window_color)
        table = draw_table()  

        clock.tick(60)    #sets frame rate for speed control
        add_time, end_time = timer(add_time, end_time)
        score()

        update_control()
        control = draw_control(window, ball_color, ball_pos, ball_radius)
                
        creating_balls()
        bound_and_roll()

        all_pockets()
        off_table()
                

        update_all() #checks for collisions and dictates reactions
        stopballs()

        cue_fireworks()

        whileCount += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                ball_vel = move_control(ball_vel)        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                auto_win()
            if event.type == pygame.KEYDOWN:
                play_again()
        pygame.display.flip()



main()

#changes?