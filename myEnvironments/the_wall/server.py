from flask import Flask, render_template, request, redirect, flash, session
from flask.ext.bcrypt import Bcrypt
import datetime

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
	#pw_hash = bcrypt.generate_password_hash(password)
	#bcrypt.check_password_hash(pw_hash, test_password_1)
	# return render_template('login.html')
	session["userId"] = 1 # HACK
	result = getAllMessagesAndComments()
	return render_template('wall.html', userName="Hans", userId=session["userId"], messages=result[0], comments=result[1])

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

@app.route('/friends/<userId>/edit', methods=['POST'])
def editFriend(id):
	return render_template('edit.html', friend=getFriend(id))

# Get a specified friend from the database.
def getFriend(id):
	select_query = "SELECT id, first_name, last_name, occupation, created_at, updated_at FROM friends WHERE id = :id"
	data = {'id' : id}
	return mysql.query_db(select_query, data)

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

@app.route('/friends/<id>/delete', methods=['POST'])
def deleteFriend(id):
	removeFriend(id)
	return redirect('/')

# Delete friend with a given id
def removeFriend(id):
	delete_query = "DELETE FROM friends WHERE id = :id"
	data = {"id" : id}
	mysql.query_db(delete_query, data)

@app.route('/friends', methods=['POST'])
def addFriend():
	saveFriendToDb(request.form['first_name'], request.form['last_name'], request.form['occupation'])
	return redirect('/')

# Adds a new friedn to the database.
# It does not check if it already exists.
def saveFriendToDb(first_name, last_name, occupation):
	insert_query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
	data = {
				'first_name': first_name,
				'last_name' : last_name,
				'occupation' : occupation
			}

	return mysql.query_db(insert_query, data)

app.run(debug=True)