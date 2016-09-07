from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def displayGreeting():
	return render_template('index.html')

@app.route('/ninjas')
def displayNinjaInfo():
	return render_template('ninjas.html')

@app.route('/dojos/new')
def doForm():
	return render_template('dojos.html')

app.run(debug=True)