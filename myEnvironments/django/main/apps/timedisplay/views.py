from django.shortcuts import render #, HttpResponse
import time

# Create your views here.
def index(request):
	# Formatting stolen from http://www.tutorialspoint.com/python/time_strftime.htm
	context = { "currentMonthYear" : time.strftime("%b %d, %Y"), "currentTime" : time.strftime("%r") }
	return render(request, 'timedisplay/index.html', context)