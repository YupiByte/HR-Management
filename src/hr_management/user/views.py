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
    return render(request, 'manage_employees.html', context)



