from django import forms
from .models import Request

class RequestCreateForm(forms.ModelForm):


    REQ_CHOICES = (
        ('PTO', 'Paid Time Off'),
        ('Sick Day', 'Sick Day'),
    )

    employee_id = forms.CharField(required=True, label='employee_id',
                                    widget=forms.TextInput(
                                    attrs={"placeholder": "id"}
                                  ))

    request_id = forms.CharField(required=True, label='request_id',
                                    widget=forms.TextInput(
                                    attrs={"placeholder": "req_id"}
                                  ))

    request_type = forms.ChoiceField(choices=REQ_CHOICES, label='Request Type')
    request_status = forms.CharField(label='Request Status')

    start_date = forms.DateField(label='Start of Leave')
    end_date = forms.DateField(label='End of Leave')


    class Meta:
        model = Request
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date should be before the end date.")


# class LeaveRequestForm(forms.ModelForm):

#     class Meta:
#         model = Request
#         # fields = ['start_date', 'end_date', 'request_type']
#         fields = '__all__'
    
#     def clean(self):
#         cleaned_data = super().clean()
#         start_date = cleaned_data.get('start_date')
#         end_date = cleaned_data.get('end_date')

#         if start_date and end_date and start_date > end_date:
#             raise forms.ValidationError("Start date should be before the end date.")
