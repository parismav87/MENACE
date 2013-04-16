import random
import itertools


class Game(object):

 	def __init__(self):
 		self.board = [] #board of the game
  		self.pos = [] # array of possible moves
  		self.mirrorlist = []
  		self.rotate90list = []
  		self.manyStates = list(itertools.product('ox-',repeat=9))

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

	def findmirrors(self):
		self.mirrorlist = []
		self.mirrorlist.append([self.board[6],self.board[7],self.board[8],self.board[3],self.board[4],self.board[5],self.board[0],self.board[1],self.board[2]])
		for i in range(0,6):
			self.mirrorlist.append(self.rotate90(self.mirrorlist[i]))
		return self.mirrorlist

	def rotate90(self,tempboard):
		self.rotate90list = [tempboard[2],tempboard[5],tempboard[8],tempboard[1],tempboard[4],tempboard[7],tempboard[0],tempboard[3],tempboard[6]]
		return self.rotate90list


	def show(self):
		print self.board[0],'|',self.board[1],'|',self.board[2]
		print '---------'
		print self.board[3],'|',self.board[4],'|',self.board[5]
		print '---------'
		print self.board[6],'|',self.board[7],'|',self.board[8]


class RandomPlayer():

	def randomChoice(self):
		random.seed()
		return random.randint(0,8)


class LearningPlayer(object):


	def __init__(self):
		self.states =[]
		self.possibleMoves =[]
		self.beads =[]

	def generateStates(self):
		fewStates =[]
		mirrorFound = False
		game = Game()
		for i in range(len(game.manyStates)):
			game.board  = game.manyStates[i]
			for j in range(len(game.manyStates)):
				if j==i:
					pass
				else :
					mirrors = game.findmirrors
					for k in range(len(mirrors)):
						if game.manyStates[j]==mirrors[k]:
							mirrorFound=True
			if mirrorFound:
				mirrorFound = False
			else :
				fewStates.append(manyStates[i])
		return fewStates





			



tictac = Game()
tictac.initializeBoard()
learningP = LearningPlayer()
mirrors = tictac.findmirrors()
print mirrors
#stateslow = learningP.generateStates()
#print stateslow

