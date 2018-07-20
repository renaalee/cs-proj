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

def update_control():#ball_pos, ball_vel, ball_radius):
    global ball_pos, ball_vel, ball_radius, table_dims

    if ball_pos[0] + ball_radius >= table_dims[2] or ball_pos[0] - ball_radius <= table_dims[0]:
        ball_vel = [-ball_vel[0], ball_vel[1]]
    if ball_pos[1] + ball_radius >= table_dims[3] or ball_pos[1] - ball_radius <= table_dims[1]:
        ball_vel = [ball_vel[0], -ball_vel[1]]

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
    ans = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
    if ans <= 20:
        #print('COLLISION')      
        return True
    else:
        #print('no collision')
        return False

def checking_collisions():
    """checks collisions between all objects
    takes no input, returns list of velocities of balls that have been involved in a collision"""
    
    C = []
    L = [ball_pos, b1_pos, b2_pos, b3_pos, b4_pos, b5_pos]

    #bCount = 0
    for b in range(len(L)):
        #indexCount = 1
        for r in range(len(L)):
            if b == r:
                continue
            #print(b, ' , ', r)
            check = one_collision(L[b], L[r])

            #print(check)
            if check == True:
                C += [b] + [r]
                #print(C)
            #indexCount += 1           
        #bCount += 1

    return C


def bound_and_roll():
    global b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos, b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel
    P = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
    V = [b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel]

    for x in range(5):
        #print(type(P[0]))
        #print(type(table_dims[2]))
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
    
    for x in range(5):
        P[x] = [P[x][0] + V[x][0], P[x][1] + V[x][1]]

    b1_pos, b2_pos, b3_pos, b4_pos, b5_pos = P[0], P[1], P[2], P[3], P[4]
    b1_vel, b2_vel, b3_vel, b4_vel, b5_vel = V[0], V[1], V[2], V[3], V[4]



def update_all():
    global ball_pos, ball_vel, b1_pos, b1_vel, b2_pos, b2_vel, b3_pos, b3_vel, b4_pos, b4_vel, b5_pos, b5_vel

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

    #print(ball_pos, ball_vel, b1_pos, b1_vel, b2_pos, b2_vel, b3_pos, b3_vel, b4_pos, b4_vel, b5_pos, b5_vel)


def stopc(ball_pos, ball_vel):
    ball_vel = [0,0]
    ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1]]
    return ball_pos, ball_vel

def rxn1(b1_pos, b1_vel):
    b1_vel = [b1_vel[0]+1, b1_vel[1]+1]
    b1_pos = [b1_pos[0] + b1_vel[0], b1_pos[1] + b1_vel[1]]
    return b1_pos, b1_vel

def rxn2(b2_pos, b2_vel):
    b2_vel = [b2_vel[0]+2,b2_vel[1]+2]
    b2_pos = [b2_pos[0] + b2_vel[0], b2_pos[1] + b2_vel[1]]
    return b2_pos, b2_vel

def rxn3(b3_pos, b3_vel):
    b3_vel = [b3_vel[0]+1, b3_vel[1]]
    b3_pos = [b3_pos[0] + b3_vel[0], b3_pos[1] + b3_vel[1]]
    return b3_pos, b3_vel

def rxn4(b4_pos, b4_vel):
    b4_vel = [b4_vel[0]+2, b4_vel[1]]
    b4_pos = [b4_pos[0] + b4_vel[0], b4_pos[1] + b4_vel[1]]
    return b4_pos, b4_vel

def rxn5(b5_pos, b5_vel):
    b5_vel = [b5_vel[0], b5_vel[1]+2]
    b5_pos = [b5_pos[0] + b5_vel[0], b5_pos[1] + b5_vel[1]]
    return b5_pos, b5_vel

#def rxn6(b6_pos, b6_vel):
#    b6_vel = 
#    b6_pos = 
#    return b6_pos, b6_vel

#def rxn7(b7_pos, b7_vel):
#    b7_vel = 
#    b7_pos = 
#    return b7_pos, b7_vel

#def rxn8(b8_pos, b8_vel):
#    b8_vel = 
#    b8_pos = 
#    return b8_pos, b8_vel

#def rxn9(b9_pos, b9_vel):
#    b9_vel = 
#    b9_pos = 
#    return b9_pos, b9_vel
    
#def rxn10(b10_pos, b10_vel):
#    b10_vel = 
#    b10_pos = 
#    return b10_pos, b10_vel

#def rxn11(b11_pos, b11_vel):
#    b11_vel = 
#    b11_pos = 
#    return b11_pos, b11_vel

#def rxn12(b12_pos, b12_vel):
#    b12_vel = 
#    b12_pos = 
#    return b12_pos, b12_vel

#def rxn13(b13_pos, b13_vel):
#    b13_vel = 
#    b13_pos = 
#    return b13_pos, b13_vel

#def rxn14(b14_pos, b14_vel):
#    b14_vel = 
#    b14_pos = 
#    return b14_pos, b14_vel

#def rxn15(b15_pos, b15_vel):
#    b15_vel = 
#    b15_pos = 
#    return b15_pos, b15_vel

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
    If they are in a pocket, excluding the control ball, they are removed from the list. """
    global b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    L = b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    b = [x for x in L if in_pocket(x) == False]
    return b

def off_table():
    """Takes the balls that have been scored and places them somewhere off the table. """
    global b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos
    global b1_vel, b2_vel, b3_vel, b4_vel, b5_vel, b6_vel, b7_vel, b8_vel, b9_vel, b10_vel, b11_vel, b12_vel, b13_vel, b14_vel, b15_vel
    L = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
    g = [x for x in L if in_pocket(x) == True]
    for x in g:
        if b1_pos == x:
            b1_pos = [100, 750]
            b1_vel = [0, 0]
        if b2_pos == x:
            print("Off table!")
            b2_pos = [160, 750]
            print("Where?")
            b2_vel = [0, 0]
            print("Here!")
        if b3_pos == x:
            b3_pos = [220, 750]
            b3_vel = [0, 0]
        if b4_pos == x:
            b4_pos = [280, 750]
            b4_vel = [0, 0]
        if b5_pos == x:
            b5_pos = [340, 750]
            b5_vel = [0, 0]
        if b6_pos == x:
            b6_pos = [400, 750]
            b6_vel = [0, 0]
        if b7_pos == x:
            b7_pos = [460, 750]
            b7_vel = [0, 0]
        if b8_pos == x:
            b8_pos = [520, 750]
            b8_vel = [0, 0]
        if b9_pos == x:
            b9_pos = [580, 750]
            b9_vel = [0, 0]
        if b10_pos == x:
            b10_pos = [640, 750]
            b10_vel = [0, 0]
        if b11_pos == x:
            b11_pos = [700, 750]
            b11_vel = [0, 0]
        if b12_pos == x:
            b12_pos = [760, 750]
            b12_vel = [0, 0]
        if b13_pos == x:
            b13_pos = [820, 750]
            b13_vel = [0, 0]
        if b14_pos == x:
            b14_pos = [880, 750]
            b14_vel = [0, 0]
        if b15_pos == x:
            b15_pos = [940, 750]
            b15_vel = [0, 0]

def timer(add_time):
    """Creates a timer that runs throughout the game. Should also add 30 seconds when the control ball is in a pocket. """
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    frame_count = pygame.time.get_ticks()
    frame_rate = 1000
    total_seconds  = frame_count // frame_rate + add_time

    if in_pocket(ball_pos) == True:
        add_time += 1

    seconds = total_seconds % 60
    minutes = total_seconds // 60
    
    output_string = "Timer: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, [0, 0, 0])
    window.blit(text, [300, 50])
    
    return add_time
    

def score():
    """Displays the number of balls left to get in the pockets. """
    font = pygame.font.Font(None, 30)
    left = len(all_pockets())
    output_string = "Left To Go: {0:02}".format(left)
    text = font.render(output_string, True, [0, 0, 0])
    window.blit(text, [700, 50])


collsec = 0
def stopballs():
    global collsec, b1_vel, b2_vel, b3_vel, b4_vel, b5_vel
    V = [b1_vel, b2_vel, b3_vel, b4_vel, b5_vel]
    
    collcheck = checking_collisions()
    
    frame_count = pygame.time.get_ticks()
    frame_rate = 1000
    totsec = frame_count  // frame_rate

    if collcheck != []:
        collsec = frame_count  // frame_rate
        #print('collsec')
    
    elif totsec - collsec == 3:
        for x in range(len(V)):
            V[x] = [0,0]

    b1_vel, b2_vel, b3_vel, b4_vel, b5_vel = V[0], V[1], V[2], V[3], V[4]
    #print('all have stopped')
    bound_and_roll()
    #print('updating')
    #update_all()


L = [b1_pos, b2_pos, b3_pos, b4_pos, b5_pos, b6_pos, b7_pos, b8_pos, b9_pos, b10_pos, b11_pos, b12_pos, b13_pos, b14_pos, b15_pos]
add_time = 0        #Variables that need to exist outside of the while loop
while True:
    window = pygame.display.set_mode(window_size)
    window.fill(window_color)
    table = draw_table()

    clock.tick(60)
    add_time = timer(add_time)
    score()

    #ball_pos, ball_vel = 
    update_control()#ball_pos, ball_vel, ball_radius)
    control = draw_control(window, ball_color, ball_pos, ball_radius)
    
    creating_balls()
    bound_and_roll()

    all_pockets()
    off_table()
    
    #one_collision(ball_pos, b1_pos)
    #checking_collisions()

    #if one_collision(b5_pos, b4_pos)==True:
        #print('COLLISIONCOLLISIONCOLLISIONCOLLISIONCOLLISIONCOLLISIONCOLLISIONCOLLISION')

    update_all() #checks for collisions and dictates reactions
    #stopballs()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ball_vel = move_control(ball_vel)        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    

    pygame.display.flip()
#changeeeEEee