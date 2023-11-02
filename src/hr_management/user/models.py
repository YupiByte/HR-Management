from django.db import models

# Parent Class
class User(models.Model):
    user_id = models.AutoField(primary_key=True) # Automatic Primary Key
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64) # Note: MODIFY to a HASH
    full_name = models.CharField(max_length=64)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
# Child Class inherits from User
class Admin(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.admin.username
    
# Child Class inherits from User
class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    employee_type = models.CharField(max_length=3)
    available_pto = models.IntegerField()
    available_sickdays = models.IntegerField()

    def __str__(self):
        return self.employee.username


