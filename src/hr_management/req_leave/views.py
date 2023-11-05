from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Request
from .forms import LeaveRequestForm



def submit_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user
            leave_request.status = 'Pending'
            leave_request.save()
            return redirect('leave_request_success')  # Redirect to a success page
    else:
        form = LeaveRequestForm()
    
    context = {'form': form}
    return render(request, 'req_leave/submit_leave_request.html', context)



def manage_leave_request(request):
    # if not request.user.is_manager:  # Check if the user is a manager
        # raise Http404  # Handle unauthorized access
    
    leave_requests = Request.objects.all()
    
    context = {'leave_requests': leave_requests}
    return render(request, 'req_leave/manage_leave_request.html', context)



def leave_request_approval(request):
    if request.method == 'POST':
        leave_request_id = request.POST.get('leave_request_id')
        status = request.POST.get('status')
        leave_request = Request.objects.get(id=leave_request_id)
        leave_request.status = status
        leave_request.save()
    leave_requests = Request.objects.filter(status='Pending')
    return render(request, 'leaves/request_approval.html', {'leave_requests': leave_requests})