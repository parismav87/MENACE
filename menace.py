import sys, os, random
import pygame
from pygame.locals import *

#initialize pygame
pygame.init()
window = pygame.display.set_mode((600,600))
turn =0 

#box class
class Box(pygame.sprite.Sprite):
	def __init__(self,position,id):
		pygame.sprite.Sprite.__init__(self)
		self.images = [pygame.image.load("black.png").convert(),pygame.image.load("circle.png").convert(), pygame.image.load("cross.png").convert()]
		self.pos = position
		self.image = self.images[0]
		self.clicked = False #if clicked already in the game.
		self.id = id
	def update(self,turn):
		if turn ==0:
			self.image = self.images[1] 
		else :
			self.image = self.images[2]
		window.blit(self.image,self.pos)
		pygame.display.flip()
	def isClicked(self,x,y):#checks if mouseclick was inside a box
		if x>= self.pos[0] and x<= self.pos[0]+190 and y>= self.pos[1] and y<= self.pos[1]+190:
			return True
		else: 
			return False





class Game(object):

	def _init_(self):
		pass

	board = [] #board of the game
	pos = [] # array of possible moves

	def initializeBoard(self):
		self.board = [0,1,2,3,4,5,6,7,8]

	def checkLine(self,char,spot1,spot2,spot3):
		if self.board[spot1]==char and self.board[spot2]==char and self.board[spot3]==char:
			return True


	def checkAll(self,char):
		if self.checkLine(char,0,1,2):
			return True
		if self.checkLine(char,3,4,5):
			return True
		if self.checkLine(char,6,7,8):
			return True
		if self.checkLine(char,0,3,6):
			return True
		if self.checkLine(char,1,4,7):
			return True
		if self.checkLine(char,2,5,8):
			return True
		if self.checkLine(char,0,4,8):
			return True
		if self.checkLine(char,2,4,6):
			return True

	def getValidMoves(self):
		for i in range(0,8):
			if self.board[i] != 'o' and self.board[i] != 'x':
				self.pos.append(i)
		return self.pos 

	def show(self):
		print self.board[0],'|',self.board[1],'|',self.board[2]
		print '---------'
		print self.board[3],'|',self.board[4],'|',self.board[5]
		print '---------'
		print self.board[6],'|',self.board[7],'|',self.board[8]

	def reset(self):
		self.initializeBoard()
		for box in allBoxes:
			box.image = box.images[0]
			window.blit(box.image,box.pos)
			pygame.display.flip()

			


class Player():

	def _init_(self):
		pass

	boxes = []

	def randomChoice(self):
		random.seed()
		return random.randint(0,8)

	def learningChoice(self):
		pass









#each box is a sprite (to click on)
box1 = Box((5,5),0)
box2 = Box((205,5),1)
box3 = Box((405,5),2)
box4 = Box((5,205),3)
box5 = Box((205,205),4)
box6 = Box((405,205),5)
box7 = Box((5,405),6)
box8 = Box((205,405),7)
box9 = Box((405,405),8)

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



#initialize game
tictac = Game()
tictac.initializeBoard()

randomP = Player()
learningP = Player()



#check events (click quit etc.)
while True: 
	 for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				for box in allBoxes:
					box.clicked = False 	
					sys.exit(0) 
			elif event.type ==pygame.MOUSEBUTTONDOWN:
				mousex,mousey = pygame.mouse.get_pos()
				for box in allBoxes:
					if box.isClicked(mousex,mousey) and box.clicked is False:
						box.update(turn)
						turn = (turn+1)%2
						box.clicked = True
						if turn==0:
							tictac.board[box.id] = 'o'
						else:
							tictac.board[box.id] = 'x'
				if tictac.checkAll('o') or tictac.checkAll('x'):
					tictac.reset()
					













