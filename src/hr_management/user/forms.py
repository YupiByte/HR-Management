from django import forms
from .models import Employee
from phonenumber_field.modelfields import PhoneNumberField



# ======================> FROM 4-hr tutorial
# class CreateEmployeeForm(forms.ModelForm):
#     username            = forms.CharField()
#     password            = forms.CharField()
#     first_name          = forms.CharField()
#     last_name           = forms.CharField()
#     email               = forms.EmailField()
#     phone_number        = PhoneNumberField()
#     employee_type       = forms.CharField()
#     available_pto       = forms.IntegerField()
#     available_sickdays  = forms.IntegerField()

#     class Meta:
#         model = Employee
#         fields = [
#             'username',
#             'password',
#             'first_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'employee_type',
#             'available_pto',
#             'available_sickdays',
#         ]
# <=======================================