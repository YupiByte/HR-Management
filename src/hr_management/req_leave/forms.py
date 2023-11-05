from django import forms
from .models import Request

class LeaveRequestForm(forms.ModelForm):

    class Meta:
        model = Request
        # fields = ['start_date', 'end_date', 'request_type']
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date should be before the end date.")
