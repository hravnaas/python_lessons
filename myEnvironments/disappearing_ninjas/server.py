from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "1234"

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/ninja')
def showNinjas():
	return render_template('ninja.html')

app.run(debug=True)
