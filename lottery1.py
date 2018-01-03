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

	def checkWinner(self):
		while not self.winner:
			theWinners = self.getLottoNumbers()
			qPick = self.getLottoNumbers()
			if theWinners == qPick:
				self.winner = True
				self.week += 1
				print('{} {} {}'.format(self.week, theWinners, qPick))
				print ('You won!')
			else:
				self.week += 1
				print('{} {} {}'.format(self.week, theWinners, qPick))

# Hoosier Lottery: ($2 per ticket) / 46 numbers (pick 6)
l = Lotto(46, 3)
l.checkWinner()