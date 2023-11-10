from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import Group, Permission

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



# This will be the Parent 
class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    groups = models.ManyToManyField(Group, related_name='newuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='newuser_permissions')

    def __str__(self):
        return self.user_name








'''

# Abstract Parent Class
class Parent_User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64) # Note: MODIFY to a HASH
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
 
    class Meta: # tells Django not to create a database table for this class.
            abstract = True
    

class Administrator(Parent_User): # Child Class inherits from User Abstract Class

    def __str__(self):
         return(f"{self.first_name} {self.last_name}")
    

class Employee(Parent_User): # Child Class inherits from User Abstract Class

    EMPLOYEE_TYPE = (
         ('Chief Executive Officer', 'Chief Executive Officer'),
         ('Chief Financial Officer', 'Chief Financial Officer'),
         ('Chief Operating Officer', 'Chief Operating Officer'),
         ('Chief Marketing Officer', 'Chief Marketing Officer'),
         ('Chief Technology Officer', 'Chief Technology Officer'),
         ('Vice President', 'Vice President'),
         ('Director', 'Director'),
         ('Manager', 'Manager'),
    )

    employee_type = models.CharField(max_length=30, choices=EMPLOYEE_TYPE)
    available_pto = models.PositiveIntegerField(default=15)
    available_sickdays = models.PositiveIntegerField(default=15)
    
    def __str__(self):
         return(f"{self.first_name} {self.last_name}")

         '''