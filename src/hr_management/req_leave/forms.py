from django import forms
from .models import Request
from datetime import timezone, date
from uuid import uuid1


def generate_request_id():
    return str(uuid1())[:8]

def get_employee_id():
    '''
    '''
    get_id = "1324"

    return get_id


# TO-DO: Make immutable fields!
# Admin page, view requests, can only change status fields.
# Admin can click on a box, accept or decline which then updates
# the Request's status field.

class RequestCreateForm(forms.ModelForm):

    REQ_CHOICES = (
        ('PTO', 'Paid Time Off'),
        ('Sick Day', 'Sick Day'),
    )

    # Must be read-only, value given by getting current user's employee_id
    employee_id = forms.CharField(required=True, initial=get_employee_id(), \
                                label='employee_id',
                                widget=forms.TextInput(
                                attrs={"placeholder": "id"}
                                ))


    # Must be read-only
    request_id = forms.CharField(required=True,  initial=generate_request_id, \
                                label='request_id',
                                widget=forms.TextInput(
                                attrs={"placeholder": "req_id"}
                                ))

    # Must be read-only; Possibly hide the field
    request_type = forms.ChoiceField(choices=REQ_CHOICES, label='Request Type')
    request_status = forms.CharField(label='Request Status', initial='Pending')

    start_date = forms.DateField(required=True, label='Start of Leave', \
                                 widget=forms.SelectDateWidget(), initial=date.today)
    
    end_date = forms.DateField(required=True, label='End of Leave', \
                               widget=forms.SelectDateWidget(), initial=date.today)


    class Meta:
        model = Request
        fields = "__all__"

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

    