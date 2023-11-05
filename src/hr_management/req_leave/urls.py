from django.urls import path, include
from req_leave.views import *

urlpatterns = [
    path('', submit_leave_request, name="request_leave"),
    path('manage/', manage_leave_request, name="manage_leave")
]