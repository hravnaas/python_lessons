from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "1234"

@app.route('/')
def displaySurvery():
    return render_template('survey.html')

@app.route('/submit_survery', methods=['POST'])
def submitSurvey():
	MAX_COMMENT = 120
	userName = request.form['name']
	loc = request.form['location']
	lang = request.form['programming_language']
	comment = request.form['comment']
	hasErrors = False

	#debug
	print len(userName)
	#debug

	if len(userName) < 1:
		flash("Name can't be blank")
		hasErrors = True

	if len(comment) < 1:
		flash("'Comment' can't be blank")
		hasErrors = True
	elif len(comment) > 120:
		flash("'Comment' can't be longer than {} characters. It is exceeding it by {} characters.".format(MAX_COMMENT, len(comment) - MAX_COMMENT))
		hasErrors = True

	if hasErrors == True:
		return redirect('/')

	return render_template('submitted.html', name=userName, loc=loc, lang=lang, comment=comment)

app.run(debug=True)