from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import RegisterEmployeeForm, UpdateEmployeeForm
from django.urls import reverse



# Reference custom user model Employee
Employee = get_user_model()


def home(request):
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
				# return render(request, '../templates/administrator/admin_home.html', {'title': 'Administrator'})
				return redirect('admin_home')
			else:
				return redirect('employee_home')
		else:
			messages.error(request, "Invalid email or password. Please try again.")

	return render(request, '../templates/home.html', {'title': 'Login'})



@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')


def is_admin(user):
    return user.is_authenticated and user.is_staff


# @user_passes_test(is_admin, login_url='admin_home') # <====== CHECK
# Admin landing page after authentication
def admin_home(request):
	if request.user.is_authenticated and request.user.is_staff:
		context = {"title": "Dashboard"}
		return render(request, "../templates/administrator/admin_home.html", context)
	else:
		messages.success(request, "(from admin_home) You Must Be Logged In To View That Page...")
		return redirect('home')   
	
def employee_home(request):
	if request.user.is_authenticated and not request.user.is_staff:
		messages.success(request, "(from employee_home) Employee, you Have Been Logged In!")
		context = {"title": "Employee"}
		return render(request, "../templates/employees/employee_home.html", context)
	else:
		messages.success(request, "(from employee_home) Employee, you Must Be Logged In To View That Page...")
		return redirect('home')  



def tmp(request):
    return render(request, "tmp.html")



def manage_employees(request):
	# if request.user.is_authenticated:
	if request.user.is_authenticated and request.user.is_staff:
		employees = Employee.objects.all()
		context = {"title": "Manage Employees", 'employees': employees}
		return render(request, '../templates/administrator/manage_employees.html', context)
	else:
			messages.success(request, "(from manage_employees) You must be logged in and have permission to view this page...")
			return redirect('home')




def logout_user(request): # erased to explore Login App with tutorial 
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')



def register_employee(request):
	if request.user.is_authenticated and request.user.is_staff:
		if request.method == 'POST':
			form = RegisterEmployeeForm(request.POST)
			if form.is_valid():
				form.save()
				# Authenticate and login
				email = form.cleaned_data['email']
				password = form.cleaned_data['password1']
				# user = authenticate(email=email, password=password)
				# login(request, user)
				authenticate(email=email, password=password)
				messages.success(request, "(from register_employee) Employee Successfully Registered")
				return redirect('admin_home')
		else:
			form = RegisterEmployeeForm()
			return render(request, '../templates/administrator/register_employee.html', {'form':form})

		return render(request, '../templates/administrator/register_employee.html', {'form':form})
	else:
		messages.success(request, "(from register_employee) You Must Be Logged In To View That Page...")
		return redirect('manage_employees')



# def add_employee(request):
# 	form = AddEmployeeForm(request.POST or None)
# 	if request.user.is_authenticated:
# 		if request.method == "POST":
# 			if form.is_valid():
# 				add_employee = form.save()
# 				messages.success(request, "Employee Added...")
# 				return redirect('manage_employees')
# 		return render(request, '../templates/administrator/add_employee.html', {'title':'Add Employee', 'form':form})
# 	else:
# 		messages.success(request, "You Must Be Logged In...")
# 		return redirect('manage_employees')



def employee_record(request, pk):
	# if request.user.is_authenticated:
	if request.user.is_authenticated and request.user.is_staff:
		employee_record = Employee.objects.get(id=pk) # Look Up Records
		return render(request, '../templates/administrator/employee_record.html', {'title': 'Employee Record', 'employee_record':employee_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_employee(request, pk):
	if request.user.is_authenticated:
		delete_it = Employee.objects.get(id=pk)
		#  Add conditional to confirm deletion of employee <=================================
		delete_it.delete()
		messages.success(request, "Employee Deleted Successfully")
		return redirect('manage_employees')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

      

# @user_passes_test(is_admin, login_url='home')
def update_employee(request, pk):
	if request.user.is_authenticated and request.user.is_staff:
		current_employee = Employee.objects.get(id=pk)
		form = UpdateEmployeeForm(request.POST or None, instance=current_employee)
		if form.is_valid():
			form.save()
			messages.success(request, "Employee Record Has Been Updated!")
			url = reverse('employee_record', args=[pk]) # generate the URL for the employee record page
			return redirect(url)
		return render(request, '../templates/administrator/update_employee.html', {'title':'Update Employee Record', 'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

