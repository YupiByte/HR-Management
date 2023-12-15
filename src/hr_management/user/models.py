from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class CustomAccountManager(BaseUserManager): # Manager for the custom user model
    # Overwrite create_superuser
    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Employee(AbstractBaseUser, PermissionsMixin): # Extend Application's User from AbstractBaseUser to let Django know we are using a custom user model
    # Following the existing Django model
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(
        max_length=150, 
        validators=[RegexValidator('^[a-zA-ZñÑáéíóúüÁÉÍÓÚÜ\s]+$')] # Accept only Latin letters
        )
    last_name = models.CharField(
        max_length=150,
        validators=[RegexValidator('^[a-zA-ZñÑáéíóúüÁÉÍÓÚÜ\s]+$')] # Accept only Latin letters
        )
    phone = PhoneNumberField()

    EMPLOYEE_TYPE = (
        ('CEO', 'Chief Executive Officer'),
        ('Vice President', 'Vice President'),
        ('Software Engineer', 'Software Engineer'),
        ('System Administrator', 'System Administrator'),
        ('QA Engineer', 'QA Engineer'),
        ('Director', 'Director'),
        ('Manager', 'Manager'),
        ('Administrator', 'Administrator'),
        ('HR Administrator', 'HR Administrator'),
        ('Intern', 'Intern'),
    )

    employee_type = models.CharField(max_length=30, choices=EMPLOYEE_TYPE)
    available_pto = models.PositiveIntegerField(default=15)
    available_sickdays = models.PositiveIntegerField(default=15)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # Changed to default=True because we are not validating account through email just yet

    objects = CustomAccountManager() # Tell NewUser to use the custom manager

    USERNAME_FIELD = 'email' # email will be the user's login identifier
    REQUIRED_FIELDS = ['username', 'first_name'] # list of fields that will be prompted when the user creates a new superuser. No need to include email here bc it will already be required.

    def __str__(self):
        return self.username


