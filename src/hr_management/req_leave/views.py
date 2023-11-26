from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404, HttpResponse
# Messages used for cancelling request unavailability
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_POST
# Necessary for making queries; Retrieving corresponding employee(s)
from django.db import models
from .models import *
# For adding absences to Calendar
from calendar_app.models import Absence_Calendar
from .forms import *

# Used for validating available days off request(s)
from user.models import Employee

# View all requests
def view_request(request):

    # Utilize this alongside a function to obtain the current
    # logged in employee's ID (MAKE SURE TO GET CORRECT EMPLOYEE_ID)
    get_logged_employee = request.user
    request_query = Request.objects.filter(employee_id=get_logged_employee)

    # This will present all the current requests, of all users
    # Leave it only for development purposes
    # view_request = Request.objects.all()

    # Change view_request to request_query
    # Calculating days requested per request
    for leave_request in request_query:
        leave_request.days_requested = \
            days_requested(leave_request.start_date, leave_request.end_date)


    # For development purposes
    # context = {"view_request": view_request}

    # Uncomment this for current logged user only
    context = {"view_request": request_query}
    return render(request, "view_request.html", context)


# Creates a leave request form
def submit_request(request):

    request_form = RequestCreateForm(request.POST or None)

    if request_form.is_valid():

        # Creates but doesn't saves yet
        new_request_form = request_form.save(commit=False)

        # Validating requested days are available for user
        employee = Employee.objects.get(username=request.user)
        days_req = days_requested(new_request_form.start_date, \
                                  new_request_form.end_date)

        if new_request_form.request_type == 'PTO'\
              and days_req > employee.available_pto:
            messages.error(request, "Insufficient PTO days available")


        elif new_request_form.request_type == 'Sick Day'\
              and days_req > employee.available_sickdays:
            messages.error(request, "Insufficient Sick Days available")


        # Assign to employee_id currently logged user:
        new_request_form.employee_id = request.user.username

        # Save instance with the employee's username added
        new_request_form.save()

        return redirect(reverse("req_leave:submit_request"))

    # Getting the request
    # This is so we can present the requests received in Admin
    # and the manage panel(s) 
    else:
        initial = {'employee_id': request.user.username}
        request_form = RequestCreateForm(initial=initial)

    context = {"request_form": request_form}
    return render(request, "request.html", context)


# Canceling submitted request, for the employee
# in case of accidental / erroneous request
def cancel_request(request, id):

    cancel_request = get_object_or_404(Request, id=id)

    if cancel_request.request_status != "Pending":
        messages.info(request, "Can't cancel request that has been attended!")
        return redirect("../../view")

    if request.method == "POST":
        
        cancel_request.delete()
        return redirect("../../view")

    context = {"request": cancel_request}
    return render(request, "view_request.html", context)


# For managing requests
def manage_request(request):

    if request.user.is_authenticated and request.user.is_staff:

        if request.method == 'POST':

            form = RequestCreateForm(request.POST)

            if form.is_valid():

                # Gets a cleaned form 
                # (raw data stripped from Django's widget)
                action = form.cleaned_data.get('manage_request')
                pk = form.cleaned_data.get('request_id')
                leave_request = get_object_or_404(Request, pk=pk)

                if action == 'Accept':
                    leave_request.request_status = 'Accepted'

                # Update employees available days
                employee = Employee.objects.get(\
                    username=leave_request.employee_id)

                if leave_request.request_type == 'PTO':
                    employee.available_pto -= \
                        days_requested(leave_request.start_date, \
                                        leave_request.end_date)

                elif leave_request.request_type == 'Sick Day':
                    employee.available_sickdays -= \
                        days_requested(leave_request.start_date, \
                                        leave_request.end_date)

                elif action == 'Decline':
                    leave_request.request_status = 'Declined'

                    leave_request.save()
        
        else:
            form = RequestCreateForm()

        view_request = Request.objects.all()
        
        for leave_request in view_request:
            leave_request.days_requested = \
                days_requested(leave_request.start_date, leave_request.end_date)

        context = {"view_request": view_request, "form": form}
        return render(request, "manage_request.html", context)
    
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('login')



# Utilized for updating the request status
# that is when a form is updated (POST)
@require_POST
def update_request_status(request, pk):

    leave_request = get_object_or_404(Request, pk=pk)
    action = request.POST.get('action')

    if action == 'accept':

        # Check if it has already been Accepted
        # Dont do anything
        if leave_request.request_status == 'Accepted':
            return redirect('req_leave:manage_request')

        leave_request.request_status = 'Accepted'

        # Send data to calendar_app's Calendar models.py
        Absence_Calendar.objects.create(
            employee_id = leave_request.employee_id,
            start_date = leave_request.start_date,
            end_date = leave_request.end_date,
        )


    elif action == 'decline':

        # Check if it has already been Declined
        # Dont do anything
        if leave_request.request_status == 'Declined':
            return redirect('req_leave:manage_request')

        leave_request.request_status = 'Declined'

    leave_request.save()

    return redirect('req_leave:manage_request')
