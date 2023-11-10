from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import *



# View all requests
def view_request(request):

    view_request = Request.objects.all()

    context = {"view_request": view_request}
    return render(request, "view_request.html", context)


# Creates a leave request form
def submit_request(request):

    request_form = RequestCreateForm(request.POST or None)

    if request_form.is_valid():

        start_date = request_form.cleaned_data.get('start_date')
        end_date = request_form.cleaned_data.get('end_date')

        print(f"From: {start_date}\nTo: {end_date}\n\
        Days Requested:{days_requested(start_date, end_date)}")
        
        request_form.save()
        request_form = RequestCreateForm()

        return redirect(view_request)


    context = {"request_form": request_form}
    return render(request, "request.html", context)


# Obsolete (?)
def manage_request(request):

    if request.method == 'POST':
        form = RequestCreateForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data.get('manage_request')
            pk = form.cleaned_data.get('request_id')
            leave_request = get_object_or_404(Request, pk=pk)

            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            print(f"From: {start_date}\nTo: {end_date}\n\
            Days Requested:{days_requested(start_date, end_date)}")

            if action == 'Accept':
                leave_request.request_status = 'Accepted'
            elif action == 'Decline':
                leave_request.request_status = 'Declined'

            leave_request.save()
    else:
        form = RequestCreateForm()

    view_request = Request.objects.all()

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
