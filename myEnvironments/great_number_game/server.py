from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def startGame():
    session['randNumber'] = random.randrange(0, 101) # random number between 0-100
    return render_template('index.html', formatClass="hide_me", displayMsg="")

@app.route('/guessNumber', methods=['POST'])
def guessNumber():
    guess = int(request.form['guessed_number'])
    actual = int(session['randNumber'])
    print "DEBUG - Guessed:", str(guess)
    print "DEBUG - Actual:", str(actual)
    className = ""
    displayText = ""
    if guess < actual:
        className = "tooLow"
        displayText = "Too low!"
    elif guess > actual:
        className = "tooHigh"
        displayText = "Too high!"
    else:
        className = "correct"
        displayText = str(guess) + " was the number!"

    return render_template('index.html', formatClass=className, displayMsg=displayText)

app.run(debug=True)