from django.shortcuts import render, redirect
from .models import Employee, Administrator
from .forms import CreateEmployeeForm

'''
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
'''


def home(request):
    return render(request, "index.html")

# Dummy page for features under construction
def tmp(request):
    return render(request, "tmp.html")

# Admin landing page after authentication
def admin_home(request):
    context = {"title": "Dashboard"}
    return render(request, "../templates/administrator/admin_home.html", context)


# def manage_employees(request):
#     employees = Employee.objects.all()
#     context = {"title": "Manage Employees", 'employees': employees}
#     return render(request, '../templates/administrator/manage_employees.html', context)


def manage_employees(request):
    employees = Employee.objects.all()
	# # Check to see if logging in
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
	# 	# Authenticate
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, "You Have Been Logged In!")
    #         return redirect('home')
    #     else:
    #         messages.success(request, "There Was An Error Logging In, Please Try Again...")
    #         return redirect('home')
    # else:
    return render(request, '../templates/administrator/manage_employees.html', {'title':'Manage Employees', 'employees':employees})


def create_employee(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
	# 		# Authenticate and login
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password1']
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         messages.success(request, "You Have Successfully Registered! Welcome!")
    #         return redirect('home')
    # else:
    form = CreateEmployeeForm()
    return render(request, '../templates/administrator/create_employee.html', {'form':form})


def employee_record(request, pk):
	# if request.user.is_authenticated:
	employee_record = Employee.objects.get(id=pk) # Look Up Records
	return render(request, '../templates/administrator/employee_record.html', {'title': 'Employee Record', 'employee_record':employee_record})
	# else:
	# 	messages.success(request, "You Must Be Logged In To View That Page...")
	# 	return redirect('home')

'''
def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
'''






# =====================> from 4-hr tutorial
# def create_employee_view(request):
#     form = CreateEmployeeForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = CreateEmployeeForm()

#     context = {
#         'title': 'Add Employee',
#         'form': form
#     }
#     return render(request, "../templates/administrator/create_employee.html", context)


# def create_employee_view(request):
#     my_form = CreateEmployeeForm()
#     if request.method == "POST":
#         my_form = CreateEmployeeForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Employee.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'title': 'Add Employee',
#         'form': my_form
#     }
#     return render(request, "../templates/administrator/create_employee.html", context)
# <=================================




