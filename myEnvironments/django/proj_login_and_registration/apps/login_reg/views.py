from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import inputchk
import bcrypt

# inputchk.validateAllFields()

# TODO: After login, show first name, not email.
# TODO: Support storing and validating birthday.

# Default route when launching web site.
def index(request):
    #allofit = User.objects.raw('SELECT email FROM login_reg_user')
    return render(request, 'login_reg/index.html')

# Used for registering a new user.
def register(request):
    if request.method == 'POST':
        inputchk.validateAllFields(request)

        # Redirect to login/registration page if there are validation errors.
        if hasErrors(request):
            return redirect('/')

        # Input validation passed. Save user to the database.
        User.objects.create(
            first_name = request.POST['First Name'],
            last_name = request.POST['Last Name'],
            email = request.POST['Email'],
            password = bcrypt.hashpw(request.POST['Password'].encode(), bcrypt.gensalt()),
            birthday = request.POST['Birthday']
        )

        return render(request, 'login_reg/success.html', { "fullName" : request.POST['First Name'], "action" : "registered" })
    return redirect('/')

# Logs in an existing user.
def login(request):
    if request.method == 'POST':
        try:
            existingPassword = User.objects.filter(email = request.POST['Email'])[0].password
            if bcrypt.hashpw(request.POST['Password'].encode(), existingPassword.encode()) != existingPassword:
                print "bad password"
                return redirect('/')
            print "good password"
     	except Exception, e:
     	      # Handle situation when the salt is bad, etc.
     	    print "Unexpected error, please try again (" + e.message + ")"
            return redirect('/')

        return render(request, 'login_reg/success.html', { "fullName" : request.POST['Email'], "action" : "logged in" })

    # Add error messages if any.
    return redirect('/')

def hasErrors(request):
    return len(messages.get_messages(request)) > 0

# Get specified user from the database based on provided email.
def getUserByEmail(email):
	# Note that caller needs to handle non-existent user.

	select_query = "SELECT id, first_name, password FROM users WHERE email = :email LIMIT 1"
	data = {'email' : email}
	return mysql.query_db(select_query, data)
