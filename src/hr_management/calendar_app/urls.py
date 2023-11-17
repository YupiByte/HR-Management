from django.urls import path
from .views import *

app_name = 'calendar_app'

urlpatterns = [
    path('', view_calendar, name="view_calendar")
]
