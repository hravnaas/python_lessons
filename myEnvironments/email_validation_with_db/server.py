from flask import Flask, render_template, request, redirect, flash
import re

# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "1234"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/verifyEmail', methods=['POST'])
def verifyEmail():
	email = request.form["email"]
	hasErrors = False
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
	if not EMAIL_REGEX.match(email):
		hasErrors = True
		flash("Email is not valid!")

	if hasErrors:
		return redirect('/')

	saveEmailToDb(email)
	allEmails = getAllEmails()
	print allEmails

	return render_template("success.html", validatedEmail=email, currentEmails=allEmails)

# Saves an email address from the user to the database.
# It does not check if it already exists.
def saveEmailToDb(email):
	insert_query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW())"
	data = {'email_address': email}
	mysql.query_db(insert_query, data)

# Retrieves all emails from the database.
def getAllEmails():
	select_query = "SELECT email_address, created_at FROM emails"
	return mysql.query_db(select_query)

app.run(debug=True)