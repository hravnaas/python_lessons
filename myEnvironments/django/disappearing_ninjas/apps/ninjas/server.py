from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "1234"

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/ninja')
def showNinjas():
	return render_template('image.html', imageName="ninjas.png")

@app.route('/ninja/<color>')
def coloredNinja(color):
	colorImageMappings = {
		"blue": "leonardo.jpg",
		"red": "raphael.jpg",
		"orange" : "michelangelo.jpg",
		"purple" : "donatello.jpg"
	}
	
	try:
		imageName = colorImageMappings[color.lower()]
	except Exception, e:
		return render_template('image.html', imageName="notapril.jpg")
	else:
		pass
	finally:
		pass
	 
	return render_template('image.html', imageName=imageName)

app.run(debug=True)

