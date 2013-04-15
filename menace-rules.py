import random



class Game(object):

 	def __init__(self):
 		self.board = [] #board of the game
  		self.pos = [] # array of possible moves
  		self.mirrorlist = []
  		self.rotate90list = []

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
		self.mirrorlist = [self.board]
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
		self.boxes = []

	def learningChoice(self,Game):
		Game.mirrorlist = Game.findmirrors()
		turn = 0
		for i in Game.mirrorlist:
			if str(i) in Game.mirrorlist:
				break
			turn = turn+1
		return turn



	def givebeads(tempboard2):
		options = tempboard2.count(" ")
		beadslist = []
		for i in xrange(len(tempboard2)):
			if tempboard2[i] == " ":
				entry = tempboard2[:]
				entry[i] = "x"
				beadslist.append([entry,options])
		return beadslist



tictac = Game()
tictac.initializeBoard()

randomP = RandomPlayer()
learningP = LearningPlayer()

# tictac.show()
while True:
	


	while True:
		randomA = randomP.randomChoice()
		if tictac.board[randomA] != 'o' and tictac.board[randomA] != 'x':
			tictac.board[randomA] = 'o'
			tictac.show()
			print tictac.findmirrors()
			# print tictac.getValidMoves()
			print learningP.learningChoice(tictac)
			del tictac.pos[:]
			break;
			
	#check for winner
	if tictac.checkAll('o')==True:
		break;

