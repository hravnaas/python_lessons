from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def displaySurvery():
    return render_template('survey.html')

@app.route('/submit_survery', methods=['POST'])
def submitSurvey():
    userName = request.form['name']
    loc = request.form['location']
    lang = request.form['programming_language']
    comment = request.form['comment']
    return render_template('submitted.html', name=userName, loc=loc, lang=lang, comment=comment)

app.run(debug=True)