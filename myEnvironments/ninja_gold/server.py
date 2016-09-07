from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def startGame():
    session['gameScore'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def processMoney():
	building = request.form["building"]
	currentScore = session['gameScore']
	newGold = 0

	if building == "farm":
		newGold = getRandNum(10, 20)
	elif building == "cave":
		newGold = getRandNum(5, 10)
	elif building == "house":
		newGold = getRandNum(2, 5)
	elif building == "casino":
		newGold = getRandNum(0, 50)
		# Determine if user should gain or lose gold
		if getRandNum(0,1) == 0:
			newGold = 0 - newGold
	else:
		# Ignore unknown building types
		pass

	# Construct the message to send back to the activities window
	msg = ""
	now = str(datetime.now())
	if newGold > 0:
		msg = "Earned " + str(newGold) + " golds from the " + building + "! (" + now + ")"
		styleClass="greenText"
	else:
		msg = "Entered a " + building + " and lost " + (str(newGold))[1:] + " golds... Ouch.. (" + now + ")"
		styleClass="redText"

	# Get the new score and return it
	session['gameScore'] = getNewScore(newGold)
	return render_template('index.html', message=msg, colorClass=styleClass)

def getRandNum(min, max):
	return random.randrange(min, max + 1)

def getNewScore(newGold):
	return int(session['gameScore']) + newGold

app.run(debug=True)