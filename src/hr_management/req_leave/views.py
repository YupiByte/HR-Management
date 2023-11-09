from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from .models import *
from .forms import *



# View all requests
def view_request(request):

    view_request = Request.objects.all()

    context = {"view_request": view_request}
    return render(request, "view_request.html", context)


# Creates a leave request form
def request_submit(request):

    request_form = RequestCreateForm(request.POST or None)

    if request_form.is_valid():

        start_date = request_form.cleaned_data.get('start_date')
        end_date = request_form.cleaned_data.get('end_date')

        print(f"From: {start_date}\nTo: {end_date}\n\
        Days Requested:{days_requested(start_date, end_date)}")
        
        request_form.save()
        request_form = RequestCreateForm()

        # return redirect(view_request)


    context = {"request_form": request_form}
    return render(request, "request.html", context)


# Approve / Reject
def manage_request(request):

    ''''''

