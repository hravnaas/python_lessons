from django.shortcuts import render, redirect

# Starting point
def index(request):
	return render(request, 'survey_form/index.html')

def process(request):
	if request.method == 'POST':
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		return	render(request, 'survey_form/result.html')
	
	return redirect(request, '/')
