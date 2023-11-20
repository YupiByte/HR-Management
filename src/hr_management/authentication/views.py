from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages


# Reference custom user model Employee
Employee = get_user_model()

def login_user(request):
	# Check if the user is already authenticated
	if request.user.is_authenticated:
		if request.user.is_staff:
			return render(request, '../templates/administrator/admin_home.html', {'title': 'Administrator'})
		else:
			return render(request, '../templates/employees/employee_home.html', {'title': 'Employee'})

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