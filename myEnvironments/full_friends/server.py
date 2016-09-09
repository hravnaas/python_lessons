from flask import Flask, render_template, request, redirect, flash
import datetime

# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "1234"

# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
	return render_template('index.html', friends=getAllFriends())

# Retrieves all friends from the database.
def getAllFriends():
	select_query = "SELECT id, first_name, last_name, occupation, created_at, updated_at FROM friends"
	return mysql.query_db(select_query)

@app.route('/friends/<id>/edit', methods=['POST'])
def editFriend(id):
	return render_template('edit.html', friend=getFriend(id))

# Get a specified friend from the database.
def getFriend(id):
	select_query = "SELECT id, first_name, last_name, occupation, created_at, updated_at FROM friends WHERE id = :id"
	data = {'id' : id}
	return mysql.query_db(select_query, data)

@app.route('/friends/<id>', methods=['POST'])
def updateFriend(id):
	updateFriendInDb(
		id,
		request.form['first_name'], 
		request.form['last_name'],
		request.form['occupation'])
	return redirect('/')

# Update a friend's name, last name or occupation in the database.
def updateFriendInDb(id, first_name, last_name, occupation):
	update_query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = :updated_at WHERE id = :id"
	data = {
		"first_name" : first_name,
		"last_name" : last_name,
		"occupation" : occupation,
		"updated_at" : datetime.datetime.now(),
		"id" : id
	}

	mysql.query_db(update_query, data)
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