from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# from django.utils import timezone

# Abstract Parent Class
class User(models.Model):
    user_id = models.AutoField(primary_key=True) # Automatic Primary Key
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64) # Note: MODIFY to a HASH
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=64)
    # email = models.EmailField()
    # phone_number = PhoneNumberField()

    class Meta: # tells Django not to create a database table for this class.
            abstract = True
    

class Admin(User): # Child Class inherits from User Abstract Class

    def __str__(self):
        return str(self.user_id)
    

class Employee(User): # Child Class inherits from User Abstract Class
    employee_type = models.CharField(max_length=30)
    available_pto = models.PositiveIntegerField(default=15)
    available_sickdays = models.PositiveIntegerField(default=15)
    
    def __str__(self):
        return str(self.user_id)
