from django.urls import path
from . import views
from calendar_app import views as calendar_view
from req_leave import views as req_leave
from publication import views as publications_view
from authentication import views as auth_views

urlpatterns = [

    # Authentication 
    path('', auth_views.login_user, name='login'), 
    path('logout/', auth_views.logout_user, name='logout'), 

    # Admin Pages
    path('admin_home/', views.admin_home, name='admin_home'),
    path("manage_employees/", views.manage_employees, name="manage_employees"),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('employee_record/<int:pk>', views.employee_record, name='employee_record'),
    path('delete_employee/<int:pk>', views.delete_employee, name='delete_employee'),
    path('update_employee/<int:pk>', views.update_employee, name='update_employee'),

    # Employee Pages
    path('employee_home', views.employee_home, name='employee_home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    # Calendar
    path('calendar/', calendar_view.view_calendar, name='calendar'),

    # Leave Request
    # path('req_leave/', req_leave, name='req_leave'),
    path('manage_req/', req_leave.manage_request, name='manage_req'),
    path('submit_req/', req_leave.submit_request, name='submit_req'),
    path('view_req/', req_leave.view_request, name='view_req'), # For Empoyee to view request history

    # Publications
    path('publications/', publications_view.view_publications, name='publications'), 
    path('create/', publications_view.create_publication, name='create_publication'), # For Admin to create and view publications

    # Help
    path('help/', views.help, name='help'),


]
