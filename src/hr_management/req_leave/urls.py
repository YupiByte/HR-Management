from django.urls import path, include
from .views import *

urlpatterns = [
    path('', request_submit, name="request_leave")
    # path('', submit_leave_request, name="request_leave"),
    # path('manage/', manage_leave_request, name="manage_leave")
]