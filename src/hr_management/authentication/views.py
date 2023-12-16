from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Reference custom user model Employee
Employee = get_user_model()

@never_cache
def login_user(request):
	# Check if the user is already authenticated and redirect them 
	# to their corresponding home page
	if request.user.is_authenticated:
		if request.user.is_staff:
			return redirect('admin_home')
		else:
			return redirect('employee_home')


    # Check if the form is submitted
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
        
        # Authenticate user
		user = authenticate(request, email=email, password=password)

		if user is not None:
            # Log the user in
			login(request, user)

			if user.is_staff:
				messages.success(request, "You have been logged in!")
				return redirect('admin_home')
			else:
				return redirect('employee_home')
		else:
			messages.error(request, "Invalid email or password. Please try again.")

	return render(request, '../templates/login.html', {'title': 'Login'})


def logout_user(request): 
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('login')