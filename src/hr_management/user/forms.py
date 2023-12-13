from .models import Employee
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django import forms


EMPLOYEE_TYPE = (
    ("", "----"),
    ("Chief Executive Officer", "Chief Executive Officer"),
    ("Chief Financial Officer", "Chief Financial Officer"),
    ("Chief Operating Officer", "Chief Operating Officer"),
    ("Chief Marketing Officer", "Chief Marketing Officer"),
    ("Chief Technology Officer", "Chief Technology Officer"),
    ("Vice President", "Vice President"),
    ("Director", "Director"),
    ("Manager", "Manager"),
    ("Administrator", "Administrator"),
)


class RegisterEmployeeForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter Only Latin Alphabet Characters</small></span>',
    )
    last_name = forms.CharField(
        required=True,
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter Only Latin Alphabet Characters</small></span>',
    )
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    phone = PhoneNumberField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Phone", "class": "form-control"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter a valid phone number (e.g. +12125552368).</small></span>',
        label="",
    )
    employee_type = forms.ChoiceField(
        required=True,
        choices=EMPLOYEE_TYPE,
        widget=forms.Select(
            attrs={"placeholder": "Position", "class": "form-control"}
        ),
        help_text ="<span class='form-text text-muted'><small>Choose the employee's position.</small></span>",
        label="",
    )
    available_pto = forms.IntegerField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Assigned PTO", "class": "form-control"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter the amount of Paid Time Off assigned to the employee.</small></span>',
        label="",
    )
    available_sickdays = forms.IntegerField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Assigned Sick Days", "class": "form-control"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter the amount of Paid Sick Days assigned to the employee.</small></span>',
        label="",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "phone",
            "employee_type",
            "available_pto",
            "available_sickdays",
            "is_staff",
        )

    def __init__(self, *args, **kwargs):
        super(RegisterEmployeeForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>Password can't be too similar to employee's personal information.</li><li>Password must contain at least 8 characters.</li><li>Password can't be a commonly used password.</li><li>Password can't be entirely numeric.</li></ul>"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateEmployeeForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "username", "class": "form-control"}
        ),
        label="Username",
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter Only Latin Alphabet Characters</small></span>',
        label="First Name",
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter Only Latin Alphabet Characters</small></span>',
        label="Last Name",
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
        label="Email",
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={"placeholder": "Phone", "class": "form-control"}
        ),
        label="Phone Number",
    )
    employee_type = forms.ChoiceField(
        required=True,
        choices=EMPLOYEE_TYPE,
        widget=forms.Select(
            attrs={
                "placeholder": "Position",
                "class": "form-control",
            }
        ),
        label="Employee Type",
    )
    available_pto = forms.IntegerField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Available PTO", "class": "form-control"}
        ),
        label="Available PTO",
    )
    available_sickdays = forms.IntegerField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Available Sick Days", "class": "form-control"}
        ),
        label="Available Sick Days",
    )

    class Meta:
        # model = Employee
        model = get_user_model()
        exclude = ("user", "password", "last_login", "user_permissions", "is_superuser", "groups")


class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter Only Latin Alphabet Characters</small></span>',
        label="First Name",
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
        help_text ='<span class="form-text text-muted"><small>Enter Only Latin Alphabet Characters</small></span>',
        label="Last Name",
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
        label="Email",
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={"placeholder": "Phone", "class": "form-control"}
        ),
        label="Phone Number",
    )

    
    class Meta:
        # model = Employee
        model = get_user_model()
        exclude = ("user", 
                   "last_login", 
                   "user_permissions", 
                   "is_superuser", 
                   "groups", 
                   "password", 
                   "username", 
                   "employee_type", 
                   "available_pto",
                   "available_sickdays",
                   "is_staff",
                   "is_active",)