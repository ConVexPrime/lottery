from flask import Flask, render_template
from lotto import Lotto

app = Flask(__name__)

@app.route('/')
def index():
	l = Lotto(4, 3)
	
	theWinner = l.checkWinner()
	
	return render_template('index.html', theWinner=theWinner)
