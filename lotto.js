var winner = false;
var week = 0;

var ballMachine = {
	balls: [],
	// Currently hardcoded variables, need some forms and shit.
	numBalls: 10,
	numBallsDrawn: 3,
	theWinners: [],
	populateBalls: function(numBalls) {
		for (var i = 0; i < numBalls; i++) {
			this.balls.push(i+1);
		}
	},
	drawNumbers: function(numBallsDrawn) {
		var a = [];
		var b = [];
		for (var i = 0; i < numBallsDrawn; i++) {
			b = this.getRandomBall(self.balls);
			while (a.includes(b)) {
				b = this.getRandomBall(self.balls);
			}
		a.push(b);
		}
		return a;
	},
	getRandomBall: function() {
    return Math.floor(Math.random()*(this.balls.length-1+1))+1;
	},
}

var lottoGame = {
	showBalls: function() {
		console.log(ballMachine.balls);
	},

	checkWinner: function() {
		// Function to check winning numbers against the players numbers
	},

	numbersDrawn: function() {
		// Function to get numbers drawn
	},

	playersNumbers: function() {
		// Function to get players numbers
	},
}

