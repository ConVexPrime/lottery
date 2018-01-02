# Hoosier Lottery: ($2 per ticket) / 46 numbers (pick 6) 
import random

NUM_RANGE = 10
NUM_OF_NUMBERS = 1
WINNER = False
BALLS = []
ATTEMPT = 0

HIGH_SCORE = 0
GUESSES_EACH_GAME = []
AVERAGE_GUESSES = 0
GAMES_TO_PLAY = 100000


for i in range(NUM_RANGE):
	BALLS.append(i+1)

def getRanNum():
	a = []
	for i in range(NUM_OF_NUMBERS):
		b = random.choice(BALLS)
		while b in a:
			b = random.choice(BALLS)
		a.append(b)
		a.sort()
	return a

j = 0
while j < GAMES_TO_PLAY:
	for i in range (0,100):
		winningNum = getRanNum()
		pick = getRanNum()
		if winningNum == pick:
			WINNER = True
			ATTEMPT += 1
			
			if ATTEMPT > HIGH_SCORE:
				HIGH_SCORE = ATTEMPT
			
			GUESSES_EACH_GAME.append(ATTEMPT)

			WINNER = False
			ATTEMPT = 0
			j += 1
		else:
			ATTEMPT += 1
print('\nHigh Score')
print(HIGH_SCORE)
print('Average Guesses Per Game')
print((sum(GUESSES_EACH_GAME) / len(GUESSES_EACH_GAME)))

