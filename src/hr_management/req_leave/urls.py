from django.urls import path, include
from .views import *

urlpatterns = [
    path('', submit_request, name="submit_request"),
    path('view/', view_request, name="view_request"),
    path('manage/', manage_request, name="manage_request"),
    path('update_request_status/<int:pk>/', update_request_status, name='update_request_status')
]