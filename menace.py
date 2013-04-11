import sys, os
import pygame
from pygame.locals import *



class Box(pygame.sprite.Sprite):
	def __init__(self,position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("circle.png")
		


position = [0,0]
box1 = Box()
box1.__init__(box1,position)

"""
Graphics
"""





pygame.init()


window = pygame.display.set_mode((600,600))
image = pygame.image.load("circle.png").convert()
window.blit(image,(0,0))
pygame.display.flip()


while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print event


"""
window = pygame.display.set_mode((600,600))

pygame.draw.line(window,(255,255,255),(0,200),(600,200))
pygame.draw.line(window,(255,255,255),(0,400),(600,400))
pygame.draw.line(window,(255,255,255),(200,0),(200,600))
pygame.draw.line(window,(255,255,255),(400,0),(400,600))

pygame.display.flip()

 



"""

"""
Menace

"""








