from django.shortcuts import render, redirect
#from . import models
from .models import Course, Description, Comment
from ..login_reg.models import User

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

    return redirect('/courses')

def CourseRemoveConfirmation(request, courseID):
    # Grab the course about to be deleted and prompt user for confirmation.
    return render(request, 'courses/confirmation.html', { "course":  Course.objects.get(id = courseID) })


def removeCourse(request, courseID):
    # User has confirmed deletion. It's on.
    # Delete comments associated with course.
    Description.objects.filter(course_id = courseID).delete()

    # Delete course itself.
    Course.objects.filter(id = courseID).delete()

    return redirect('/courses')

def addUserToCourse(request):
    #Get all the courses and users from the db.
    courses_users = Course.objects.all()
    users = User.objects.all();
    return render(request, 'courses/users_courses.html', { "courses_users" : courses_users, "users" : users } )

def linkUserToCourse(request):
    course = Course.objects.get(id = request.POST['course_id'])
    user = User.objects.get(id = request.POST['user_id'])
    course.user.add(user)

    return redirect('/courses/users_courses')
