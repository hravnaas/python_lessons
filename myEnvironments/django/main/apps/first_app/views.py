from django.shortcuts import render, HttpResponse

# Create your views here.
# While Django will automatically create the request object for us that's passed into our method, HttpResponse
# objects are our responsibility to create and return to the browser.
  #  Note that 'render' is a shortcut method that combines a given template with a given context dictionary and
  # returns an HttpResponse object with that rendered text.
  # Create your views here.
  # THIS IS THE CONTROLLER
def index(request):
 #response = "Hello, I am your first request!"
 #return HttpResponse(response)
 return render(request, 'first_app/index.html')
 # Not using render because we haven't created any templates yet!
