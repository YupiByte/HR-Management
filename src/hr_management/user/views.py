from django.shortcuts import render, redirect
from .models import NewUser
from .forms import RegisterEmployeeForm, AddEmployeeForm
from django.contrib import messages
from django.urls import reverse
# from .forms import SignUpForm, AddRecordForm



def home(request):
    return render(request, "index.html")

# Dummy page for features under construction
def tmp(request):
    return render(request, "tmp.html")

# Admin landing page after authentication
def admin_home(request):
    context = {"title": "Dashboard"}
    return render(request, "../templates/administrator/admin_home.html", context)



def manage_employees(request):
    employees = NewUser.objects.all()
    context = {"title": "Manage Employees", 'employees': employees}
    return render(request, '../templates/administrator/manage_employees.html', context)



def manage_employees(request):
    employees = NewUser.objects.all()
	# Check to see if logging in
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



def register_employee(request):
    if request.method == 'POST':
        form = RegisterEmployeeForm(request.POST)
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
    form = RegisterEmployeeForm()
    return render(request, '../templates/administrator/register_employee.html', {'form':form})

	# return render(request, 'register.html', {'form':form})



def employee_record(request, pk):
	if request.user.is_authenticated:
		employee_record = NewUser.objects.get(id=pk) # Look Up Records
		return render(request, '../templates/administrator/employee_record.html', {'title': 'Employee Record', 'employee_record':employee_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('tmp')



def delete_employee(request, pk):
     delete_it = NewUser.objects.get(id=pk)
	#  Add conditional to confirm deletion of employee <=================================
     delete_it.delete()
     messages.success(request, "Employee Deleted Successfully")
    
     return redirect('manage_employees')



def add_employee(request):
	form = AddEmployeeForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_employee = form.save()
				messages.success(request, "Employee Added...")
				return redirect('manage_employees')
		return render(request, '../templates/administrator/add_employee.html', {'title':'Add Employee', 'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('manage_employees')
      


def update_employee(request, pk):
	if request.user.is_authenticated:
		current_employee = NewUser.objects.get(id=pk)
		form = AddEmployeeForm(request.POST or None, instance=current_employee)
		if form.is_valid():
			form.save()
			messages.success(request, "Employee Record Has Been Updated!")
			url = reverse('employee_record', args=[pk]) # generate the URL for the employee record page
			return redirect(url)
		return render(request, '../templates/administrator/update_employee.html', {'title':'Update Employee Record', 'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('manage_employees')
      

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

