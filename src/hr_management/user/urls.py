from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('tmp/', views.tmp, name='tmp'),

    # Admin Pages
    path('admin_home/', views.admin_home, name='admin_home'), 
    path("manage_employees/", views.manage_employees, name="manage_employees"),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('employee_record/<int:pk>', views.employee_record, name='employee_record'),
    path('delete_employee/<int:pk>', views.delete_employee, name='delete_employee'),
    path('update_employee/<int:pk>', views.update_employee, name='update_employee'),

    # Employee Pages
    path('employee_home', views.employee_home, name='employee_home'),
    # path('edit_profile/<int:pk>', views.edit_profile, name='edit_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
    
]
