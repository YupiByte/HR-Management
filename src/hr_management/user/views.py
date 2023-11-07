from django.shortcuts import render, HttpResponse
from .models import Employee, Admin



def home(request):
    return render(request, "index.html")

# Dummy page for features under construction
def tmp(request):
    return render(request, "tmp.html")

# Admin landing page after authentication
def admin_home(request):
    context = {"title": "Dashboard"}
    return render(request, "admin_home.html", context)


def manage_employees(request):
    employees = Employee.objects.all()
    context = {"title": "Manage Employees", 'employees': employees}
    return render(request, '../templates/administrator/manage_employees.html', context)




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




