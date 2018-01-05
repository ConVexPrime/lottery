var ballMachine = {
	balls: [],
	numBalls: 3,
	numBallsDrawn: 2,
	populateBalls: function(numBalls) {
		for (var i = 0; i < numBalls; i++) {
			this.balls.push(i+1);
		}
	},
	drawNumbers: function(numBallsDrawn) {
		var a = [];
		var b = [];
		for (var i = 0; i < numBallsDrawn; i++) {
			b = this.getRandomBall(this.balls);
			while (a.includes(b)) {
				b = this.getRandomBall(this.balls);
			}
		a.push(b);
		}
		a.sort();
		return a;
	},
	getRandomBall: function() {
    return Math.floor(Math.random()*(this.balls.length-1+1))+1;
	},
};

var lottoGame = {
	theWinners: [],
	playerNumbers: [],

	init: function() {
		ballMachine.balls = [];
		ballMachine.populateBalls(ballMachine.numBalls);
		theWinners = ballMachine.drawNumbers(ballMachine.numBallsDrawn);
		playerNumbers = ballMachine.drawNumbers(ballMachine.numBallsDrawn);
	},
	isWinner: function() {
		for (var i = 0; i < theWinners.length; i++) {
			if (theWinners[i] != playerNumbers[i]) {
				return false;
			}
		}
		return true;
	},
	displayStuff: function() {
		this.init();
		console.log(ballMachine.balls + '\n' + theWinners + ' -- ' + playerNumbers)
		if (this.isWinner()) {
			console.log('You won!');
		}	else {
			console.log('You lost');
		}
	}
};