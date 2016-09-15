from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
	WORD_LENGTH = 14
	if not 'wordAttempt' in request.session:
		request.session['wordAttempt'] = 0

	request.session['wordAttempt'] += 1
	myWord = {'word' : generateWord(WORD_LENGTH)}
	return render(request, "random_word_generator/index.html", myWord)

# Generate a random word of the specified length.
def generateWord(length):
	word = ''
	for i in range(length):	
		asciiValue = random.randrange(33,127)
		word += chr(asciiValue)
	return word
