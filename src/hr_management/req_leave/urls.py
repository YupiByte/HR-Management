from django.urls import path, include
from .views import *

urlpatterns = [
    path('request/', submit_leave_request, name="submit_leave_request"),
    path('manage/', manage_leave_request, name="manage_leave_request")
]