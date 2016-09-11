from flask import Flask, render_template, request, redirect, flash, session
from flask.ext.bcrypt import Bcrypt
import datetime
import re

# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "supersecretlongkeyhere"
bcrypt = Bcrypt(app)

# Connect to "thewall" database
mysql = MySQLConnector(app, 'thewall')

# Default route. User is redirected here after successful login
@app.route('/')
def index():
	if "userId" not in session:
		# User is logged in and needs to register or log in
		return render_template('login.html')

	# User is already logged in. Go to the wall
	result = getAllMessagesAndComments()
	return render_template('wall.html', userName=session["firstName"], userId=session["userId"], messages=result[0], comments=result[1])

# Retrieves all messages and their comments from the database.
def getAllMessagesAndComments():
	# Get all the messages
	message_query = "SELECT m.id, m.created_at, m.message, concat_ws(' ', u.first_name, u.last_name) as full_name FROM messages AS m INNER JOIN users AS u ON u.id = m.user_id ORDER BY m.created_at DESC"
	messages = mysql.query_db(message_query)

	# Get all the comments
	comment_query = "SELECT c.message_id, c.comment, c.created_at, concat_ws(' ', u.first_name, u.last_name) as full_name FROM comments AS c INNER JOIN users AS u ON c.user_id = u.id ORDER BY message_id, created_at DESC"
	comments = mysql.query_db(comment_query)

	# Return messages and comments as separate items. That way
	# the caller can decide if it's neccessary to combine them.
	return [messages, comments]

@app.route('/wall/<userId>/post_message', methods=['POST'])
def postMessage(userId):
		postMessageToDb(userId, request.form['message'])
		return redirect('/')

# Writes a message from a user to the database
def postMessageToDb(userId, message):
	insert_query = "INSERT INTO messages (created_at, updated_at, user_id, message) VALUES (NOW(), NOW(), :userId, :message)"
	data = {
		"userId" : userId,
		"message" : message
	}

	mysql.query_db(insert_query, data)
	return redirect('/')

@app.route('/wall/<userId>/post_comment', methods=['POST'])
def postComment(userId):
		postCommentToDb(userId, request.form['message_id'], request.form['comment'])
		return redirect('/')

# Writes a comment for message to the database
def postCommentToDb(userId, message_id, comment):
	insert_query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :userId, :message_id)"
	data = {
		"comment" : comment,
		"userId" : userId,
		"message_id" : message_id
	}

	mysql.query_db(insert_query, data)
	return redirect('/')

@app.route('/wall/register', methods=['POST'])
def register():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	cpassword = request.form['cpassword']

	# Validate input fields
	session['hasValidationErrors'] = False
	validateAllFields()
	if session['hasValidationErrors']:
		return redirect('/')

    # All input fields look good. Save the user to the database.
	userId = addUserToDb(first_name, last_name, email, bcrypt.generate_password_hash(password))

	# The user was successfully registered.
	# Automatically do a login.
	login(userId)
	
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
    if not request.form["first_name"].isalpha() or not request.form["last_name"].isalpha():
        flash("Only alphamumeric characters are allowed for the first and last name.")
        session['hasValidationErrors'] = True

def validatePasswords():
    MIN_PASSWORD = 8
    if len(request.form["password"]) < MIN_PASSWORD:
        flash("The password must be at least " + str(MIN_PASSWORD) + " characters. Yours is only " + str(len(request.form["password"])) + ".")
        session['hasValidationErrors'] = True

    if len(request.form["password"]) != len(request.form["cpassword"]):
        flash("The password and confirmed password do not match.")
        session['hasValidationErrors'] = True

def validateEmail():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(request.form["email"]):
        flash("The email is invalid.")
        session['hasValidationErrors'] = True

# Adds a new user to the database and returns the user ID.
# It does not check if it already exists.
def addUserToDb(first_name, last_name, email, encrypted_password):
	insert_query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at, password) VALUES (:first_name, :last_name, :email, NOW(), NOW(), :password)"
	data = {
				'first_name': first_name,
				'last_name' : last_name,
				'email' : email,
				'password' : encrypted_password
			}

	return mysql.query_db(insert_query, data)

@app.route('/wall/login', methods=['POST', 'GET'])
def login(userId = -1):
	if "userId" not in session:
		if len(request.form) < 1:
			# User is not logged in and no info was posted. Force another login.
			return render_template('login.html')

		# Log the user in by grabbing the encrypted password from the database
		# and comparing it to the provided password after encrypting it.
		user = getUserByEmail(request.form["email"])[0]
		try:
			if not bcrypt.check_password_hash(user["password"], request.form['password']):
				flash("Incorrect user name or password")
				return render_template('login.html')
		except Exception, e:
			# Handle situation when the salt is bad, etc.
			flash("Unexpected error, please try again (" + e.message + ")")
			return render_template('login.html')

		# Credentials look good.
		session['userId'] = user["id"]
		session['firstName'] = user["first_name"]
	
	# User is (now) considered logged in. Go to the wall.
	result = getAllMessagesAndComments()
	return render_template('wall.html', userName=session["firstName"], userId=session["userId"], messages=result[0], comments=result[1])

# Get specified user from the database based on provided email.
def getUserByEmail(email):
	# TODO handle non-existent user
	select_query = "SELECT id, first_name, password FROM users WHERE email = :email LIMIT 1"
	data = {'email' : email}
	return mysql.query_db(select_query, data)

# Logs the user out and indirectly redirects to the login page
@app.route('/wall/<userId>/logout', methods=['POST'])
def logOut(userId):
	session.pop('userId')
	session.pop('firstName')
	return redirect('/')

app.run(debug=True)