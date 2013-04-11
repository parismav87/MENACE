import sys
import pygame



"""
Graphics

"""
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.draw.line(window,(255,255,255),(0,150),(1000,150))
pygame.draw.line(window,(255,255,255),(0,320),(1000,320))
pygame.draw.line(window,(255,255,255),(200,0),(200,1000))
pygame.draw.line(window,(255,255,255),(420,0),(420,1000))
pygame.display.flip()

while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print event 





"""
Menace

"""








