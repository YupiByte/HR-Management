from django.urls import path
from .views import *

app_name = 'req_leave'

urlpatterns = [
    path('', submit_request, name="submit_request"),
    path('submit/', submit_request, name="submit_request"),
    path('view/', view_request, name="view_request"),
    path('manage/', manage_request, name="manage_request"),
    path('update_request_status/<int:pk>/', update_request_status, name='update_request_status'),
    path('<int:id>/cancel/', cancel_request, name="cancel_request")
]
