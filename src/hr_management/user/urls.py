from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("manage_employees/", views.manage_employees, name="manage_employees"),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('home/', views.home, name='home'),
    path('tmp/', views.tmp, name='tmp'),
]
