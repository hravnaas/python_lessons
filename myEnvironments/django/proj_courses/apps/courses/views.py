from django.shortcuts import render, redirect
#from . import models
from .models import Course, Description, Comment

# TODO: Add support for comments if time allows.
# TODO: Add sexy CSS.

def index(request):
    return render(request, 'courses/index.html', { "courses" : Course.objects.all() })

def addCourse(request):
    if request.method == 'POST' and len(request.POST['courseName']) > 0:

        # Add the new course
        newCourse = Course.objects.create(name=request.POST['courseName'])

        # Add description for new course
        newDescription = Description.objects.create(
            description = request.POST['description'],
            course = newCourse
        )

    return redirect('/')

def CourseRemoveConfirmation(request, courseID):
    # Grab the course about to be deleted and prompt user for confirmation.
    return render(request, 'courses/confirmation.html', { "course":  Course.objects.get(id = courseID) })


def removeCourse(request, courseID):
    # User has confirmed deletion. It's on.
    # Delete comments associated with course.
    Description.objects.filter(course_id = courseID).delete()

    # Delete course itself.
    Course.objects.filter(id = courseID).delete()

    return redirect('/')
