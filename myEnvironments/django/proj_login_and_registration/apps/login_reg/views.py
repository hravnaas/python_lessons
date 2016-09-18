from django.shortcuts import render, redirect
from .models import User
import inputchk

# inputchk.validateAllFields()

# TODO: After login, show first name, not email.
# TODO: Support storing and validating birthday.

# Default route when launching web site.
def index(request):
    return render(request, 'login_reg/index.html')

# Used for registering a new user.
def register(request):
    if request.method == 'POST':
        inputchk.validateAllFields(request)

    # Redirect to login/registration page if there are validation errors.
    if hasErrors():
        return redirect('/')

    # Input validation passed. Save user to the database.
    
    return render(request, 'login_reg/success.html', { "fullName" : request.POST['First Name'], "action" : "registered" })

# Logs in an existing user.
def login(request):
    if True:
        return render(request, 'login_reg/success.html', { "fullName" : request.POST['email'], "action" : "logged in" })

    # Add error messages if any.
    return redirect('/')

def hasErrors(request):
    if len(messages.get_messages(request)) > 0:
        storage.used = False
        return True
    return False

# def login():
# 	if "userId" not in session:
# 		if len(request.form) < 1:
# 			# User is not logged in and no info was posted. Force another login.
# 			return render_template('login.html')
#
# 		# Log the user in by grabbing the encrypted password from the database
# 		# and comparing it to the provided password after encrypting it.
# 		badLogin = "Incorrect user name or password"
# 		user = getUserByEmail(request.form["email"])
# 		if len(user) != 1:
# 			# User does not exist in the database.
# 			flash(badLogin)
# 			return render_template('login.html')
# 		try:
# 			if not bcrypt.check_password_hash(user[0]["password"], request.form['password']):
# 				flash(badLogin)
# 				return render_template('login.html')
# 		except Exception, e:
# 			# Handle situation when the salt is bad, etc.
# 			flash("Unexpected error, please try again (" + e.message + ")")
# 			return render_template('login.html')
#
# 		# Credentials look good.
# 		session['userId'] = user[0]["id"]
# 		session['firstName'] = user[0]["first_name"]
#
# 	# User is (now) considered logged in. Go to the wall.
# 	return toTheWall()
