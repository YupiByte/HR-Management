from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.utils import timezone

# Abstract Parent Class
class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64) # Note: MODIFY to a HASH
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    phone_number = PhoneNumberField()

    class Meta: # tells Django not to create a database table for this class.
            abstract = True
    

class Admin(User): # Child Class inherits from User Abstract Class

    def __str__(self):
        return str(self.user_id)
    

class Employee(User): # Child Class inherits from User Abstract Class

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
        return str(self.id)
