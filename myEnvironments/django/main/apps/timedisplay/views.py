from django.shortcuts import render #, HttpResponse
from time import localtime, strftime

# Create your views here.
def index(request):
	# Formatting stolen from http://www.tutorialspoint.com/python/time_strftime.htm
	# currentlocalTime = localtime()
	# print currentlocalTime
	# TODO: The below does NOT convert to local time as expected, but leaves date/time in UTC/GMT.
	context = { "currentMonthYear" : strftime("%b %d, %Y", localtime()), "currentTime" : strftime("%r %Z", localtime()) }
	return render(request, 'timedisplay/index.html', context)