from flask import request, flash, session
import re

# TODO: Pass names of form fields in as parameters.
def validateAllFields():
    validateNotBlank()
    validateNames()
    validatePasswords()
    validateEmail()

def validateNotBlank():
    for key in request.form:
        if len(request.form[key]) < 1:
            flash(key + " is empty but is required.")
            session['hasValidationErrors'] = True

def validateNames():
    if not request.form["First Name"].isalpha() or not request.form["Last Name"].isalpha():
        flash("Only alphamumeric characters are allowed for the first and last name.")
        session['hasValidationErrors'] = True

def validatePasswords():
    MIN_PASSWORD = 8
    if len(request.form["Password"]) < MIN_PASSWORD:
        flash("The password must be at least " + str(MIN_PASSWORD) + " characters. Yours is only " + str(len(request.form["Password"])) + ".")
        session['hasValidationErrors'] = True

    if len(request.form["Password"]) != len(request.form["Confirmed Password"]):
        flash("The password and confirmed password do not match.")
        session['hasValidationErrors'] = True

def validateEmail():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(request.form["Email"]):
        flash("The email is invalid.")
        session['hasValidationErrors'] = True