import random

class Lotto:
	def __init__(self, numBalls, numBallsDrawn):
		self.numBalls = numBalls
		self.numBallsDrawn = numBallsDrawn
		self.winner = False
		self.balls = []
		self.week = 0

		for i in range(self.numBalls):
			self.balls.append(i+1)

	def getLottoNumbers(self):
		a = []
		for i in range(self.numBallsDrawn):
			b = random.choice(self.balls)
			while b in a:
				b = random.choice(self.balls)
			a.append(b)
			a.sort()
		return a

	def isWinner(self):
		if self.winner:
			return True
		else:
			return False

	def checkWinner(self):
		theWinners = self.getLottoNumbers()
		quickPick = self.getLottoNumbers()
		
		if theWinners == quickPick:
			self.winner = True
			self.week += 1
			# print('{} {} {} You won!'.format(self.week, theWinners, quickPick))
			return('You won! {} {} {}'.format(self.week, theWinners, quickPick))
		else:
			self.week += 1
			# print('{} {} {}'.format(self.week, theWinners, quickPick))
			return('Not a winner {} {} {}'.format(self.week, theWinners, quickPick))