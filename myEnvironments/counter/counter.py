from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def countOnMe():
    session['counter'] = int(session['counter']) + 1
    return render_template('index.html')

@app.route('/plustwo')
def plusTwo():
    session['counter'] = int(session['counter']) + 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)