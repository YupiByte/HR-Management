from django.shortcuts import render, HttpResponse
from .models import Employee, Admin

# Create your views here.
def home(request):
    return render(request, "index.html")

def admin_employees(request):
    item = Employee.objects.all()
    context = {"item": item}
    return render(request, "admin_employees.html", context) # return all items in the Employee object


def admin_home(request):
    navigation_data = [
        {"name": "Dashboard", "url": "admin_home"},
        {"name": "Employees", "url": "admin_employees"}, # Change to Manage Employees link
        {"name": "Dummy Home", "url": "home"}, # Change to Manage Requests link
        {"name": "Dummy Home", "url": "home"}, # Change to Calendar link
        {"name": "Dummy Home", "url": "home"}, # Change to Publications link
    ]

    context = {"title": "Dashboard", "navigation_data": navigation_data}
    return render(request, "admin_home.html", context)

