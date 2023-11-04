from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"), # Remove?
    path("admin_employees/", views.admin_employees, name="admin_employees"),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('home/', views.home, name='home'),
]
