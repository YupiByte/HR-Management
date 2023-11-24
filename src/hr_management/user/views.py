from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import RegisterEmployeeForm, UpdateEmployeeForm, EditProfileForm
from django.urls import reverse



# Reference custom user model Employee
Employee = get_user_model()



def is_admin(user):
    return user.is_authenticated and user.is_staff



# ======> Admin Views <======

# @user_passes_test(is_admin, login_url='admin_home') # <====== CHECK
# Admin landing page after authentication
def admin_home(request):
	if request.user.is_authenticated and request.user.is_staff:
		context = {"title": "Dashboard"}
		return render(request, "../templates/administrator/admin_home.html", context)
	else:
		messages.success(request, "(from admin_home) You must be Admin and be Logged In To View That Page...")
		return redirect('login')  



def manage_employees(request):
	if request.user.is_authenticated and request.user.is_staff:
		employees = Employee.objects.all()
		context = {"title": "Manage Employees", 'employees': employees}
		return render(request, '../templates/administrator/manage_employees.html', context)
	else:
			messages.success(request, "(from manage_employees) You must be Admin and be logged in and have permission to view this page...")
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



def employee_record(request, pk):
	if request.user.is_authenticated and request.user.is_staff:
		employee_record = Employee.objects.get(id=pk) # Look Up Records
		return render(request, '../templates/administrator/employee_record.html', {'title': 'Employee Record', 'employee_record':employee_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



# @user_passes_test(is_admin, login_url='home')
def update_employee(request, pk):
	if request.user.is_authenticated and request.user.is_staff:
		current_employee = Employee.objects.get(id=pk)

		form = UpdateEmployeeForm(request.POST or None, instance=current_employee)
		if form.is_valid():
			form.save()
			messages.success(request, "Employee Record Has Been Updated by Administrator.")
			url = reverse('employee_record', args=[pk]) # generate the URL for the employee record page
			return redirect(url)
		return render(request, '../templates/administrator/update_employee.html', {'title': 'Update Employee Record', 'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
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




# ======> Employee Views <======


def employee_home(request):
    # Retrieve user attributes from the database
	if request.user.is_authenticated and not(request.user.is_staff):

		user_attributes = Employee.objects.get(id=request.user.id) 
		first_name = user_attributes.first_name
		last_name = user_attributes.last_name

		
		# emp_requests = # Function query to req_leave history
		
		title = f"Welcome {first_name}!"
		context = {
			'user_attributes': user_attributes,
			# 'emp_requests': emp_requests,
			'title': title
		}
		return render(request, '../templates/employees/employee_home.html', context)
	else:
		messages.success(request, "You must be Employee and be Logged In To View That Page...")
		return redirect('login')  



# Employee view for editing first name, last name, email, and phone number
def edit_profile(request):
	if request.user.is_authenticated:
		current_employee = Employee.objects.get(id=request.user.id)

		form = EditProfileForm(request.POST or None, instance=current_employee)
		if form.is_valid():
			form.save()
			messages.success(request, "Employee Record Has Been Updated by Employee.")
			return redirect('employee_home')
		return render(request, '../templates/employees/edit_profile.html', {'title': 'Edit My Profile', 'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
