from lotto import Lotto

# Hoosier Lottery: ($2 per ticket) / 46 numbers (pick 6)
l = Lotto(4, 3)
while not l.isWinner():
	l.checkWinner()