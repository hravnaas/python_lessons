from django.shortcuts import render, redirect
from datetime import datetime
import random

# Default route
def index(request):
	request.session['gameScore'] = 0
	request.session['comments'] = []
	return render(request, "app_ninja_gold/index.html")

# /process_money'
def processMoney(request, building):
	# Only accept POSTS
	if not request or request.method != "POST":
		return redirect('/')

	#building = request.POST["building"] # Not needed when using route parameters
	currentScore = request.session['gameScore']
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
	# TODO: Fix line below to use local time and format the time.
	now = str(datetime.now())
	if newGold > 0:
		msg = "Earned " + str(newGold) + " golds from the " + building + "! (" + now + ")"
		styleClass="greenText"
	else:
		msg = "Entered a " + building + " and lost " + (str(newGold))[1:] + " golds... Ouch.. (" + now + ")"
		styleClass="redText"

	request.session["comments"].insert(0, {"class": styleClass, "message": msg})
	
	# Get the new score and return it
	request.session['gameScore'] = getNewScore(newGold, request)
	return render(request, 'app_ninja_gold/index.html')

def getRandNum(min, max):
	return random.randrange(min, max + 1)

def getNewScore(newGold, request):
	return int(request.session['gameScore']) + newGold
