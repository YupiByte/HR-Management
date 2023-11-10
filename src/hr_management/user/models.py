from django.db import models

# Abstract Parent Class
class Parent_User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64) # Note: MODIFY to a HASH
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    
    #     class Meta: # tells Django not to create a database table for this class.
#             abstract = True

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

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
