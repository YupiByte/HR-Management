from django import forms
from .models import Request
from datetime import timedelta, datetime, date
from uuid import uuid1
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# Generates a request ticket ID
def generate_request_id():
    return str(uuid1())[:8]

# Get from user page
def get_employee_id():
    '''
    '''
    get_id = "1324"

    return get_id



# Calculating for total requested days,
# subtracting the weekend days
# Still a WIP, needs testing
def days_requested(start, end):

    total_days = (end - start).days + 1

    # Account for weekend days
    weekend_days = sum(1 for single_date in \
                    [start + timedelta(days=n)\
                    for n in range(total_days)]\
                    if single_date.weekday() in [5,6])

    return total_days - weekend_days


# TO-DO: Make immutable fields!
# Admin page, view requests, can only change status fields.
# Admin can click on a box, accept or decline which then updates
# the Request's status field.

class RequestCreateForm(forms.ModelForm):

    # Crispy Form utilities
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('request_submit')
        self.helper.form_method = 'GET'
        self.helper.add_input(Submit('submit', 'Submit'))


    REQ_CHOICES = (
        ('PTO', 'Paid Time Off'),
        ('Sick Day', 'Sick Day'),
    )

    # Must be read-only, value given by getting current user's employee_id
    employee_id = forms.CharField(required=True, initial=get_employee_id(), \
                                label='employee_id',
                                widget=forms.TextInput(
                                attrs={"placeholder": "id", \
                                       "read-only": "read-only"}
                                )
                                )


    # Must be read-only
    request_id = forms.CharField(required=True,  initial=generate_request_id(), \
                                label='request_id',
                                widget=forms.TextInput(
                                attrs={"placeholder": "req_id", \
                                       "read-only": "read-only"}
                                )
                                )

    # Must be read-only; Possibly hide the field
    request_type = forms.ChoiceField(choices=REQ_CHOICES, \
                                    label='Request Type', \
                                    widget=forms.RadioSelect())

    request_status = forms.CharField(label='Request Status', initial='Pending')

    start_date = forms.DateField(required=True, label='Start', \
                                widget=forms.DateInput( \
                                attrs={'type': 'date', 'min': \
                                datetime.now().date()}), initial=date.today)
    
    end_date = forms.DateField(required=True, label='End', \
                                widget=forms.DateInput( \
                                attrs={'type': 'date', 'min': \
                                datetime.now().date()}), initial=date.today)

    class Meta:
        model = Request
        # fields = "__all__"
        fields = ['employee_id', 'request_id', \
                'request_type', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date should be before the end date.")


# Utilized by the Administrator to manage the request
# Pseudocode...
class RequestManage(forms.ModelForm):

    class Meta:
        model = Request
        fields = '__all__'

    req_choices = (
        ('Accept', 'Accept'),
        ('Reject', 'Reject')
    )
    
    manage_request = forms.ChoiceField(label='Manage Request', \
                    widget=forms.SelectMultiple(choices=req_choices))
    

    if (manage_request == 'Accept'):
        Request.request_status = 'Accepted'
    else:
        Request.request_status = 'Declined'

    