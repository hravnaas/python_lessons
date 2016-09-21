from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .models import User
import bcrypt

# Default route when launching web site.
def index(request):
    #allofit = User.objects.raw('SELECT email FROM login_reg_user')
    return render(request, 'login_reg/index.html')

# Used for registering a new user.
def register(request):
    if request.method == 'POST':
        result = User.objects.register(request.POST)
        # Redirect to login/registration page again if there are validation or
        # general registration errors.
        if not result["validated"] or not result["registered"]:
            for err in result["errors"]:
                messages.add_message(request, messages.ERROR, err)
            return redirect(reverse('useradmin:index'))

        # Registration succeeded.
        return render(request, 'login_reg/success.html', { "firstName" : result["user"].first_name, "action" : "registered" })
    return redirect(reverse('useradmin:index'))

# Logs in an existing user.
def login(request):
    if request.method == 'POST':
        result = User.objects.login(request.POST)
        if not result["logged_in"]:
            for err in result["errors"]:
                messages.add_message(request, messages.ERROR, err)
            return redirect('/')
        # User is now logged in.
        request.session['userID'] = result["user"].id #Currently not used.
        request.session['firstName'] = result["user"].first_name
        return render(request, 'login_reg/success.html', { "firstName" : result["user"].first_name, "action" : "logged in" })
    return redirect(reverse('useradmin:index'))

def logout(request):
    if "userID" in request.session:
        del request.session["userID"]

    if "userName" in request.session:
        del request.session["userName"]

    return redirect(reverse('useradmin:index'))
