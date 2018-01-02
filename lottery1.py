# Hoosier Lottery: ($2 per ticket) / 46 numbers (pick 6) 
import random

NUM_BALLS = 46
NUM_BALLS_DRAWN = 6
WINNER = False
BALLS = []
week = 0	

for i in range(NUM_BALLS):
	BALLS.append(i+1)

def getLottoNums():
	a = []
	for i in range(NUM_BALLS_DRAWN):
		b = random.choice(BALLS)
		while b in a:
			b = random.choice(BALLS)
		a.append(b)
		a.sort()
	return a

while not WINNER:
	theWinners = getLottoNums()
	qPick = getLottoNums()
	if theWinners == qPick:
		WINNER = True
		week += 1
		print('{} {} {}'.format(week, theWinners, qPick))
		print ('You won!')
	else:
		week += 1
		print('{} / {} / {}'.format(week, theWinners, qPick))
