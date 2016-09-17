from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
import re

def index(request):
    return render(request, 'email_validation/index.html')

def addEmail(request):

    # NOTE NOTE NOTE THIS IS NOT DONE AND IS ONLY PARTIALLY WORKING
    # NOTE NOTE NOTE THIS IS NOT DONE AND IS ONLY PARTIALLY WORKING
    # NOTE NOTE NOTE THIS IS NOT DONE AND IS ONLY PARTIALLY WORKING
    # NOTE NOTE NOTE THIS IS NOT DONE AND IS ONLY PARTIALLY WORKING

    if request.method == 'POST':
        hasErrors = False
        email = request.POST['email']

        # Validate the email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not len(email) > 0 or not EMAIL_REGEX.match(email):
            hasErrors = True
        else:
            # Email is valid, add it to the db.
            Email.objects.create(email = request.POST['email'])
            return redirect('/showAllEmails/' + email)

    messages.add_message(request, 'Email is invalid')
    return redirect(request, '/')

def showAllEmails(request, email):
    context =  {
        "new_email" : email,
        "emails" : Email.objects.all()
    }
    return render(request, 'email_validation/success.html', context)
