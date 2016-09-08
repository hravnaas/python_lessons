from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def registerUser():
    session['hasErrors'] = False
    validateAllFields()
    print session['hasErrors']
    if session['hasErrors'] == False:
        flash("Thanks for submitting your information.")
    return redirect('/')

def validateAllFields():
    validateNotBlank()
    validateNames()
    validatePasswords()
    validateEmail()

def validateNotBlank():
    for key in request.form:
        if len(request.form[key]) < 1:
            flash(key + " is empty but is required.")
            session['hasErrors'] = True

def validateNames():
    if not request.form["First Name"].isalpha() or not request.form["Last Name"].isalpha():
        flash("Only alphamumeric characters are allowed for the first and last name.")
        session['hasErrors'] = True

def validatePasswords():
    MIN_PASSWORD = 8
    if len(request.form["Password"]) < MIN_PASSWORD:
        flash("The password must be at least " + str(MIN_PASSWORD) + " characters. Yours is only " + str(len(request.form["Password"])) + ".")
        session['hasErrors'] = True

    if len(request.form["Password"]) != len(request.form["Confirmed Password"]):
        flash("The password and confirmed password do not match.")
        session['hasErrors'] = True

def validateEmail():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(request.form["Email"]):
        flash("The email is invalid.")
        session['hasErrors'] = True

app.run(debug=True)