from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
# Necessary for making queries; Retrieving corresponding employee(s)
from django.db import models
from .models import *
from .forms import *



# View all requests
def view_request(request):

    # Utilize this alongside a function to obtain the current
    # logged in employee's ID (MAKE SURE TO GET CORRECT EMPLOYEE_ID)
    # request_query = Request.objects.filter(employee_id="Shrimp")

    # Comment / Remove this
    view_request = Request.objects.all()

    # Calculating days requested per request
    for leave_request in view_request:
        leave_request.days_requested = \
            days_requested(leave_request.start_date, leave_request.end_date)

    # Comment / Remove this
    context = {"view_request": view_request}

    # Uncomment this
    # context = {"view_request": request_query}
    return render(request, "view_request.html", context)


# Creates a leave request form
def submit_request(request):

    request_form = RequestCreateForm(request.POST or None)

    if request_form.is_valid():
        
        request_form.save()
        request_form = RequestCreateForm()

        return redirect(reverse("req_leave:submit_request"))


    context = {"request_form": request_form}
    return render(request, "request.html", context)


# Canceling submitted request, for the employee
# in case of accidental / erroneous request
def cancel_request(request, id):

    cancel_request = get_object_or_404(Request, id=id)

    if request.method == "POST":
        
        cancel_request.delete()
        return redirect("../../view")

    context = {"request": cancel_request}
    return render(request, "view_request.html", context)

# For managing requests
def manage_request(request):

    if request.method == 'POST':

        form = RequestCreateForm(request.POST)

        if form.is_valid():

            action = form.cleaned_data.get('manage_request')
            pk = form.cleaned_data.get('request_id')
            leave_request = get_object_or_404(Request, pk=pk)

            if action == 'Accept':
                leave_request.request_status = 'Accepted'
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




@require_POST
def update_request_status(request, pk):
    leave_request = get_object_or_404(Request, pk=pk)
    action = request.POST.get('action')

    if action == 'accept':
        leave_request.request_status = 'Accepted'
    elif action == 'decline':
        leave_request.request_status = 'Declined'

    leave_request.save()

    return redirect('manage_request')
