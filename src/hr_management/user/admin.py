from django.contrib import admin
from .models import Administrator, Employee

# Register models
admin.site.register(Administrator)
admin.site.register(Employee)
