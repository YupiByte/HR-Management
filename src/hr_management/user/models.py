from django.db import models


class User(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64) # Note: MODIFY to a HASH
    full_name = models.CharField(max_length=64)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.username
