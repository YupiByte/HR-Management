from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from .models import *
from .forms import *



def home_view(*args, **kwargs):
    return HttpResponse("<h1> Test </h1>")

# View all requests
def view_request(request):

    request_form = Request.objects.all()

    context = {"request_form": request_form}
    return render(request, "request.html", context)


# Creates a leave request form
def request_submit(request):

    # request_form = Request.objects.all()

    # if not request_form:
    request_form = RequestCreateForm(request.POST or None)

    if request_form.is_valid():
        request_form.save()
        request_form = RequestCreateForm()

    # if not request_form.is_valid():
    #     return HttpResponse("<h1> Invalid Request Form </h1>")

    context = {"request_form": request_form}
    return render(request, "request.html", context)


# def submit_leave_request(request):

#     form = LeaveRequestForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         form = LeaveRequestForm()


#     context = {
#         'form': form
#     }

#     return render(request, "req_leave/submit_leave_request.html", context)


# def submit_leave_request(request):



#     if request.method == 'POST':
#         form = LeaveRequestForm(request.POST)
#         if form.is_valid():
#             leave_request = form.save(commit=False)

#             leave_request.

#             leave_request.request_status = 'Pending'
#             leave_request.save()
#             # return redirect('leave_request_success')  # Redirect to a success page
#     else:
#         form = LeaveRequestForm()
    
#     context = {'form': form}
#     return render(request, 'submit_leave_request.html', context)



# def manage_leave_request(request):
#     # if not request.user.is_manager:  # Check if the user is a manager
#         # raise Http404  # Handle unauthorized access
    
#     leave_requests = Request.objects.all()
    
#     context = {'leave_requests': leave_requests}
#     return render(request, 'req_leave/manage_leave_request.html', context)



# def leave_request_approval(request):
#     if request.method == 'POST':
#         leave_request_id = request.POST.get('leave_request_id')
#         status = request.POST.get('status')
#         leave_request = Request.objects.get(id=leave_request_id)
#         leave_request.status = status
#         leave_request.save()
#     leave_requests = Request.objects.filter(status='Pending')
#     return render(request, 'request_approval.html', {'leave_requests': leave_requests})