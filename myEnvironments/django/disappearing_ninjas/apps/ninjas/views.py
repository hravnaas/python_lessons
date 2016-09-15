from django.shortcuts import render, redirect

# Default route (/)
def index(request):
	return render(request, "ninjas/index.html")

def showFourTurtles(request):
	context = { "imageName" : "ninjas.png" }
	return render(request, "ninjas/image.html", context)

def showImage(request, myColor):
	color = myColor.lower()

	colorImageMappings = {
		"blue": "leonardo.jpg",
		"red": "raphael.jpg",
		"orange" : "michelangelo.jpg",
		"purple" : "donatello.jpg"
	}
	
	imageName = "notapril.jpg"

	try:
		imageName = colorImageMappings[color]
	except Exception, e:
		pass
	else:
		pass
	finally:
		pass

	return render(request, "ninjas/image.html", { "imageName" : imageName })

