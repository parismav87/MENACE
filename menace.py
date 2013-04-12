import sys, os
import pygame
from pygame.locals import *



class Box(pygame.sprite.Sprite):
	def __init__(self,position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("circle.png")
		self.pos = position
	def update(self):
		self.image= pygame.image.load("cross.png")
		window.blit(self.image,self.pos)
		pygame.display.flip()
		


box1 = Box((0,0))
box2 = Box((200,0))

"""
Graphics
"""





pygame.init()


window = pygame.display.set_mode((600,600))
image = box1.image
window.blit(image,box1.pos)
window.blit(box2.image,box2.pos)

pygame.draw.line(window,(255,255,255),(0,200),(600,200))
pygame.draw.line(window,(255,255,255),(0,400),(600,400))
pygame.draw.line(window,(255,255,255),(200,0),(200,600))
pygame.draw.line(window,(255,255,255),(400,0),(400,600))

pygame.display.flip()

 
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      elif event.type ==pygame.MOUSEBUTTONDOWN:
          	box1.update()
          	box2.update()





"""
Menace

"""








