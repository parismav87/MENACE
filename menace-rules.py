import random



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


class Player():

	def _init_(self):
		pass

	boxes = []

	def randomChoice(self):
		random.seed()
		return random.randint(0,8)

	def learningChoice(self):
		pass





tictac = Game()
tictac.initializeBoard()

randomP = Player()
learningP = Player()

# tictac.show()
while True:
	



	while True:
		randomA = randomP.randomChoice()
		if tictac.board[randomA] != 'o' and tictac.board[randomA] != 'x':
			tictac.board[randomA] = 'o'
			tictac.show()
			print tictac.getValidMoves()
			del tictac.pos[:]
			break;
			
	#check for winner
	if tictac.checkAll('o')==True:
		break;


