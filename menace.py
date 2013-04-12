import sys, os
import pygame
from pygame.locals import *

#initialize pygame
pygame.init()
window = pygame.display.set_mode((600,600))
turn =0 

#box class
class Box(pygame.sprite.Sprite):
	def __init__(self,position):
		pygame.sprite.Sprite.__init__(self)
		self.images = [pygame.image.load("black.png").convert(),pygame.image.load("circle.png").convert(), pygame.image.load("cross.png").convert()]
		self.pos = position
		self.image = self.images[0]
		self.clicked = False
	def update(self,turn):
		if turn ==0:
			self.image = self.images[1] 
		else :
			self.image = self.images[2]
		window.blit(self.image,self.pos)
		pygame.display.flip()
		

#each box is a sprite (to click on)
box1 = Box((5,5))
box2 = Box((205,5))
box3 = Box((405,5))
box4 = Box((5,205))
box5 = Box((205,205))
box6 = Box((405,205))
box7 = Box((5,405))
box8 = Box((205,405))
box9 = Box((405,405))

allBoxes = [box1,box2,box3,box4,box5,box6,box7,box8,box9]

#initialize all boxes
for box in allBoxes :
	window.blit(box.image,box.pos)

#tic tac toe lines
pygame.draw.line(window,(255,255,255),(0,200),(600,200))
pygame.draw.line(window,(255,255,255),(0,400),(600,400))
pygame.draw.line(window,(255,255,255),(200,0),(200,600))
pygame.draw.line(window,(255,255,255),(400,0),(400,600))

#initialize display
pygame.display.flip()

#check events (click quit etc.)
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
      		for box in allBoxes:
      			box.clicked = False 	
        		sys.exit(0) 
      elif event.type ==pygame.MOUSEBUTTONDOWN:
      		mousex,mousey = pygame.mouse.get_pos()
      		if mousex<=200 and mousey<=200 and not box1.clicked:
          		box1.update(turn)
          		box1.clicked = True
          		turn = (turn+1)%2
          	elif mousex>200 and mousex <=400 and mousey <=200 and not box2.clicked:
          		box2.update(turn)
          		box2.clicked = True
          		turn = (turn+1)%2
          	elif mousex>400 and mousex <=600 and mousey <=200 and not box3.clicked:
          		box3.update(turn)
          		box3.clicked = True
          		turn = (turn+1)%2
          	elif mousey >200 and mousex <=200 and mousey <=400 and not box4.clicked:	
          		box4.update(turn)
          		box4.clicked = True
          		turn = (turn+1)%2
          	elif mousey >200 and mousex> 200 and mousex <=400 and mousey <= 400 and not box5.clicked:	
          		box5.update(turn)
          		box5.clicked = True
          		turn = (turn+1)%2
          	elif mousex>400 and mousey >200 and mousex <=600 and mousey <= 400 and not box6.clicked:	
          		box6.update(turn)
          		box6.clicked = True
          		turn = (turn+1)%2
          	elif mousey >400 and mousex <= 200 and mousey <= 600 and not box7.clicked:	
          		box7.update(turn)
          		box7.clicked = True
          		turn = (turn+1)%2
          	elif mousex>200 and mousey>400 and mousex<= 400 and mousey <= 600 and not box8.clicked:	
          		box8.update(turn)
          		box8.clicked = True
          		turn = (turn+1)%2
          	elif mousex>400 and mousey>400 and mousex <= 600 and mousey <= 600 and not box9.clicked:	
          		box9.update(turn)
          		box9.clicked = True
          		turn = (turn+1)%2













