from django.shortcuts import render, redirect
#from . import models
from .models import Course, Description, Comment

def index(request):

    allCourses = Course.objects.all()
    print allCourses

    context = {
        "courses" : Course.objects.all()
    }

    return render(request, 'courses/index.html', context)

def addCourse(request):
    print "Adding course"
    #if request.method == 'POST':
    courseId = Course.objects.create(name="Algorithms dummy data for now")
    print "Course ID: ", courseId

    return redirect('/')

def removeCourse(request, courseID):
    print "Remove course", courseID
    return render(request, 'courses/index.html')
