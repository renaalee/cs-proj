# balls


import pygame

pygame.init()

window_size = [900, 600]
window_color = pygame.Color(255, 255, 255)
window = pygame.display.set_mode(window_size)

def ball(surface, ball_color, ball_pos, ball_radius):
  pygame.draw.circle(surface, ball_color, ball_pos, ball_radius)
    
    
while True:
  window.fill(window_color)
  b1 = ball(window, pygame.Color(255, 153, 153), (800, 250), 10) #1
  b2 = ball(window, pygame.Color(255, 153, 153), (800, 275), 10) #2
  b3 = ball(window, pygame.Color(255, 255, 153), (800, 300), 10) #2
  b4 = ball(window, pygame.Color(204, 255, 153), (800, 325), 10) #4
  b5 = ball(window, pygame.Color(153, 255, 153), (800, 350), 10) #5
  b6 = ball(window, pygame.Color(153, 255, 204), (780, 337), 10) #6
  b7 = ball(window, pygame.Color(153, 255, 255), (780, 312), 10) #7
  b8 = ball(window, pygame.Color(153, 204, 255), (780, 287), 10) #8
  b9 = ball(window, pygame.Color(153, 153, 255), (780, 262), 10) #9
  b10 = ball(window, pygame.Color(204, 153, 255), (760, 275), 10) #10
  b11 = ball(window, pygame.Color(255, 153, 255), (760, 300), 10) #11
  b12 = ball(window, pygame.Color(255, 153, 204), (760, 325), 10) #12
  b13 = ball(window, pygame.Color(255, 204, 229), (740, 312), 10) #13
  b14 = ball(window, pygame.Color(229, 204, 255), (740, 287), 10) #14
  b15 = ball(window, pygame.Color(204, 229, 255), (720, 300), 10) #15
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        pygame.quit()
  pygame.display.flip()