from django.db import models

# Abstract Parent Class
class User(models.Model):
    user_id = models.AutoField(primary_key=True) # Automatic Primary Key
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64) # Note: MODIFY to a HASH
    full_name = models.CharField(max_length=64)
    is_admin = models.BooleanField(default=False)

    class Meta: # Tells Django not to create a database table for this class.
            abstract = True
    
# Child Class inherits from User
class Admin(User):
    # admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # is_admin = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user_id)
    
# Child Class inherits from User
class Employee(User):
    # employee = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    employee_type = models.CharField(max_length=30)
    available_pto = models.PositiveIntegerField(default=15)
    available_sickdays = models.PositiveIntegerField(default=15)
    
    def __str__(self):
        return str(self.user_id)
